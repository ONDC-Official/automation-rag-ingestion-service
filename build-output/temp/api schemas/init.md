# ═══════════════════════════════════════════════════════════
# ONDC Beckn API — "init" action — valid field paths
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
# TOTAL UNIQUE PATHS: 2974

# ── Reusable Type Definitions ──────────────────────────────

## Items
id: string
parent_item_id: string
parent_item_quantity: $ref:Quantity
descriptor: $ref:Descriptor
creator: $ref:Organization
price: $ref:Price
quantity: $ref:Quantity
category_ids[*]: string
fulfillment_ids[*]: string
location_ids[*]: string
payment_ids[*]: string
add_ons[*]: $ref:Add_ons
cancellation_terms[*]: $ref:Cancellation_terms
refund_terms[*]: $ref:Refund_terms
replacement_terms[*]: $ref:Replacement_terms
return_terms[*]: $ref:Return_terms
xinput: $ref:Xinput
time: $ref:Time
rateable: string
rating: string
matched: string
related: string
recommended: string
ttl: string
tags[*]: $ref:Tags

## Fulfillments
id: string
type: string
rateable: string
rating: string
state: $ref:Fulfillment_state
tracking: string
customer: $ref:Customer
agent: $ref:Agent
contact: $ref:Contact
vehicle: $ref:Vehicle
stops[*]: $ref:Stops
path: string
tags[*]: $ref:Tags

## Stops
id: string
parent_stop_id: string
location: $ref:Return_location
type: string
time: $ref:Time
instructions: $ref:Descriptor
contact: $ref:Contact
person: $ref:Person
authorization: $ref:Authorization

## Add_ons
id: string
descriptor: $ref:Descriptor
price: $ref:Price
quantity: $ref:Quantity
tags[*]: $ref:Tags

## Cancellation_terms
fulfillment_state: $ref:Fulfillment_state
reason_required: string
cancel_by: $ref:Time
cancellation_fee: $ref:Cancellation_fee
xinput: $ref:Xinput
external_ref: $ref:Media

## Agent
person: $ref:Person
contact: $ref:Contact
organization: $ref:Organization
rating: string

## Customer
organization: $ref:Organization
person: $ref:Person
contact: $ref:Contact

## Payments
id: string
collected_by: string
url: string
params: $ref:Params
type: string
status: string
time: $ref:Time
tags[*]: $ref:Tags

## Offers
id: string
descriptor: $ref:Descriptor
location_ids[*]: string
category_ids[*]: string
item_ids[*]: string
time: $ref:Time
tags[*]: $ref:Tags

## Return_terms
fulfillment_state: $ref:City
return_eligible: string
return_time: $ref:Time
return_location: $ref:Return_location
fulfillment_managed_by: string

## Quantity
allocated: $ref:Allocated
available: $ref:Allocated
maximum: $ref:Allocated
minimum: $ref:Allocated
selected: $ref:Allocated
unitized: $ref:Allocated

## Person
id: string
url: string
name: string
image: $ref:Images
age: string
dob: string
gender: string
creds[*]: $ref:Creds
languages[*]: $ref:City
skills[*]: $ref:City
tags[*]: $ref:Tags

## Return_location
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

## Tags
display: string
descriptor: $ref:Descriptor
list[*]: $ref:List

## Xinput
head: $ref:Head
form: $ref:Form
form_response: $ref:Form_response
required: string

## Organization
descriptor: $ref:Descriptor
address: string
state: $ref:City
city: $ref:City
contact: $ref:Contact
creds[*]: $ref:Creds

## Refund_terms
fulfillment_state: $ref:City
refund_eligible: string
refund_within: $ref:Time
refund_amount: $ref:Price

## Head
descriptor: $ref:Descriptor
index: $ref:Index
headings[*]: string

## Fulfillment_state
descriptor: $ref:Descriptor
updated_at: string
updated_by: string

## List
descriptor: $ref:Descriptor
value: string
display: string

## Replacement_terms
fulfillment_state: $ref:City
replace_within: $ref:Time
external_ref: $ref:Media

## Params
transaction_id: string
amount: string
currency: string
bank_code: string
bank_account_number: string
virtual_payment_address: string
source_bank_code: string
source_bank_account_number: string
source_virtual_payment_address: string
source_bank_account_name: string
bank_account_name: string

