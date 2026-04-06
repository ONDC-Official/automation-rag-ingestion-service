---
action: on_confirm
codeName: L1validations
numTests: 42
generated: 2026-03-18
domain: ONDC:FIS12
version: 2.0.2
---

# L1validations — `on_confirm` Validations

These are the validation rules applied when processing the `on_confirm` API call in the L1validations flow.
There are **42** validation rules organized into **9** top-level group(s).

---
## ON_CONFIRM_CONTEXT

This group contains **3** sub-group(s)/validation(s): CONTEXT_REQUIRED, CONTEXT_ENUM, and CONTEXT_REGEX.

---

### CONTEXT_REQUIRED

This is a group of **12** sub-validation(s) that all must pass: REQUIRED_CONTEXT_LOCATION_COUNTRY_CODE, REQUIRED_CONTEXT_LOCATION_CITY_CODE, REQUIRED_CONTEXT_DOMAIN, REQUIRED_CONTEXT_TIMESTAMP, REQUIRED_CONTEXT_BAP_ID, REQUIRED_CONTEXT_BAP_URI, REQUIRED_CONTEXT_BPP_ID, REQUIRED_CONTEXT_BPP_URI, REQUIRED_CONTEXT_TRANSACTION_ID, REQUIRED_CONTEXT_MESSAGE_ID, REQUIRED_CONTEXT_VERSION, and REQUIRED_CONTEXT_TTL.

---

**REQUIRED_CONTEXT_LOCATION_COUNTRY_CODE**
`group: ON_CONFIRM_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.location.country.code must be present in the payload

**REQUIRED_CONTEXT_LOCATION_CITY_CODE**
`group: ON_CONFIRM_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.location.city.code must be present in the payload

**REQUIRED_CONTEXT_DOMAIN**
`group: ON_CONFIRM_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.domain must be present in the payload

**REQUIRED_CONTEXT_TIMESTAMP**
`group: ON_CONFIRM_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.timestamp must be present in the payload

**REQUIRED_CONTEXT_BAP_ID**
`group: ON_CONFIRM_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.bap_id must be present in the payload

**REQUIRED_CONTEXT_BAP_URI**
`group: ON_CONFIRM_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.bap_uri must be present in the payload

**REQUIRED_CONTEXT_BPP_ID**
`group: ON_CONFIRM_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.bpp_id must be present in the payload

> **Skip if:**
>
>     - all elements of ["on_confirm"] are in ["search"]

**REQUIRED_CONTEXT_BPP_URI**
`group: ON_CONFIRM_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.bpp_uri must be present in the payload

> **Skip if:**
>
>     - all elements of ["on_confirm"] are in ["search"]

**REQUIRED_CONTEXT_TRANSACTION_ID**
`group: ON_CONFIRM_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.transaction_id must be present in the payload

**REQUIRED_CONTEXT_MESSAGE_ID**
`group: ON_CONFIRM_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.message_id must be present in the payload

**REQUIRED_CONTEXT_VERSION**
`group: ON_CONFIRM_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.version must be present in the payload

**REQUIRED_CONTEXT_TTL**
`group: ON_CONFIRM_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.ttl must be present in the payload

### CONTEXT_ENUM

This is a group of **2** sub-validation(s) that all must pass: VALID_CONTEXT_LOCATION_COUNTRY_CODE and VALID_CONTEXT_DOMAIN.

---

**VALID_CONTEXT_LOCATION_COUNTRY_CODE**
`group: ON_CONFIRM_CONTEXT > CONTEXT_ENUM | type: leaf`

- At least one of $.context.location.country.code must be in ["IND"]

> **Skip if:**
>
>     - $.context.location.country.code is not in the payload

**VALID_CONTEXT_DOMAIN**
`group: ON_CONFIRM_CONTEXT > CONTEXT_ENUM | type: leaf`

- All elements of $.context.domain must be in ["ONDC:FIS12"]

> **Skip if:**
>
>     - $.context.domain is not in the payload

### CONTEXT_REGEX

This is a group of **5** sub-validation(s) that all must pass: REGEX_CONTEXT_LOCATION_CITY_CODE, REGEX_CONTEXT_TIMESTAMP, REGEX_CONTEXT_BAP_ID, REGEX_CONTEXT_BAP_URI, and REGEX_CONTEXT_TTL.

---

**REGEX_CONTEXT_LOCATION_CITY_CODE**
`group: ON_CONFIRM_CONTEXT > CONTEXT_REGEX | type: leaf`

- All elements of $.context.location.city.code must follow every regex in ["^\*$"]

