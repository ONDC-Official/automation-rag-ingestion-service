---
action: confirm
codeName: L1validations
numTests: 36
generated: 2026-04-14
domain: ONDC:FIS12
version: 2.3.0
---

# L1validations — `confirm` Validations

These are the validation rules applied when processing the `confirm` API call in the L1validations flow.
There are **36** validation rules organized into **6** top-level group(s).

---
## CONFIRM_CONTEXT

This group contains **3** sub-group(s)/validation(s): CONTEXT_REQUIRED, CONTEXT_ENUM, and CONTEXT_REGEX.

---

### CONTEXT_REQUIRED

This is a group of **12** sub-validation(s) that all must pass: REQUIRED_CONTEXT_LOCATION_COUNTRY_CODE, REQUIRED_CONTEXT_LOCATION_CITY_CODE, REQUIRED_CONTEXT_DOMAIN, REQUIRED_CONTEXT_TIMESTAMP, REQUIRED_CONTEXT_BAP_ID, REQUIRED_CONTEXT_BAP_URI, REQUIRED_CONTEXT_TRANSACTION_ID, REQUIRED_CONTEXT_MESSAGE_ID, REQUIRED_CONTEXT_VERSION, REQUIRED_CONTEXT_TTL, REQUIRED_CONTEXT_BPP_ID, and REQUIRED_CONTEXT_BPP_URI.

---

**REQUIRED_CONTEXT_LOCATION_COUNTRY_CODE**
`group: CONFIRM_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.location.country.code must be present in the payload

**REQUIRED_CONTEXT_LOCATION_CITY_CODE**
`group: CONFIRM_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.location.city.code must be present in the payload

**REQUIRED_CONTEXT_DOMAIN**
`group: CONFIRM_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.domain must be present in the payload

**REQUIRED_CONTEXT_TIMESTAMP**
`group: CONFIRM_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.timestamp must be present in the payload

**REQUIRED_CONTEXT_BAP_ID**
`group: CONFIRM_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.bap_id must be present in the payload

**REQUIRED_CONTEXT_BAP_URI**
`group: CONFIRM_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.bap_uri must be present in the payload

**REQUIRED_CONTEXT_TRANSACTION_ID**
`group: CONFIRM_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.transaction_id must be present in the payload

**REQUIRED_CONTEXT_MESSAGE_ID**
`group: CONFIRM_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.message_id must be present in the payload

**REQUIRED_CONTEXT_VERSION**
`group: CONFIRM_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.version must be present in the payload

**REQUIRED_CONTEXT_TTL**
`group: CONFIRM_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.ttl must be present in the payload

**REQUIRED_CONTEXT_BPP_ID**
`group: CONFIRM_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.bpp_id must be present in the payload

**REQUIRED_CONTEXT_BPP_URI**
`group: CONFIRM_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.bpp_uri must be present in the payload

### CONTEXT_ENUM

This is a group of **2** sub-validation(s) that all must pass: VALID_CONTEXT_LOCATION_COUNTRY_CODE and VALID_CONTEXT_DOMAIN.

---

**VALID_CONTEXT_LOCATION_COUNTRY_CODE**
`group: CONFIRM_CONTEXT > CONTEXT_ENUM | type: leaf`

- All elements of $.context.location.country.code must be in ["IND"]

> **Skip if:**
>
>     - $.context.location.country.code is not in the payload

**VALID_CONTEXT_DOMAIN**
`group: CONFIRM_CONTEXT > CONTEXT_ENUM | type: leaf`

- All elements of $.context.domain must be in ["ONDC:FIS12"]

> **Skip if:**
>
>     - $.context.domain is not in the payload

### CONTEXT_REGEX

This is a group of **7** sub-validation(s) that all must pass: REGEX_CONTEXT_LOCATION_CITY_CODE, REGEX_CONTEXT_TIMESTAMP_1, REGEX_CONTEXT_BAP_ID, REGEX_CONTEXT_BAP_URI, REQUIRED_CONTEXT_TTL, REGEX_CONTEXT_BPP_ID, and REGEX_CONTEXT_BPP_URI.

---

**REGEX_CONTEXT_LOCATION_CITY_CODE**
`group: CONFIRM_CONTEXT > CONTEXT_REGEX | type: leaf`

- All elements of $.context.location.city.code must follow every regex in ["(\\*)|(^std\\:[0-9]{2,4}$)"]

