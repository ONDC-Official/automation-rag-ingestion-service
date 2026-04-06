# ═══════════════════════════════════════════════════════════
# ONDC Beckn API — "on_support" action — valid field paths
# ═══════════════════════════════════════════════════════════
#
# HOW TO READ:
#   Each nested key represents a JSONPath segment.
#   Keys ending with [*] are arrays.
#   Values marked "$ref:TypeName" expand to the type defined below.
#   "string" means it's a leaf field (terminal value).
#
# TO RECONSTRUCT A FULL PATH:
#   Join the nesting chain with "." and prefix with "$."
#   e.g. context → location → descriptor → (expand Descriptor) → name
#   becomes: $.context.location.descriptor.name
#
# TOTAL UNIQUE PATHS: 58

# ── Reusable Type Definitions ──────────────────────────────

## City
name: string
code: string

# ── Main Schema ────────────────────────────────────────────

context:
  domain: string
  location:
    id: string
    descriptor:
      name: string
      code: string
      short_desc: string
      long_desc: string
      additional_desc:
        url: string
        content_type: string
      media[*]:
        mimetype: string
        url: string
        signature: string
        dsa: string
      images[*]:
        url: string
        size_type: string
        width: string
        height: string
    map_url: string
    gps: string
    address: string
    city: $ref:City
    district: string
    state: $ref:City
    country: $ref:City
    area_code: string
    circle:
      gps: string
      radius:
        type: string
        value: string
        estimated_value: string
        computed_value: string
        range:
          min: string
          max: string
        unit: string
    polygon: string
    3dspace: string
    rating: string
  action: string
  version: string
  bap_id: string
  bap_uri: string
  bpp_id: string
  bpp_uri: string
  transaction_id: string
  message_id: string
  timestamp: string
  key: string
  ttl: string
message:
  support:
    order_id: string
    ref_id: string
    callback_phone: string
    phone: string
    email: string
    url: string
error:
  code: string
  paths: string
  message: string

# ── Example Full Path Expansions ───────────────────────────
# $.error.code
# $.context.domain
# $.context.bap_uri
# $.message.support.url
# $.message.support.ref_id
# $.context.location.3dspace
# $.context.location.area_code
# $.context.location.country.code
# $.context.location.circle.radius.unit
# $.context.location.descriptor.media[*].dsa