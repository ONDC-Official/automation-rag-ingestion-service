# ═══════════════════════════════════════════════════════════
# ONDC Beckn API — "on_rating" action — valid field paths
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
# TOTAL UNIQUE PATHS: 82

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

## Errors
code: string
paths: string
message: string

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
  feedback_form:
    head:
      descriptor: $ref:Descriptor
      index:
        min: string
        cur: string
        max: string
      headings[*]: string
    form:
      id: string
      url: string
      mime_type: string
      resubmit: string
      multiple_sumbissions: string
    form_response:
      status: string
      signature: string
      submission_id: string
      errors[*]: $ref:Errors
    required: string
error: $ref:Errors

# ── Example Full Path Expansions ───────────────────────────
# $.error.code
# $.context.bpp_id
# $.context.transaction_id
# $.context.location.city.code
# $.message.feedback_form.form.url
# $.message.feedback_form.head.index.min
# $.context.location.descriptor.media[*].dsa
# $.context.location.descriptor.images[*].height
# $.message.feedback_form.head.descriptor.long_desc
# $.message.feedback_form.form_response.errors[*].paths