> **Skip if:**
>
>     - $.context.location.city.code is not in the payload

**REGEX_CONTEXT_TIMESTAMP_1**
`group: CONFIRM_CONTEXT > CONTEXT_REGEX | type: leaf`

- All elements of $.context.timestamp must follow every regex in ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[+-]\\d{2}:\\d{2})$"]

> **Skip if:**
>
>     - $.context.timestamp is not in the payload

**REGEX_CONTEXT_BAP_ID**
`group: CONFIRM_CONTEXT > CONTEXT_REGEX | type: leaf`

- All elements of $.context.bap_id must follow every regex in ["^(?!.*\b(?:http|https|www)\b)[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)+$"]

> **Skip if:**
>
>     - $.context.bap_id is not in the payload

**REGEX_CONTEXT_BAP_URI**
`group: CONFIRM_CONTEXT > CONTEXT_REGEX | type: leaf`

- All elements of $.context.bap_uri must follow every regex in ["^https:\/\/(www\.)?[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)+(/)?$"]

> **Skip if:**
>
>     - $.context.bap_uri is not in the payload

**REQUIRED_CONTEXT_TTL**
`group: CONFIRM_CONTEXT > CONTEXT_REGEX | type: leaf`

- All elements of $.context.ttl must follow every regex in ["^P(?=\\d|T\\d)(\\d+Y)?(\\d+M)?(\\d+D)?(T(\\d+H)?(\\d+M)?(\\d+S)?)?$"]

> **Skip if:**
>
>     - $.context.ttl is not in the payload

**REGEX_CONTEXT_BPP_ID**
`group: CONFIRM_CONTEXT > CONTEXT_REGEX | type: leaf`

- All elements of $.context.bpp_id must follow every regex in ["^(?!.*\b(?:http|https|www)\b)[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)+$"]

> **Skip if:**
>
>     - $.context.bpp_id is not in the payload

**REGEX_CONTEXT_BPP_URI**
`group: CONFIRM_CONTEXT > CONTEXT_REGEX | type: leaf`

- All elements of $.context.bpp_uri must follow every regex in ["^https:\/\/(www\.)?[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)+(/)?$"]

> **Skip if:**
>
>     - $.context.bpp_uri is not in the payload

---

## REQUIRED_PROVIDER_ID

`group: top-level | type: leaf`

- $.message.order.provider.id must be present in the payload

---

## REQUIRED_ITEM_FIELDS

This is a group of **2** sub-validation(s) that all must pass: REQUIRED_ITEM_ID and REQUIRED_PARENT_ITEM_ID.

---

**REQUIRED_ITEM_ID**
`group: REQUIRED_ITEM_FIELDS | type: leaf`

- $.message.order.items[*].id must be present in the payload

**REQUIRED_PARENT_ITEM_ID**
`group: REQUIRED_ITEM_FIELDS | type: leaf`

- $.message.order.items[*].parent_item_id must be present in the payload

---

## CONFIRM_PAYMENTS

This group contains **1** sub-group(s)/validation(s): REQUIRED_PAYMENT_ITEMS.

> **Skip if:**
> - $.message.order.ref_order_ids[*] must be present in the payload

---

### REQUIRED_PAYMENT_ITEMS

This group contains **7** sub-group(s)/validation(s): REQUIRED_PAYMENT_ITEMS, REQUIRED_PAYMENT_ID, REQUIRED_PAYMENT_STATUS, REQUIRED_PAYMENT_COLLECTED_BY, REQUIRED_PAYMENT_BANK_ACCOUNT_NUMBER, REQUIRED_PAYMENT_BANK_CODE, and REQUIRED_PAYMENT_LABEL.

---

**REQUIRED_PAYMENT_ITEMS**
`group: CONFIRM_PAYMENTS > REQUIRED_PAYMENT_ITEMS | type: leaf`

- $.message.order.payments[*].type must be present in the payload

**REQUIRED_PAYMENT_ID**
`group: CONFIRM_PAYMENTS > REQUIRED_PAYMENT_ITEMS | type: leaf`

- $.message.order.payments[*].id must be present in the payload

**REQUIRED_PAYMENT_STATUS**
`group: CONFIRM_PAYMENTS > REQUIRED_PAYMENT_ITEMS | type: leaf`

- $.message.order.payments[*].status must be present in the payload

