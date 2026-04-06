---
action: on_update
codeName: L1validations
numTests: 30
generated: 2026-03-18
domain: ONDC:FIS12
version: 2.0.2
---

# L1validations — `on_update` Validations

These are the validation rules applied when processing the `on_update` API call in the L1validations flow.
There are **30** validation rules organized into **5** top-level group(s).

---
## ON_UPDATE_CONTEXT

This group contains **3** sub-group(s)/validation(s): CONTEXT_REQUIRED, CONTEXT_ENUM, and CONTEXT_REGEX.

---

### CONTEXT_REQUIRED

This is a group of **12** sub-validation(s) that all must pass: REQUIRED_CONTEXT_LOCATION_COUNTRY_CODE, REQUIRED_CONTEXT_LOCATION_CITY_CODE, REQUIRED_CONTEXT_DOMAIN, REQUIRED_CONTEXT_TIMESTAMP, REQUIRED_CONTEXT_BAP_ID, REQUIRED_CONTEXT_BAP_URI, REQUIRED_CONTEXT_BPP_ID, REQUIRED_CONTEXT_BPP_URI, REQUIRED_CONTEXT_TRANSACTION_ID, REQUIRED_CONTEXT_MESSAGE_ID, REQUIRED_CONTEXT_VERSION, and REQUIRED_CONTEXT_TTL.

---

**REQUIRED_CONTEXT_LOCATION_COUNTRY_CODE**
`group: ON_UPDATE_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.location.country.code must be present in the payload

**REQUIRED_CONTEXT_LOCATION_CITY_CODE**
`group: ON_UPDATE_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.location.city.code must be present in the payload

**REQUIRED_CONTEXT_DOMAIN**
`group: ON_UPDATE_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.domain must be present in the payload

**REQUIRED_CONTEXT_TIMESTAMP**
`group: ON_UPDATE_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.timestamp must be present in the payload

**REQUIRED_CONTEXT_BAP_ID**
`group: ON_UPDATE_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.bap_id must be present in the payload

**REQUIRED_CONTEXT_BAP_URI**
`group: ON_UPDATE_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.bap_uri must be present in the payload

**REQUIRED_CONTEXT_BPP_ID**
`group: ON_UPDATE_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.bpp_id must be present in the payload

> **Skip if:**
>
>     - all elements of ["on_update"] are in ["search"]

**REQUIRED_CONTEXT_BPP_URI**
`group: ON_UPDATE_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.bpp_uri must be present in the payload

> **Skip if:**
>
>     - all elements of ["on_update"] are in ["search"]

**REQUIRED_CONTEXT_TRANSACTION_ID**
`group: ON_UPDATE_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.transaction_id must be present in the payload

**REQUIRED_CONTEXT_MESSAGE_ID**
`group: ON_UPDATE_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.message_id must be present in the payload

**REQUIRED_CONTEXT_VERSION**
`group: ON_UPDATE_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.version must be present in the payload

**REQUIRED_CONTEXT_TTL**
`group: ON_UPDATE_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.ttl must be present in the payload

### CONTEXT_ENUM

This is a group of **2** sub-validation(s) that all must pass: VALID_CONTEXT_LOCATION_COUNTRY_CODE and VALID_CONTEXT_DOMAIN.

---

**VALID_CONTEXT_LOCATION_COUNTRY_CODE**
`group: ON_UPDATE_CONTEXT > CONTEXT_ENUM | type: leaf`

- At least one of $.context.location.country.code must be in ["IND"]

> **Skip if:**
>
>     - $.context.location.country.code is not in the payload

**VALID_CONTEXT_DOMAIN**
`group: ON_UPDATE_CONTEXT > CONTEXT_ENUM | type: leaf`

- All elements of $.context.domain must be in ["ONDC:FIS12"]

> **Skip if:**
>
>     - $.context.domain is not in the payload

### CONTEXT_REGEX

This is a group of **5** sub-validation(s) that all must pass: REGEX_CONTEXT_LOCATION_CITY_CODE, REGEX_CONTEXT_TIMESTAMP, REGEX_CONTEXT_BAP_ID, REGEX_CONTEXT_BAP_URI, and REGEX_CONTEXT_TTL.

---

**REGEX_CONTEXT_LOCATION_CITY_CODE**
`group: ON_UPDATE_CONTEXT > CONTEXT_REGEX | type: leaf`

- All elements of $.context.location.city.code must follow every regex in ["^\*$"]

> **Skip if:**
>
>     - $.context.location.city.code is not in the payload

**REGEX_CONTEXT_TIMESTAMP**
`group: ON_UPDATE_CONTEXT > CONTEXT_REGEX | type: leaf`

- All elements of $.context.timestamp must follow every regex in ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[+-]\\d{2}:\\d{2})$"]

> **Skip if:**
>
>     - $.context.timestamp is not in the payload

**REGEX_CONTEXT_BAP_ID**
`group: ON_UPDATE_CONTEXT > CONTEXT_REGEX | type: leaf`

