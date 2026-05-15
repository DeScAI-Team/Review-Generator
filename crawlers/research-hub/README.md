ResearchHub Crawler –

Project Overview
This crawler fetches data from ResearchHub API, processes various post types (papers, RFPs, proposals, bounties, questions, comments), and outputs self‑contained JSON‑LD files ready for minting as Knowledge Assets on the OriginTrail DKG. It supports incremental crawling and maintains all relationships.

Architecture
The project is organized into modular components:
- core/: Base classes and utilities
  - api_client.py: Handles HTTP requests, pagination, rate limiting, and retries.
  - incremental.py: Tracks last crawl timestamp (.last_run) and determines if a post is new.
  - base_crawler.py: Abstract class inherited by all parsers; provides save_post() and common attributes.
- parsers/: Type‑specific parsers
  - paper_parser.py – for research papers (/journal_feed/)
  - rfp_parser.py – for RFPs (/grant_feed/) – stub
  - proposal_parser.py – for proposals (/funding_feed/) – stub
  - bounty_parser.py – for bounties (/bounty/) – stub
  - question_parser.py – for questions (/researchhubpost/) – stub
  - comment_parser.py – for comments and reviews (fetched per paper)
- orchestrator.py: Coordinates multi‑type crawls, runs phases, builds relationship index, saves manifest.
- crawl.py: Unified CLI entry point (commands: platform, status, monitor, clean, stats, help).
- monitor.py: Live dashboard showing crawl progress.

Setup
Prerequisites: Python 3.9+, dependencies in requirements.txt.
Installation: pip install -r requirements.txt
Configuration: No config file required; API endpoints are hardcoded. Adjust delay in crawl.py for rate limiting.

Orchestrator Commands (Detailed)

All commands are run via crawl.py. Use --help for quick reference.

1. platform – Crawl platform content
   Usage: python crawl.py platform <post_type> [options]
   <post_type> can be:
     - all – all supported types (papers, rfps, proposals, bounties, questions, comments)
     - papers – only papers
     - rfps – only RFPs
     - proposals – only proposals
     - bounties – only bounties
     - questions – only questions
     - comments – only comments (requires --paper-id or runs after papers)
   Options:
     --mode {full,incremental,test} : full: ignore last run, crawl everything; incremental: only new/updated posts; test: one page per endpoint. Default: incremental.
     --delay SECONDS : seconds between API requests. Default: 1.0.
     --max-pages N : limit pages per endpoint. Default: no limit.
     --output-dir PATH : output directory. Default: output/.
     --paper-id ID : for comments type, fetch comments for a specific paper.
     --resume : resume a previously interrupted crawl (uses checkpoint).
     --force : force re‑crawl even if post already exists (overrides incremental).
   Examples:
     python crawl.py platform all --mode full
     python crawl.py platform all
     python crawl.py platform papers --mode test
     python crawl.py platform comments --paper-id 12345

2. status – Show crawl status
   Usage: python crawl.py status [--output-dir PATH]
   Options:
     --output-dir PATH : output directory to examine. Default: output/.


3. monitor – Live progress dashboard
   Usage: python crawl.py monitor [--output-dir PATH] [--interval SECONDS]
   Options:
     --output-dir PATH : output directory to monitor. Default: output/.
     --interval SECONDS : refresh interval. Default: 5.
   Press Ctrl+C to exit.

4. clean – Remove output files
   Usage: python crawl.py clean [--output-dir PATH] [--type TYPE] [--force]
   Options:
     --output-dir PATH : output directory to clean. Default: output/.
     --type TYPE : what to clean: all, papers, rfps, proposals, bounties, questions, comments. Default: all.
     --force : skip confirmation prompt.
   Examples:
     python crawl.py clean
     python crawl.py clean --type papers --force

5. stats – Detailed statistics
   Usage: python crawl.py stats [--output-dir PATH]
   Options:
     --output-dir PATH : output directory to analyze. Default: output/.

6. help – Show detailed help
   Usage: python crawl.py help

Incremental Crawling Logic
- The crawler maintains a .last_run timestamp file.
- On each run, it compares the created_date (or published_date) of each item with that timestamp.
- Only items newer than the last run are processed.
- To force a full re‑crawl, use --mode full or delete .last_run.

Output Format
Each post is saved as an individual JSON‑LD file in a subdirectory of the output directory:
- output/papers/
- output/rfps/
- output/proposals/
- output/bounties/
- output/questions/
- output/comments/
A crawl_manifest.json is generated with start/end times, counts per type, and any errors. A relationship_index.json optionally lists all cross‑links between assets.

Adding New Post Types
1. Create a new parser in parsers/ inheriting from BaseCrawler.
2. Define FEED_ENDPOINT and implement transform_to_jsonld().
3. Add the parser to orchestrator.py’s parsers dictionary.
4. Update CLI in crawl.py if needed.

Dependencies
- requests – HTTP client
- python-dateutil – robust date parsing