> **Skip if:**
>
>     - $.context.location.city.code is not in the payload

**REGEX_CONTEXT_TIMESTAMP**
`group: ON_CONFIRM_CONTEXT > CONTEXT_REGEX | type: leaf`

- All elements of $.context.timestamp must follow every regex in ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[+-]\\d{2}:\\d{2})$"]

> **Skip if:**
>
>     - $.context.timestamp is not in the payload

**REGEX_CONTEXT_BAP_ID**
`group: ON_CONFIRM_CONTEXT > CONTEXT_REGEX | type: leaf`

- All elements of $.context.bap_id must follow every regex in ["^(?!.*\b(?:http|https|www)\b)[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)+$"]

> **Skip if:**
>
>     - $.context.bap_id is not in the payload

**REGEX_CONTEXT_BAP_URI**
`group: ON_CONFIRM_CONTEXT > CONTEXT_REGEX | type: leaf`

- All elements of $.context.bap_uri must follow every regex in ["^https?://([a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*|localhost)(:\d+)?(/.*)?$"]

> **Skip if:**
>
>     - $.context.bap_uri is not in the payload

**REGEX_CONTEXT_TTL**
`group: ON_CONFIRM_CONTEXT > CONTEXT_REGEX | type: leaf`

- All elements of $.context.ttl must follow every regex in ["^P(?=\\d|T\\d)(\\d+Y)?(\\d+M)?(\\d+D)?(T(\\d+H)?(\\d+M)?(\\d+S)?)?$"]

> **Skip if:**
>
>     - $.context.ttl is not in the payload

---

## ON_CONFIRM_PROVIDER

This group contains **3** sub-group(s)/validation(s): REQUIRED_PROVIDER_ID, REQUIRED_PROVIDER_NAME, and REQUIRED_PROVIDER_TAGS.

---

**REQUIRED_PROVIDER_ID**
`group: ON_CONFIRM_PROVIDER | type: leaf`

- $.message.order.provider.id must be present in the payload

**REQUIRED_PROVIDER_NAME**
`group: ON_CONFIRM_PROVIDER | type: leaf`

- $.message.order.provider.descriptor.name must be present in the payload

### REQUIRED_PROVIDER_TAGS

This is a group of **2** sub-validation(s) that all must pass: REQUIRED_CONTACT_INFO_TAG_GROUP and REQUIRED_LSP_INFO_TAG_GROUP.

---

**REQUIRED_CONTACT_INFO_TAG_GROUP**
`group: ON_CONFIRM_PROVIDER > REQUIRED_PROVIDER_TAGS | type: leaf`

- At least one of $.message.order.provider.tags[*].descriptor.code must be in ["CONTACT_INFO"]

**REQUIRED_LSP_INFO_TAG_GROUP**
`group: ON_CONFIRM_PROVIDER > REQUIRED_PROVIDER_TAGS | type: leaf`

- At least one of $.message.order.provider.tags[*].descriptor.code must be in ["LSP_INFO"]

---

## ON_CONFIRM_ITEMS

This is a group of **4** sub-validation(s) that all must pass: REQUIRED_ITEM_ID, REQUIRED_ITEM_DESCRIPTOR_CODE, REQUIRED_ITEM_PRICE, and REQUIRED_LOAN_INFO_TAG.

---

**REQUIRED_ITEM_ID**
`group: ON_CONFIRM_ITEMS | type: leaf`

- $.message.order.items[*].id must be present in the payload

**REQUIRED_ITEM_DESCRIPTOR_CODE**
`group: ON_CONFIRM_ITEMS | type: leaf`

- All elements of $.message.order.items[*].descriptor.code must be in ["LOAN", "PERSONAL_LOAN"]

**REQUIRED_ITEM_PRICE**
`group: ON_CONFIRM_ITEMS | type: leaf`

- $.message.order.items[*].price.value must be present in the payload

**REQUIRED_LOAN_INFO_TAG**
`group: ON_CONFIRM_ITEMS | type: leaf`

- At least one of $.message.order.items[*].tags[*].descriptor.code must be in ["LOAN_INFO"]

---

## ON_CONFIRM_QUOTE

This is a group of **3** sub-validation(s) that all must pass: REQUIRED_QUOTE_ID, REQUIRED_QUOTE_PRICE, and REQUIRED_QUOTE_BREAKUP.

---

**REQUIRED_QUOTE_ID**
`group: ON_CONFIRM_QUOTE | type: leaf`

- $.message.order.quote.id must be present in the payload

**REQUIRED_QUOTE_PRICE**
`group: ON_CONFIRM_QUOTE | type: leaf`

