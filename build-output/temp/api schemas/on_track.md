# ═══════════════════════════════════════════════════════════
# ONDC Beckn API — "on_track" action — valid field paths
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
# TOTAL UNIQUE PATHS: 92

# ── Reusable Type Definitions ──────────────────────────────

## Location
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
circle: $ref:Circle
polygon: string
3dspace: string
rating: string

## Descriptor
name: string
code: string
short_desc: string
long_desc: string
additional_desc: $ref:Additional_desc
media[*]: $ref:Media
images[*]: $ref:Images

## Circle
gps: string
radius: $ref:Radius

## Radius
type: string
value: string
estimated_value: string
computed_value: string
range: $ref:Range
unit: string

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

## Range
min: string
max: string

# ── Main Schema ────────────────────────────────────────────

context:
  domain: string
  location: $ref:Location
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
  tracking:
    id: string
    url: string
    location: $ref:Location
    status: string
error:
  code: string
  paths: string
  message: string

# ── Example Full Path Expansions ───────────────────────────
# $.error.code
# $.context.version
# $.context.transaction_id
# $.context.location.city.code
# $.context.location.descriptor.name
# $.context.location.circle.radius.unit
# $.context.location.descriptor.short_desc
# $.message.tracking.location.descriptor.code
# $.context.location.circle.radius.estimated_value
# $.message.tracking.location.descriptor.images[*].url