**REQUIRED_PAYMENT_COLLECTED_BY**
`group: CONFIRM_PAYMENTS > REQUIRED_PAYMENT_ITEMS | type: leaf`

- $.message.order.payments[*].collected_by must be present in the payload

> **Skip if:**
>
>     - not all elements of $.message.order.payments[*].time.label are in ["LOAN_DISBURSMENT"]

#### REQUIRED_PAYMENT_BANK_ACCOUNT_NUMBER

This is a group of **1** sub-validation(s) that all must pass: REQUIRED_PAYMENT_BANK_ACCOUNT_NUMBER. It validates the `$.message.order.payments[*][?(@.time.label=='LOAN_DISBURSMENT')]` path in the payload.

---

**REQUIRED_PAYMENT_BANK_ACCOUNT_NUMBER**
`group: CONFIRM_PAYMENTS > REQUIRED_PAYMENT_ITEMS > REQUIRED_PAYMENT_BANK_ACCOUNT_NUMBER | type: leaf`

- $.message.order.payments[*].params.bank_account_number must be present in the payload

#### REQUIRED_PAYMENT_BANK_CODE

This is a group of **1** sub-validation(s) that all must pass: REQUIRED_PAYMENT_BANK_CODE. It validates the `$.message.order.payments[*][?(@.time.label=='LOAN_DISBURSMENT')]` path in the payload.

---

**REQUIRED_PAYMENT_BANK_CODE**
`group: CONFIRM_PAYMENTS > REQUIRED_PAYMENT_ITEMS > REQUIRED_PAYMENT_BANK_CODE | type: leaf`

- $.message.order.payments[*].params.bank_code must be present in the payload

**REQUIRED_PAYMENT_LABEL**
`group: CONFIRM_PAYMENTS > REQUIRED_PAYMENT_ITEMS | type: leaf`

- $.message.order.payments[*].time.label must be present in the payload

---

## CONFIRM_PAYMENT_TAGS

This is a group of **2** sub-validation(s) that all must pass: VALID_PAYMENT_TAGS and REQUIRED_ACCOUNT_DETAILS.

---

**VALID_PAYMENT_TAGS**
`group: CONFIRM_PAYMENT_TAGS | type: leaf`

- All elements of $.message.order.payments[*].tags[*].descriptor.code must be in ["ACCOUNT_DETAILS", "BREAKUP"]

> **Skip if:**
>
>     - $.message.order.payments[*].tags[*].descriptor.code is not in the payload

**REQUIRED_ACCOUNT_DETAILS**
`group: CONFIRM_PAYMENT_TAGS | type: leaf | scope: $.message.order.payments[*].tags[?(@.descriptor.code == 'ACCOUNT_DETAILS')]`

- All elements of $.message.order.payments[*].tags[?(@.descriptor.code == 'ACCOUNT_DETAILS')].list[*].descriptor.code must be in ["ACCOUNT_TYPE", "ACCOUNT_HOLDER_NAME", "BANK_NAME"]

---

## CONFIRM_TAGS

This is a group of **3** sub-validation(s) that all must pass: REQUIRED_PAYMENT_TAGS, REQUIRED_BAP_TERMS, and REQUIRED_BPP_TERMS.

---

**REQUIRED_PAYMENT_TAGS**
`group: CONFIRM_TAGS | type: leaf`

- All elements of $.message.order.tags[*].descriptor.code must be in ["BAP_TERMS", "BPP_TERMS"]

> **Skip if:**
>
>     - $.message.order.tags[*].descriptor.code is not in the payload

**REQUIRED_BAP_TERMS**
`group: CONFIRM_TAGS | type: leaf | scope: $.message.order.tags[?(@.descriptor.code == 'BAP_TERMS')]`

- All elements of $.message.order.tags[?(@.descriptor.code == 'BAP_TERMS')].list[*].descriptor.code must be in ["STATIC_TERMS", "OFFLINE_CONTRACT"]

**REQUIRED_BPP_TERMS**
`group: CONFIRM_TAGS | type: leaf | scope: $.message.order.tags[?(@.descriptor.code == 'BPP_TERMS')]`

- All elements of $.message.order.tags[?(@.descriptor.code == 'BPP_TERMS')].list[*].descriptor.code must be in ["STATIC_TERMS", "OFFLINE_CONTRACT"]