- $.message.order.quote.price.value must be present in the payload

**REQUIRED_QUOTE_BREAKUP**
`group: ON_CONFIRM_QUOTE | type: leaf`

- At least one of $.message.order.quote.breakup[*].title must be in ["PRINCIPAL", "INTEREST", "PROCESSING_FEE", "OTHER_UPFRONT_CHARGES", "INSURANCE_CHARGES", "NET_DISBURSED_AMOUNT", "OTHER_CHARGES"]

---

## ON_CONFIRM_FULFILLMENTS

This is a group of **4** sub-validation(s) that all must pass: REQUIRED_FULFILLMENT_TYPE, REQUIRED_FULFILLMENT_STATE_DESCRIPTOR_CODE, VALID_FULFILLMENT_STATE_ENUM, and REQUIRED_FULFILLMENT_CUSTOMER.

---

**REQUIRED_FULFILLMENT_TYPE**
`group: ON_CONFIRM_FULFILLMENTS | type: leaf`

- All elements of $.message.order.fulfillments[*].type must be in ["LOAN"]

> **Skip if:**
>
>     - $.message.order.fulfillments[*].type is not in the payload

**REQUIRED_FULFILLMENT_STATE_DESCRIPTOR_CODE**
`group: ON_CONFIRM_FULFILLMENTS | type: leaf`

- $.message.order.fulfillments[*].state.descriptor.code must be present in the payload

**VALID_FULFILLMENT_STATE_ENUM**
`group: ON_CONFIRM_FULFILLMENTS | type: leaf`

- All elements of $.message.order.fulfillments[*].state.descriptor.code must be in ["DISBURSED", "SANCTIONED"]

**REQUIRED_FULFILLMENT_CUSTOMER**
`group: ON_CONFIRM_FULFILLMENTS | type: leaf`

- $.message.order.fulfillments[*].customer.person.name must be present in the payload

---

## ON_CONFIRM_PAYMENTS

This is a group of **3** sub-validation(s) that all must pass: REQUIRED_PAYMENT_TYPE, REQUIRED_PAYMENT_STATUS, and VALID_PAYMENT_STATUS_ENUM.

---

**REQUIRED_PAYMENT_TYPE**
`group: ON_CONFIRM_PAYMENTS | type: leaf`

- All elements of $.message.order.payments[*].type must be in ["ON_ORDER", "ON_FULFILLMENT", "POST_FULFILLMENT"]

**REQUIRED_PAYMENT_STATUS**
`group: ON_CONFIRM_PAYMENTS | type: leaf`

- $.message.order.payments[*].status must be present in the payload

**VALID_PAYMENT_STATUS_ENUM**
`group: ON_CONFIRM_PAYMENTS | type: leaf`

- All elements of $.message.order.payments[*].status must be in ["PAID", "NOT-PAID"]

---

## ON_CONFIRM_PAYMENTS_COLLECTED_BY

This is a group of **1** sub-validation(s) that all must pass: REQUIRED_PAYMENT_COLLECTED_BY. It validates the `$.message.order.payments[?(@.type=='ON_ORDER')]` path in the payload.

---

**REQUIRED_PAYMENT_COLLECTED_BY**
`group: ON_CONFIRM_PAYMENTS_COLLECTED_BY | type: leaf`

- All elements of $.message.order.payments[?(@.type=='ON_ORDER')].collected_by must be in ["BPP", "BAP"]

---

## ON_CONFIRM_DOCUMENTS

This is a group of **3** sub-validation(s) that all must pass: REQUIRED_DOCUMENT_DESCRIPTOR_CODE, REQUIRED_DOCUMENT_URL, and REQUIRED_DOCUMENT_MIME_TYPE.

---

**REQUIRED_DOCUMENT_DESCRIPTOR_CODE**
`group: ON_CONFIRM_DOCUMENTS | type: leaf`

- $.message.order.documents[*].descriptor.code must be present in the payload

**REQUIRED_DOCUMENT_URL**
`group: ON_CONFIRM_DOCUMENTS | type: leaf`

- $.message.order.documents[*].url must be present in the payload

**REQUIRED_DOCUMENT_MIME_TYPE**
`group: ON_CONFIRM_DOCUMENTS | type: leaf`

- All elements of $.message.order.documents[*].mime_type must be in ["application/pdf", "text/html"]

---

## ON_CONFIRM_CANCELLATION_TERMS

`group: top-level | type: leaf`

- All elements of $.message.order.cancellation_terms[*].fulfillment_state.descriptor.code must be in ["SANCTIONED", "DISBURSED"]
