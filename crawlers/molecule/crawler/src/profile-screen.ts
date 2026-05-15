/**
 * Heuristic: "competent" = indexed in Data API with enough catalog metadata to be useful
 * (not a null ipnft or a bare stub). Mirrors a healthy row like BeeARD / VITA-FAST.
 */
export function isCompetentCatalogProfile(
  ipnft: Record<string, unknown> | null,
): boolean {
  if (!ipnft || typeof ipnft !== "object") return false

  const name = String(ipnft.name ?? "").trim()
  if (name.length === 0) return false

  const desc = String(ipnft.description ?? "").trim()
  const topic = String(ipnft.topic ?? "").trim()
  const org = String(ipnft.organization ?? "").trim()
  const tokenUri = String(ipnft.tokenUri ?? "").trim()
  const externalUrl = String(ipnft.externalUrl ?? "").trim()
  const image = String(ipnft.image ?? "").trim()

  if (desc.length >= 40) return true
  if (desc.length >= 12 && (topic.length > 0 || org.length > 0)) return true
  if (tokenUri.length > 0 || externalUrl.length > 0) return true
  if (image.length > 0 && desc.length >= 20) return true
  return false
}

export type ProfileSkipReason =
  | "fetch_error"
  | "not_in_data_api"
  | "thin_metadata"

export function classifyProfileSkip(
  ipnft: Record<string, unknown> | null,
  hadFetchError: boolean,
): ProfileSkipReason | null {
  if (hadFetchError) return "fetch_error"
  if (!ipnft) return "not_in_data_api"
  if (!isCompetentCatalogProfile(ipnft)) return "thin_metadata"
  return null
}
