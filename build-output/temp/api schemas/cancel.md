# ═══════════════════════════════════════════════════════════
# ONDC Beckn API — "cancel" action — valid field paths
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
# TOTAL UNIQUE PATHS: 96

# ── Reusable Type Definitions ──────────────────────────────

## Descriptor
name: string
code: string
short_desc: string
long_desc: string
additional_desc: $ref:Additional_desc
media[*]: $ref:Media
images[*]: $ref:Images

## Media
mimetype: string
url: string
signature: string
dsa: string

## Images
url: string
size_type: string
width: string
height: string

## Additional_desc
url: string
content_type: string

## City
name: string
code: string

# ── Main Schema ────────────────────────────────────────────

context:
  domain: string
  location:
    id: string
    descriptor: $ref:Descriptor
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
  order_id: string
  cancellation_reason_id: string
  descriptor: $ref:Descriptor
  tags[*]:
    display: string
    descriptor: $ref:Descriptor
    list[*]:
      descriptor: $ref:Descriptor
      value: string
      display: string

# ── Example Full Path Expansions ───────────────────────────
# $.context.key
# $.message.order_id
# $.message.tags[*].display
# $.context.location.state.name
# $.message.descriptor.media[*].url
# $.context.location.circle.radius.type
# $.context.location.descriptor.short_desc
# $.context.location.circle.radius.range.min
# $.message.tags[*].list[*].descriptor.long_desc
# $.context.location.descriptor.additional_desc.url