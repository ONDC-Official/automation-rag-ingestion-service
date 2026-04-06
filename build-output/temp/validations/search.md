---
action: search
codeName: L1validations
numTests: 28
generated: 2026-03-18
domain: ONDC:FIS12
version: 2.0.2
---

# L1validations — `search` Validations

These are the validation rules applied when processing the `search` API call in the L1validations flow.
There are **28** validation rules organized into **3** top-level group(s).

---
## SEARCH_CONTEXT

This group contains **3** sub-group(s)/validation(s): CONTEXT_REQUIRED, CONTEXT_ENUM, and CONTEXT_REGEX.

---

### CONTEXT_REQUIRED

This is a group of **12** sub-validation(s) that all must pass: REQUIRED_CONTEXT_LOCATION_COUNTRY_CODE, REQUIRED_CONTEXT_LOCATION_CITY_CODE, REQUIRED_CONTEXT_DOMAIN, REQUIRED_CONTEXT_TIMESTAMP, REQUIRED_CONTEXT_BAP_ID, REQUIRED_CONTEXT_BAP_URI, REQUIRED_CONTEXT_BPP_ID, REQUIRED_CONTEXT_BPP_URI, REQUIRED_CONTEXT_TRANSACTION_ID, REQUIRED_CONTEXT_MESSAGE_ID, REQUIRED_CONTEXT_VERSION, and REQUIRED_CONTEXT_TTL.

---

**REQUIRED_CONTEXT_LOCATION_COUNTRY_CODE**
`group: SEARCH_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.location.country.code must be present in the payload

**REQUIRED_CONTEXT_LOCATION_CITY_CODE**
`group: SEARCH_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.location.city.code must be present in the payload

**REQUIRED_CONTEXT_DOMAIN**
`group: SEARCH_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.domain must be present in the payload

**REQUIRED_CONTEXT_TIMESTAMP**
`group: SEARCH_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.timestamp must be present in the payload

**REQUIRED_CONTEXT_BAP_ID**
`group: SEARCH_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.bap_id must be present in the payload

**REQUIRED_CONTEXT_BAP_URI**
`group: SEARCH_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.bap_uri must be present in the payload

**REQUIRED_CONTEXT_BPP_ID**
`group: SEARCH_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.bpp_id must be present in the payload

> **Skip if:**
>
>     - all elements of ["search"] are in ["search"]

**REQUIRED_CONTEXT_BPP_URI**
`group: SEARCH_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.bpp_uri must be present in the payload

> **Skip if:**
>
>     - all elements of ["search"] are in ["search"]

**REQUIRED_CONTEXT_TRANSACTION_ID**
`group: SEARCH_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.transaction_id must be present in the payload

**REQUIRED_CONTEXT_MESSAGE_ID**
`group: SEARCH_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.message_id must be present in the payload

**REQUIRED_CONTEXT_VERSION**
`group: SEARCH_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.version must be present in the payload

**REQUIRED_CONTEXT_TTL**
`group: SEARCH_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.ttl must be present in the payload

### CONTEXT_ENUM

This is a group of **2** sub-validation(s) that all must pass: VALID_CONTEXT_LOCATION_COUNTRY_CODE and VALID_CONTEXT_DOMAIN.

---

**VALID_CONTEXT_LOCATION_COUNTRY_CODE**
`group: SEARCH_CONTEXT > CONTEXT_ENUM | type: leaf`

- At least one of $.context.location.country.code must be in ["IND"]

> **Skip if:**
>
>     - $.context.location.country.code is not in the payload

**VALID_CONTEXT_DOMAIN**
`group: SEARCH_CONTEXT > CONTEXT_ENUM | type: leaf`

- All elements of $.context.domain must be in ["ONDC:FIS12"]

> **Skip if:**
>
>     - $.context.domain is not in the payload

### CONTEXT_REGEX

This is a group of **5** sub-validation(s) that all must pass: REGEX_CONTEXT_LOCATION_CITY_CODE, REGEX_CONTEXT_TIMESTAMP, REGEX_CONTEXT_BAP_ID, REGEX_CONTEXT_BAP_URI, and REGEX_CONTEXT_TTL.

---

**REGEX_CONTEXT_LOCATION_CITY_CODE**
`group: SEARCH_CONTEXT > CONTEXT_REGEX | type: leaf`

- All elements of $.context.location.city.code must follow every regex in ["^\*$"]

> **Skip if:**
>
>     - $.context.location.city.code is not in the payload

**REGEX_CONTEXT_TIMESTAMP**
`group: SEARCH_CONTEXT > CONTEXT_REGEX | type: leaf`

- All elements of $.context.timestamp must follow every regex in ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[+-]\\d{2}:\\d{2})$"]

> **Skip if:**
>
>     - $.context.timestamp is not in the payload

**REGEX_CONTEXT_BAP_ID**
`group: SEARCH_CONTEXT > CONTEXT_REGEX | type: leaf`

- All elements of $.context.bap_id must follow every regex in ["^(?!.*\b(?:http|https|www)\b)[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)+$"]

> **Skip if:**
>
>     - $.context.bap_id is not in the payload

**REGEX_CONTEXT_BAP_URI**
`group: SEARCH_CONTEXT > CONTEXT_REGEX | type: leaf`

