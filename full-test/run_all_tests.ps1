<#
.SYNOPSIS
    Full integration test suite for all four DeScAi pipelines.
.DESCRIPTION
    Runs 12 tests (3 per pipeline): articles, compounds, DAOs, proposals.
    Processing output goes to full-test/<pipeline>/.
    Review artifacts are copied to full-test/reviews/<pipeline>/.

    Expects two vLLM instances:
      - LLM  (text)  on LLM_BASE_URL  (default http://localhost:8000/v1)
      - OCR  (vision) on OCR_BASE_URL  (default http://localhost:8001/v1)

    Articles and DAOs run in two phases (OCR then LLM) since read-paper.py
    and the text steps share the same VLLM_BASE_URL env var.
#>

$ErrorActionPreference = "Continue"

# ---------------------------------------------------------------------------
# Paths (resolve relative to repo root, one level up from this script)
# ---------------------------------------------------------------------------
$ScriptDir  = Split-Path -Parent $MyInvocation.MyCommand.Definition
$RepoRoot   = (Resolve-Path "$ScriptDir\..").Path
$TestRoot   = $ScriptDir

Set-Location $RepoRoot

# ---------------------------------------------------------------------------
# Environment -- models & vLLM
# ---------------------------------------------------------------------------
$LLM_URL = if ($env:LLM_BASE_URL) { $env:LLM_BASE_URL } else { "http://127.0.0.1:8001/v1" }
$OCR_URL = if ($env:OCR_BASE_URL) { $env:OCR_BASE_URL } else { "http://127.0.0.1:8000/v1" }

$env:VALIDATOR_MODEL   = if ($env:VALIDATOR_MODEL)  { $env:VALIDATOR_MODEL }  else { "/model" }
$env:READ_PAPER_MODEL  = if ($env:READ_PAPER_MODEL) { $env:READ_PAPER_MODEL } else { "nanonets/Nanonets-OCR2-3B" }
$env:VLLM_API_KEY      = if ($env:VLLM_API_KEY)     { $env:VLLM_API_KEY }     else { "none" }

Write-Host "Config:" -ForegroundColor DarkGray
Write-Host "  LLM  endpoint : $LLM_URL  (model: $env:VALIDATOR_MODEL)" -ForegroundColor DarkGray
Write-Host "  OCR  endpoint : $OCR_URL  (model: $env:READ_PAPER_MODEL)" -ForegroundColor DarkGray

# ---------------------------------------------------------------------------
# Output directories
# ---------------------------------------------------------------------------
$dirs = @(
    "$TestRoot\articles",
    "$TestRoot\daos\MITY",
    "$TestRoot\daos\VITA-FAST",
    "$TestRoot\daos\CLAW",
    "$TestRoot\proposals\4459",
    "$TestRoot\proposals\32242",
    "$TestRoot\proposals\32269",
    "$TestRoot\reviews\articles",
    "$TestRoot\reviews\compounds\Rifampicin",
    "$TestRoot\reviews\compounds\Urolithin_A",
    "$TestRoot\reviews\compounds\kisspeptin-10",
    "$TestRoot\reviews\daos\MITY",
    "$TestRoot\reviews\daos\VITA-FAST",
    "$TestRoot\reviews\daos\CLAW",
    "$TestRoot\reviews\proposals\4459",
    "$TestRoot\reviews\proposals\32242",
    "$TestRoot\reviews\proposals\32269"
)
foreach ($d in $dirs) {
    if (-not (Test-Path $d)) { New-Item -ItemType Directory -Path $d -Force | Out-Null }
}

# ---------------------------------------------------------------------------
# Bookkeeping
# ---------------------------------------------------------------------------
$results  = @()
$testNum  = 0
$passed   = 0
$failed   = 0

function Write-Banner($label) {
    $script:testNum++
    Write-Host ""
    Write-Host ("=" * 70) -ForegroundColor DarkCyan
    Write-Host "  TEST $script:testNum : $label" -ForegroundColor Cyan
    Write-Host ("=" * 70) -ForegroundColor DarkCyan
}

function Record-Result($name, [bool]$ok, $detail) {
    if ($ok) {
        Write-Host "PASSED" -ForegroundColor Green
        if ($detail) { Write-Host "  $detail" }
        $script:passed++
        $script:results += [pscustomobject]@{ Test = $name; Result = "PASSED" }
    } else {
        Write-Host "FAILED" -ForegroundColor Red
        if ($detail) { Write-Host "  $detail" -ForegroundColor Red }
        $script:failed++
        $script:results += [pscustomobject]@{ Test = $name; Result = "FAILED" }
    }
}

# ===================================================================
#  ARTICLES  (3 tests)
#  Two-phase: OCR on OCR_URL, then LLM on LLM_URL
#  Runner: articles/pipeline/run_full_pipeline.py
# ===================================================================

$articleTests = @(
    @{ Id = "9631437";  Label = "Zebrafish ALS (empirical biology)" },
    @{ Id = "11152101"; Label = "Protein binder AGEs (computational)" },
    @{ Id = "11079432"; Label = "Wim Hof breathing (clinical)" }
)

foreach ($t in $articleTests) {
    $paperId   = $t.Id
    $label     = $t.Label
    $jsonPath  = "$RepoRoot\crawlers\output\researchhub\papers\PaperRecord_$paperId.json"
    $testLabel = "Articles -- $label (PaperRecord_$paperId)"

    Write-Banner $testLabel

    if (-not (Test-Path $jsonPath)) {
        Record-Result $testLabel $false "Input JSON not found: $jsonPath"
        continue
    }

    $rec    = Get-Content $jsonPath -Raw | ConvertFrom-Json
    $pdfUrl = $rec.pdf_url
    if (-not $pdfUrl) {
        Record-Result $testLabel $false "No pdf_url in $jsonPath"
        continue
    }

    Write-Host "  PDF URL: $pdfUrl"

    # Phase 1: OCR (vision model)
    Write-Host "  Phase 1: OCR -> $OCR_URL" -ForegroundColor DarkYellow
    $env:VLLM_BASE_URL = $OCR_URL
    python "$RepoRoot\articles\pipeline\run_full_pipeline.py" $pdfUrl `
        --output-dir "$TestRoot\articles" `
        --model $env:VALIDATOR_MODEL `
        --skip-upload `
        --stop-after reader

    if ($LASTEXITCODE -ne 0) {
        $env:VLLM_BASE_URL = $LLM_URL
        Record-Result $testLabel $false "OCR phase exited $LASTEXITCODE"
        continue
    }

    # Phase 2: LLM (text model)
    Write-Host "  Phase 2: LLM -> $LLM_URL" -ForegroundColor DarkYellow
    $env:VLLM_BASE_URL = $LLM_URL

    # Find the work folder just created (has full.md from OCR)
    $workDirs = Get-ChildItem "$TestRoot\articles" -Directory | Sort-Object LastWriteTime -Descending
    $latestWork = $workDirs | Select-Object -First 1

    if (-not $latestWork) {
        Record-Result $testLabel $false "No work folder found after OCR phase"
        continue
    }

    python "$RepoRoot\articles\pipeline\run_full_pipeline.py" $latestWork.FullName `
        --output-dir "$TestRoot\articles" `
        --model $env:VALIDATOR_MODEL `
        --skip-upload `
        --from-step add_data

    if ($LASTEXITCODE -ne 0) {
        Record-Result $testLabel $false "LLM phase exited $LASTEXITCODE"
        continue
    }

    $reviewFile = $null
    $candidate = Join-Path $latestWork.FullName "output\review.json"
    if (Test-Path $candidate) { $reviewFile = $candidate }

    if ($reviewFile) {
        $reviewDest = "$TestRoot\reviews\articles\$paperId"
        if (-not (Test-Path $reviewDest)) { New-Item -ItemType Directory -Path $reviewDest -Force | Out-Null }
        Copy-Item (Join-Path $latestWork.FullName "output\*") -Destination $reviewDest -Recurse -Force
        Record-Result $testLabel $true "review.json -> $reviewDest"
    } else {
        Record-Result $testLabel $false "review.json not found under $($latestWork.FullName)"
    }
}

# Restore LLM URL for remaining pipelines
$env:VLLM_BASE_URL = $LLM_URL

# ===================================================================
#  COMPOUNDS  (3 tests)
#  Source: compound names (API-based discovery), no OCR needed
#  Runner: compounds/pipeline/single/run_review.py
#  Note: intermediates land in compounds/data/<name>/ (hardcoded)
# ===================================================================

$compoundTests = @(
    @{ Name = "Rifampicin";    SafeName = "Rifampicin" },
    @{ Name = "Urolithin A";   SafeName = "Urolithin_A" },
    @{ Name = "kisspeptin-10"; SafeName = "kisspeptin-10" }
)

foreach ($t in $compoundTests) {
    $cmpName   = $t.Name
    $safeName  = $t.SafeName
    $testLabel = "Compounds -- $cmpName"

    Write-Banner $testLabel

    $reviewDir  = "$TestRoot\reviews\compounds\$safeName"
    $reviewPath = "$reviewDir\$safeName-review.json"
    if (-not (Test-Path $reviewDir)) { New-Item -ItemType Directory -Path $reviewDir -Force | Out-Null }

    python "$RepoRoot\compounds\pipeline\single\run_review.py" `
        --compound $cmpName `
        --model $env:VALIDATOR_MODEL `
        --review-output $reviewPath

    if ($LASTEXITCODE -ne 0) {
        Record-Result $testLabel $false "Pipeline exited $LASTEXITCODE"
        continue
    }

    if (Test-Path $reviewPath) {
        Record-Result $testLabel $true "Review -> $reviewPath"
    } else {
        Record-Result $testLabel $false "review JSON not found at $reviewPath"
    }
}

# ===================================================================
#  DAOs  (3 tests)
#  Two-phase: OCR on OCR_URL (--stop-after ocr), then LLM on LLM_URL (--from-step llm)
#  Runner: DAOs/molecule/pipeline/run_dao_pipeline.py
# ===================================================================

$daoTests = @(
    @{ Symbol = "MITY";      Label = "Fission Bio mitochondria (3 PDFs)" },
    @{ Symbol = "VITA-FAST"; Label = "Autophagy activators (5 PDFs)" },
    @{ Symbol = "CLAW";      Label = "Percepta brain health (4 PDFs)" }
)

foreach ($t in $daoTests) {
    $symbol    = $t.Symbol
    $label     = $t.Label
    $ipnftDir  = "$RepoRoot\crawlers\output\molecule\ipnfts\$symbol"
    $outputDir = "$TestRoot\daos\$symbol"
    $testLabel = "DAOs -- $symbol ($label)"

    Write-Banner $testLabel

    if (-not (Test-Path $ipnftDir)) {
        Record-Result $testLabel $false "IPNFT dir not found: $ipnftDir"
        continue
    }

    # Phase 1: OCR (vision model)
    Write-Host "  Phase 1: OCR -> $OCR_URL" -ForegroundColor DarkYellow
    $env:VLLM_BASE_URL = $OCR_URL
    python "$RepoRoot\DAOs\molecule\pipeline\run_dao_pipeline.py" `
        --ipnft-dir $ipnftDir `
        --output-dir $outputDir `
        --model $env:VALIDATOR_MODEL `
        --skip-upload `
        --stop-after ocr

    if ($LASTEXITCODE -ne 0) {
        $env:VLLM_BASE_URL = $LLM_URL
        Record-Result $testLabel $false "OCR phase exited $LASTEXITCODE"
        continue
    }

    # Phase 2: LLM (text model)
    Write-Host "  Phase 2: LLM -> $LLM_URL" -ForegroundColor DarkYellow
    $env:VLLM_BASE_URL = $LLM_URL
    python "$RepoRoot\DAOs\molecule\pipeline\run_dao_pipeline.py" `
        --ipnft-dir $ipnftDir `
        --output-dir $outputDir `
        --model $env:VALIDATOR_MODEL `
        --skip-upload `
        --from-step llm

    if ($LASTEXITCODE -ne 0) {
        Record-Result $testLabel $false "LLM phase exited $LASTEXITCODE"
        continue
    }

    $daoReview = "$outputDir\synthesis\dao_review.json"
    if (Test-Path $daoReview) {
        $reviewDest = "$TestRoot\reviews\daos\$symbol"
        if (-not (Test-Path $reviewDest)) { New-Item -ItemType Directory -Path $reviewDest -Force | Out-Null }
        Copy-Item "$outputDir\synthesis\*" -Destination $reviewDest -Recurse -Force
        Record-Result $testLabel $true "dao_review.json -> $reviewDest"
    } else {
        Record-Result $testLabel $false "dao_review.json not found at $daoReview"
    }
}

# Restore LLM URL
$env:VLLM_BASE_URL = $LLM_URL

# ===================================================================
#  PROPOSALS  (3 tests)
#  Text-only, no OCR needed
#  Runner: proposals/pipeline/proposal_pipe.py
# ===================================================================

$proposalTests = @(
    @{ Id = "4459";  Label = "Wim Hof cancer inflammation" },
    @{ Id = "32242"; Label = "GPCR-ligand mapping" },
    @{ Id = "32269"; Label = "CAR T antigen-presenting cells" }
)

foreach ($t in $proposalTests) {
    $propId    = $t.Id
    $label     = $t.Label
    $inputJson = "$RepoRoot\crawlers\output\researchhub\proposals\proposal_$propId.json"
    $outputDir = "$TestRoot\proposals\$propId"
    $testLabel = "Proposals -- $propId ($label)"

    Write-Banner $testLabel

    if (-not (Test-Path $inputJson)) {
        Record-Result $testLabel $false "Input JSON not found: $inputJson"
        continue
    }

    python "$RepoRoot\proposals\pipeline\proposal_pipe.py" `
        --input-json $inputJson `
        --output-dir $outputDir `
        --skip-upload

    if ($LASTEXITCODE -ne 0) {
        Record-Result $testLabel $false "Pipeline exited $LASTEXITCODE"
        continue
    }

    $reviewFile = "$outputDir\review.json"
    if (Test-Path $reviewFile) {
        $reviewDest = "$TestRoot\reviews\proposals\$propId"
        if (-not (Test-Path $reviewDest)) { New-Item -ItemType Directory -Path $reviewDest -Force | Out-Null }
        Copy-Item "$outputDir\review.json"       -Destination $reviewDest -Force -ErrorAction SilentlyContinue
        Copy-Item "$outputDir\evidence_audit.md"  -Destination $reviewDest -Force -ErrorAction SilentlyContinue
        Record-Result $testLabel $true "review.json -> $reviewDest"
    } else {
        Record-Result $testLabel $false "review.json not found at $reviewFile"
    }
}

# ===================================================================
#  SUMMARY
# ===================================================================

Write-Host ""
Write-Host ("=" * 70) -ForegroundColor DarkCyan
Write-Host "  TEST SUITE SUMMARY" -ForegroundColor Cyan
Write-Host ("=" * 70) -ForegroundColor DarkCyan
Write-Host ""

$results | Format-Table -AutoSize

Write-Host ""
Write-Host "Total: $($results.Count)   Passed: $passed   Failed: $failed" -ForegroundColor $(if ($failed -eq 0) { "Green" } else { "Yellow" })
Write-Host ""

if ($failed -gt 0) {
    Write-Host "Some tests failed." -ForegroundColor Red
    exit 1
}

Write-Host "All tests passed." -ForegroundColor Green
exit 0