## Descriptor
name: string
code: string
short_desc: string
long_desc: string
additional_desc: $ref:Additional_desc
media[*]: $ref:Media
images[*]: $ref:Images

## Vehicle
category: string
capacity: string
make: string
model: string
size: string
variant: string
color: string
energy_type: string
registration: string
wheels_count: string
cargo_volumne: string
wheelchair_access: string
code: string
emission_standard: string

## Cancellation_fee
percentage: string
amount: $ref:Price

## Price
currency: string
value: string
estimated_value: string
computed_value: string
listed_value: string
offered_value: string
minimum_value: string
maximum_value: string

## Time
label: string
timestamp: string
duration: string
range: $ref:Range
days: string
schedule: $ref:Schedule

## Allocated
count: string
measure: $ref:Measure

## Circle
gps: string
radius: $ref:Measure

## Measure
type: string
value: string
estimated_value: string
computed_value: string
range: $ref:RadiusRange
unit: string

## Form_response
status: string
signature: string
submission_id: string
errors[*]: $ref:Errors

## Form
id: string
url: string
mime_type: string
resubmit: string
multiple_sumbissions: string

## Authorization
type: string
token: string
valid_from: string
valid_to: string
status: string

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

## Schedule
frequency: string
holidays[*]: string
times[*]: string

## Errors
code: string
paths: string
message: string

## Creds
id: string
type: string
url: string

## Index
min: string
cur: string
max: string

## Additional_desc
url: string
content_type: string

## Contact
phone: string
email: string

## City
name: string
code: string

## Range
start: string
end: string

## RadiusRange
min: string
max: string

# ── Main Schema ────────────────────────────────────────────

context:
  domain: string
  location: $ref:Return_location
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
  order:
    id: string
    ref_order_ids[*]: string
    status: string
    type: string
    provider:
      id: string
      descriptor: $ref:Descriptor
      category_id: string
      rating: string
      time: $ref:Time
      categories[*]:
        id: string
        parent_category_id: string
        descriptor: $ref:Descriptor
        time: $ref:Time
        tags[*]: $ref:Tags
      fulfillments[*]: $ref:Fulfillments
      payments[*]: $ref:Payments
      locations[*]: $ref:Return_location
      offers[*]: $ref:Offers
      items[*]: $ref:Items
      exp: string
      rateable: string
      ttl: string
      tags[*]: $ref:Tags
    items[*]: $ref:Items
    add_ons[*]: $ref:Add_ons
    offers[*]: $ref:Offers
    billing:
      name: string
      organization: $ref:Organization
      address: string
      state: $ref:City
      city: $ref:City
      email: string
      phone: string
      time: $ref:Time
      tax_id: string
    fulfillments[*]: $ref:Fulfillments
    cancellation:
      time: string
      cancelled_by: string
      reason:
        id: string
        descriptor: $ref:Descriptor
      additional_description: $ref:Descriptor
    cancellation_terms[*]: $ref:Cancellation_terms
    documents[*]:
      descriptor: $ref:Descriptor
      mime_type: string
      url: string
      old_policy_doc: string
    refund_terms[*]: $ref:Refund_terms
    replacement_terms[*]: $ref:Replacement_terms
    return_terms[*]: $ref:Return_terms
    quote:
      id: string
      price: $ref:Price
      breakup[*]:
        item: $ref:Items
        title: string
        price: $ref:Price
      ttl: string
    payments[*]: $ref:Payments
    created_at: string
    updated_at: string
    xinput: $ref:Xinput
    tags[*]: $ref:Tags

# ── Example Full Path Expansions ───────────────────────────
# $.context.key
# $.message.order.tags[*].descriptor.media[*].dsa
# $.message.order.xinput.form_response.errors[*].message
# $.message.order.quote.breakup[*].item.tags[*].list[*].value
# $.message.order.items[*].quantity.maximum.measure.computed_value
# $.message.order.provider.items[*].xinput.form_response.submission_id
# $.message.order.items[*].parent_item_quantity.selected.measure.range.min
# $.message.order.fulfillments[*].agent.person.tags[*].descriptor.media[*].dsa
# $.message.order.provider.fulfillments[*].agent.organization.descriptor.short_desc
# $.message.order.provider.fulfillments[*].agent.person.tags[*].descriptor.images[*].width