- All elements of $.context.bap_uri must follow every regex in ["^https?://([a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*|localhost)(:\d+)?(/.*)?$"]

> **Skip if:**
>
>     - $.context.bap_uri is not in the payload

**REGEX_CONTEXT_TTL**
`group: SEARCH_CONTEXT > CONTEXT_REGEX | type: leaf`

- All elements of $.context.ttl must follow every regex in ["^P(?=\\d|T\\d)(\\d+Y)?(\\d+M)?(\\d+D)?(T(\\d+H)?(\\d+M)?(\\d+S)?)?$"]

> **Skip if:**
>
>     - $.context.ttl is not in the payload

---

## SEARCH_CATEGORY_CODE

This is a group of **2** sub-validation(s) that all must pass: REQUIRED_CATEGORY_CODE and VALID_ENUM_CATEGORY_CODE.

---

**REQUIRED_CATEGORY_CODE**
`group: SEARCH_CATEGORY_CODE | type: leaf`

- $.message.intent.category.descriptor.code must be present in the payload

**VALID_ENUM_CATEGORY_CODE**
`group: SEARCH_CATEGORY_CODE | type: leaf`

- All elements of $.message.intent.category.descriptor.code must be in ["GOLD_LOAN", "PERSONAL_LOAN"]

> **Skip if:**
>
>     - $.message.intent.category.descriptor.code is not in the payload

---

## SEARCH_PAYMENT

This group contains **3** sub-group(s)/validation(s): REQUIRED_PAYMENT_COLLECTED_BY, VALID_PAYMENT_COLLECTED_BY_ENUM, and REQUIRED_PAYMENT_TAGS_GROUPS.

---

**REQUIRED_PAYMENT_COLLECTED_BY**
`group: SEARCH_PAYMENT | type: leaf`

- $.message.intent.payment.collected_by must be present in the payload

**VALID_PAYMENT_COLLECTED_BY_ENUM**
`group: SEARCH_PAYMENT | type: leaf`

- At least one of $.message.intent.payment.collected_by must be in ["BPP", "BAP"]

> **Skip if:**
>
>     - $.message.intent.payment.collected_by is not in the payload

### REQUIRED_PAYMENT_TAGS_GROUPS

This is a group of **5** sub-validation(s) that all must pass: REQUIRED_BUYER_FINDER_FEES_TAG, REQUIRED_BUYER_FINDER_FEES_LIST, VALID_BUYER_FINDER_FEES_TYPE_VALUE, REQUIRED_SETTLEMENT_TERMS_TAG, and REQUIRED_SETTLEMENT_TERMS_LIST.

---

**REQUIRED_BUYER_FINDER_FEES_TAG**
`group: SEARCH_PAYMENT > REQUIRED_PAYMENT_TAGS_GROUPS | type: leaf`

- At least one of $.message.intent.payment.tags[*].descriptor.code must be in ["BUYER_FINDER_FEES"]

**REQUIRED_BUYER_FINDER_FEES_LIST**
`group: SEARCH_PAYMENT > REQUIRED_PAYMENT_TAGS_GROUPS | type: leaf | scope: $.message.intent.payment.tags[?(@.descriptor.code=='BUYER_FINDER_FEES')]`

- All elements of $.message.intent.payment.tags[?(@.descriptor.code=='BUYER_FINDER_FEES')].list[*].descriptor.code must be in ["BUYER_FINDER_FEES_TYPE", "BUYER_FINDER_FEES_PERCENTAGE"]

> **Skip if:**
>
>     - $.message.intent.payment.tags[?(@.descriptor.code=='BUYER_FINDER_FEES')].list[*].descriptor.code is not in the payload

**VALID_BUYER_FINDER_FEES_TYPE_VALUE**
`group: SEARCH_PAYMENT > REQUIRED_PAYMENT_TAGS_GROUPS | type: leaf | scope: $.message.intent.payment.tags[?(@.descriptor.code=='BUYER_FINDER_FEES')].list[?(@.descriptor.code=='BUYER_FINDER_FEES_TYPE')]`

- All elements of $.message.intent.payment.tags[?(@.descriptor.code=='BUYER_FINDER_FEES')].list[?(@.descriptor.code=='BUYER_FINDER_FEES_TYPE')].value must be in ["percent-annualized", "percent", "amount"]

**REQUIRED_SETTLEMENT_TERMS_TAG**
`group: SEARCH_PAYMENT > REQUIRED_PAYMENT_TAGS_GROUPS | type: leaf`

- At least one of $.message.intent.payment.tags[*].descriptor.code must be in ["SETTLEMENT_TERMS"]

**REQUIRED_SETTLEMENT_TERMS_LIST**
`group: SEARCH_PAYMENT > REQUIRED_PAYMENT_TAGS_GROUPS | type: leaf | scope: $.message.intent.payment.tags[?(@.descriptor.code=='SETTLEMENT_TERMS')]`

- All elements of $.message.intent.payment.tags[?(@.descriptor.code=='SETTLEMENT_TERMS')].list[*].descriptor.code must be in ["DELAY_INTEREST", "STATIC_TERMS", "OFFLINE_CONTRACT"]

> **Skip if:**
>
>     - $.message.intent.payment.tags[?(@.descriptor.code=='SETTLEMENT_TERMS')].list[*].descriptor.code is not in the payload
