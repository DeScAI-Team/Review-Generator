import {
  IPNFT_CONTRACT_ADDRESS,
  MOLECULE_GRAPHQL_ENDPOINT,
} from "./molecule-config-bridge.js"

const GET_IPNFT_QUERY = `
query GetIPNFT($id: ID!) {
  ipnft(id: $id) {
    id
    createdAt
    updatedAt
    mintedAt
    chainId
    tokenUri
    symbol
    name
    description
    image
    externalUrl
    initialSymbol
    organization
    topic
    trlValue
    trlRationale
    fundingAmountCurrency
    fundingAmountValue
    fundingAmountDecimals
    fundingAmountCurrencyType
    schemaVersion
    userId
    owner {
      id
      address
    }
    researchLead {
      id
      name
      email
    }
    agreements {
      id
      type
      url
      mimeType
      contentHash
    }
    ipt {
      id
      l2TokenAddress
      holderCount
      symbol
      name
      decimals
      totalIssued
      circulatingSupply
      markets {
        id
        name
        chainId
        pairAddress
        usdPrice
        liquidityUsd
        tradingVolume24hr
        marketCapUsd
        usdPrice24hrPercentageChange
      }
    }
  }
}
`

const LIST_IPTS_FOR_IPNFT = `
query IptsForIpnft($ipnftId: String!, $limit: Int) {
  ipts(limit: $limit, filterBy: { ipnftId: $ipnftId }) {
    id
    createdAt
    updatedAt
    mintedAt
    l2TokenAddress
    holderCount
    symbol
    name
    decimals
    totalIssued
    circulatingSupply
    agreementCid
    agreementMimeType
    image
    links
    capped
    ipnftId
    ipnft {
      id
      symbol
      name
      topic
      organization
    }
    originalOwner {
      id
      address
    }
    markets {
      id
      name
      chainId
      pairAddress
      liquidityUsd
      tradingVolume24hr
      usdPrice
      usdPrice24hrPercentageChange
      marketCapUsd
    }
  }
}
`

/** @deprecated Docs-style id; current API resolves `ipnft(id)` with the bare token id string. */
export function buildDataApiIpnftId(
  tokenId: string,
  chainId: string | number = 1,
): string {
  return `${IPNFT_CONTRACT_ADDRESS}_${tokenId}_${chainId}`
}

export async function fetchIpnftProfile(
  ipnftId: string,
): Promise<Record<string, unknown> | null> {
  const apiKey = process.env.MOLECULE_API_KEY
  if (!apiKey) {
    throw new Error("MOLECULE_API_KEY environment variable is not set")
  }

  const response = await fetch(MOLECULE_GRAPHQL_ENDPOINT, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "x-api-key": apiKey,
    },
    body: JSON.stringify({
      query: GET_IPNFT_QUERY,
      variables: { id: ipnftId },
    }),
  })

  if (!response.ok) {
    throw new Error(
      `GraphQL request failed: ${response.status} ${response.statusText}`,
    )
  }

  const result = (await response.json()) as {
    data?: { ipnft?: Record<string, unknown> | null }
    errors?: { message: string }[]
  }

  if (result.errors?.length) {
    const msg = result.errors.map((e) => e.message).join("; ")
    if (/not found|item not found/i.test(msg)) {
      return null
    }
    throw new Error(`GraphQL errors: ${msg}`)
  }

  return result.data?.ipnft ?? null
}

/**
 * Resolve catalog IP-NFT: try bare `tokenId` first (current production API),
 * then optional legacy compound ids `{contract}_{tokenId}_{suffix}`.
 */
export async function fetchIpnftProfileForToken(
  tokenId: string,
  compoundChainSuffixes: string[],
): Promise<{
  queriedId: string
  profile: Record<string, unknown> | null
  attemptedIds: string[]
}> {
  const attempted: string[] = []

  const bare = tokenId
  attempted.push(bare)
  let profile = await fetchIpnftProfile(bare)
  if (profile) {
    return { queriedId: bare, profile, attemptedIds: attempted }
  }

  for (const suf of compoundChainSuffixes) {
    const id = buildDataApiIpnftId(tokenId, suf)
    if (attempted.includes(id)) continue
    attempted.push(id)
    profile = await fetchIpnftProfile(id)
    if (profile) {
      return { queriedId: id, profile, attemptedIds: attempted }
    }
  }

  return {
    queriedId: attempted[attempted.length - 1] ?? bare,
    profile: null,
    attemptedIds: attempted,
  }
}

export async function fetchIptsForIpnftFilterId(
  ipnftFilterId: string,
  limit = 25,
): Promise<Record<string, unknown>[]> {
  const apiKey = process.env.MOLECULE_API_KEY
  if (!apiKey) {
    throw new Error("MOLECULE_API_KEY environment variable is not set")
  }

  const response = await fetch(MOLECULE_GRAPHQL_ENDPOINT, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "x-api-key": apiKey,
    },
    body: JSON.stringify({
      query: LIST_IPTS_FOR_IPNFT,
      variables: { ipnftId: ipnftFilterId, limit },
    }),
  })

  if (!response.ok) {
    throw new Error(
      `GraphQL IPT request failed: ${response.status} ${response.statusText}`,
    )
  }

  const result = (await response.json()) as {
    data?: { ipts?: Record<string, unknown>[] }
    errors?: { message: string }[]
  }

  if (result.errors?.length) {
    const msg = result.errors.map((e) => e.message).join("; ")
    throw new Error(`GraphQL IPT errors: ${msg}`)
  }

  return result.data?.ipts ?? []
}