- All elements of $.context.bap_id must follow every regex in ["^(?!.*\b(?:http|https|www)\b)[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)+$"]

> **Skip if:**
>
>     - $.context.bap_id is not in the payload

**REGEX_CONTEXT_BAP_URI**
`group: ON_UPDATE_CONTEXT > CONTEXT_REGEX | type: leaf`

- All elements of $.context.bap_uri must follow every regex in ["^https?://([a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*|localhost)(:\d+)?(/.*)?$"]

> **Skip if:**
>
>     - $.context.bap_uri is not in the payload

**REGEX_CONTEXT_TTL**
`group: ON_UPDATE_CONTEXT > CONTEXT_REGEX | type: leaf`

- All elements of $.context.ttl must follow every regex in ["^P(?=\\d|T\\d)(\\d+Y)?(\\d+M)?(\\d+D)?(T(\\d+H)?(\\d+M)?(\\d+S)?)?$"]

> **Skip if:**
>
>     - $.context.ttl is not in the payload

---

## ON_UPDATE_ORDER

This is a group of **3** sub-validation(s) that all must pass: REQUIRED_ORDER_ID, REQUIRED_ORDER_PROVIDER_ID, and REQUIRED_ORDER_ITEMS.

---

**REQUIRED_ORDER_ID**
`group: ON_UPDATE_ORDER | type: leaf`

- $.message.order.id must be present in the payload

**REQUIRED_ORDER_PROVIDER_ID**
`group: ON_UPDATE_ORDER | type: leaf`

- $.message.order.provider.id must be present in the payload

**REQUIRED_ORDER_ITEMS**
`group: ON_UPDATE_ORDER | type: leaf`

- $.message.order.items[*].id must be present in the payload

---

## ON_UPDATE_FULFILLMENTS

This is a group of **2** sub-validation(s) that all must pass: REQUIRED_FULFILLMENT_TYPE and REQUIRED_FULFILLMENT_STATE_CODE.

---

**REQUIRED_FULFILLMENT_TYPE**
`group: ON_UPDATE_FULFILLMENTS | type: leaf`

- All elements of $.message.order.fulfillments[*].type must be in ["LOAN"]

> **Skip if:**
>
>     - $.message.order.fulfillments[*].type is not in the payload

**REQUIRED_FULFILLMENT_STATE_CODE**
`group: ON_UPDATE_FULFILLMENTS | type: leaf`

- All elements of $.message.order.fulfillments[*].state.descriptor.code must be in ["INITIATED", "SANCTIONED", "DISBURSED", "PENDING", "REJECTED", "COMPLETED", "CONSENT_REQUIRED", "APPROVED"]

---

## ON_UPDATE_PAYMENTS

This is a group of **3** sub-validation(s) that all must pass: REQUIRED_PAYMENT_TYPE, REQUIRED_PAYMENT_STATUS, and VALID_PAYMENT_STATUS_ENUM.

---

**REQUIRED_PAYMENT_TYPE**
`group: ON_UPDATE_PAYMENTS | type: leaf`

- $.message.order.payments[*].type must be present in the payload

**REQUIRED_PAYMENT_STATUS**
`group: ON_UPDATE_PAYMENTS | type: leaf`

- $.message.order.payments[*].status must be present in the payload

**VALID_PAYMENT_STATUS_ENUM**
`group: ON_UPDATE_PAYMENTS | type: leaf`

- All elements of $.message.order.payments[*].status must be in ["PAID", "NOT-PAID", "FAILED", "DELAYED", "DEFERRED"]

---

## ON_UPDATE_QUOTE

This is a group of **3** sub-validation(s) that all must pass: REQUIRED_QUOTE_BREAKUP_TITLE, VALID_QUOTE_BREAKUP_TITLE_ON_UPDATE_ENUM, and REQUIRED_QUOTE_BREAKUP_PRICE.

---

**REQUIRED_QUOTE_BREAKUP_TITLE**
`group: ON_UPDATE_QUOTE | type: leaf`

- $.message.order.quote.breakup[*].title must be present in the payload

**VALID_QUOTE_BREAKUP_TITLE_ON_UPDATE_ENUM**
`group: ON_UPDATE_QUOTE | type: leaf`

- At least one of $.message.order.quote.breakup[*].title must be in ["PRINCIPAL", "INTEREST", "PROCESSING_FEE", "OTHER_UPFRONT_CHARGES", "INSURANCE_CHARGES", "NET_DISBURSED_AMOUNT", "OTHER_CHARGES", "LATE_FEE_AMOUNT", "OUTSTANDING_PRINCIPAL", "FORCLOSUER_CHARGES", "OUTSTANDING_INTEREST", "PRE_PAYMENT_CHARGE", "INSURANCE_TOTAL_FEE", "INSURANCE_PRODUCT_FEE", "TAX"]

**REQUIRED_QUOTE_BREAKUP_PRICE**
`group: ON_UPDATE_QUOTE | type: leaf`

- $.message.order.quote.breakup[*].price.value must be present in the payload
