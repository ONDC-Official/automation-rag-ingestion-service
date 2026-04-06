---
action: on_search
codeName: L1validations
numTests: 48
generated: 2026-03-18
domain: ONDC:FIS12
version: 2.0.2
---

# L1validations — `on_search` Validations

These are the validation rules applied when processing the `on_search` API call in the L1validations flow.
There are **48** validation rules organized into **8** top-level group(s).

---
## ON_SEARCH_CONTEXT

This group contains **3** sub-group(s)/validation(s): CONTEXT_REQUIRED, CONTEXT_ENUM, and CONTEXT_REGEX.

---

### CONTEXT_REQUIRED

This is a group of **12** sub-validation(s) that all must pass: REQUIRED_CONTEXT_LOCATION_COUNTRY_CODE, REQUIRED_CONTEXT_LOCATION_CITY_CODE, REQUIRED_CONTEXT_DOMAIN, REQUIRED_CONTEXT_TIMESTAMP, REQUIRED_CONTEXT_BAP_ID, REQUIRED_CONTEXT_BAP_URI, REQUIRED_CONTEXT_BPP_ID, REQUIRED_CONTEXT_BPP_URI, REQUIRED_CONTEXT_TRANSACTION_ID, REQUIRED_CONTEXT_MESSAGE_ID, REQUIRED_CONTEXT_VERSION, and REQUIRED_CONTEXT_TTL.

---

**REQUIRED_CONTEXT_LOCATION_COUNTRY_CODE**
`group: ON_SEARCH_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.location.country.code must be present in the payload

**REQUIRED_CONTEXT_LOCATION_CITY_CODE**
`group: ON_SEARCH_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.location.city.code must be present in the payload

**REQUIRED_CONTEXT_DOMAIN**
`group: ON_SEARCH_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.domain must be present in the payload

**REQUIRED_CONTEXT_TIMESTAMP**
`group: ON_SEARCH_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.timestamp must be present in the payload

**REQUIRED_CONTEXT_BAP_ID**
`group: ON_SEARCH_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.bap_id must be present in the payload

**REQUIRED_CONTEXT_BAP_URI**
`group: ON_SEARCH_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.bap_uri must be present in the payload

**REQUIRED_CONTEXT_BPP_ID**
`group: ON_SEARCH_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.bpp_id must be present in the payload

> **Skip if:**
>
>     - all elements of ["on_search"] are in ["search"]

**REQUIRED_CONTEXT_BPP_URI**
`group: ON_SEARCH_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.bpp_uri must be present in the payload

> **Skip if:**
>
>     - all elements of ["on_search"] are in ["search"]

**REQUIRED_CONTEXT_TRANSACTION_ID**
`group: ON_SEARCH_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.transaction_id must be present in the payload

**REQUIRED_CONTEXT_MESSAGE_ID**
`group: ON_SEARCH_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.message_id must be present in the payload

**REQUIRED_CONTEXT_VERSION**
`group: ON_SEARCH_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.version must be present in the payload

**REQUIRED_CONTEXT_TTL**
`group: ON_SEARCH_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.ttl must be present in the payload

### CONTEXT_ENUM

This is a group of **2** sub-validation(s) that all must pass: VALID_CONTEXT_LOCATION_COUNTRY_CODE and VALID_CONTEXT_DOMAIN.

---

**VALID_CONTEXT_LOCATION_COUNTRY_CODE**
`group: ON_SEARCH_CONTEXT > CONTEXT_ENUM | type: leaf`

- At least one of $.context.location.country.code must be in ["IND"]

> **Skip if:**
>
>     - $.context.location.country.code is not in the payload

**VALID_CONTEXT_DOMAIN**
`group: ON_SEARCH_CONTEXT > CONTEXT_ENUM | type: leaf`

- All elements of $.context.domain must be in ["ONDC:FIS12"]

> **Skip if:**
>
>     - $.context.domain is not in the payload

### CONTEXT_REGEX

This is a group of **5** sub-validation(s) that all must pass: REGEX_CONTEXT_LOCATION_CITY_CODE, REGEX_CONTEXT_TIMESTAMP, REGEX_CONTEXT_BAP_ID, REGEX_CONTEXT_BAP_URI, and REGEX_CONTEXT_TTL.

---

**REGEX_CONTEXT_LOCATION_CITY_CODE**
`group: ON_SEARCH_CONTEXT > CONTEXT_REGEX | type: leaf`

- All elements of $.context.location.city.code must follow every regex in ["^\*$"]

> **Skip if:**
>
>     - $.context.location.city.code is not in the payload

**REGEX_CONTEXT_TIMESTAMP**
`group: ON_SEARCH_CONTEXT > CONTEXT_REGEX | type: leaf`

- All elements of $.context.timestamp must follow every regex in ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[+-]\\d{2}:\\d{2})$"]

> **Skip if:**
>
>     - $.context.timestamp is not in the payload

**REGEX_CONTEXT_BAP_ID**
`group: ON_SEARCH_CONTEXT > CONTEXT_REGEX | type: leaf`

- All elements of $.context.bap_id must follow every regex in ["^(?!.*\b(?:http|https|www)\b)[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)+$"]

> **Skip if:**
>
>     - $.context.bap_id is not in the payload

**REGEX_CONTEXT_BAP_URI**
`group: ON_SEARCH_CONTEXT > CONTEXT_REGEX | type: leaf`

- All elements of $.context.bap_uri must follow every regex in ["^https?://([a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*|localhost)(:\d+)?(/.*)?$"]

> **Skip if:**
>
>     - $.context.bap_uri is not in the payload

**REGEX_CONTEXT_TTL**
`group: ON_SEARCH_CONTEXT > CONTEXT_REGEX | type: leaf`

- All elements of $.context.ttl must follow every regex in ["^P(?=\\d|T\\d)(\\d+Y)?(\\d+M)?(\\d+D)?(T(\\d+H)?(\\d+M)?(\\d+S)?)?$"]

> **Skip if:**
>
>     - $.context.ttl is not in the payload

---

## ON_SEARCH_CATALOG_NAME

`group: top-level | type: leaf`

- $.message.catalog.descriptor.name must be present in the payload

---

## ON_SEARCH_CATEGORIES

This is a group of **5** sub-validation(s) that all must pass: REQUIRED_CATEGORIES_NAME, REQUIRED_CATEGORIES_CODE, VALID_ENUM_CATEGORIES_CODE, REQUIRED_CATEGORIES_ID, and REQUIRED_CATEGORIES_PARENT_ID.

---

**REQUIRED_CATEGORIES_NAME**
`group: ON_SEARCH_CATEGORIES | type: leaf`

- $.message.catalog.providers[*].categories[*].descriptor.name must be present in the payload

**REQUIRED_CATEGORIES_CODE**
`group: ON_SEARCH_CATEGORIES | type: leaf`

- $.message.catalog.providers[*].categories[*].descriptor.code must be present in the payload

**VALID_ENUM_CATEGORIES_CODE**
`group: ON_SEARCH_CATEGORIES | type: leaf`

- All elements of $.message.catalog.providers[*].categories[*].descriptor.code must be in ["PERSONAL_LOAN", "BUREAU_LOAN", "AA_PERSONAL_LOAN", "GOLD_LOAN", "AA_LOAN", "LOAN", "PERSONAL_INFORMATION"]

**REQUIRED_CATEGORIES_ID**
`group: ON_SEARCH_CATEGORIES | type: leaf`

- $.message.catalog.providers[*].categories[*].id must be present in the payload

**REQUIRED_CATEGORIES_PARENT_ID**
`group: ON_SEARCH_CATEGORIES | type: leaf`

- $.message.catalog.providers[*].categories[*].parent_category_id must be present in the payload

> **Skip if:**
>
>     - any of ["BUREAU_LOAN", "AA_LOAN", "PERSONAL_LOAN", "AA_PERSONAL_LOAN", "GOLD_LOAN"] are in $.message.catalog.providers[*].categories[*].descriptor.code

---

## ON_SEARCH_PROVIDER

This is a group of **4** sub-validation(s) that all must pass: REQUIRED_PROVIDER_ID, REQUIRED_PROVIDER_NAME, REQUIRED_PROVIDER_IMAGES_URL, and REQUIRED_PROVIDER_IMAGES_SIZE_TYPE.

---

**REQUIRED_PROVIDER_ID**
`group: ON_SEARCH_PROVIDER | type: leaf`

- $.message.catalog.providers[*].id must be present in the payload

**REQUIRED_PROVIDER_NAME**
`group: ON_SEARCH_PROVIDER | type: leaf`

- $.message.catalog.providers[*].descriptor.name must be present in the payload

**REQUIRED_PROVIDER_IMAGES_URL**
`group: ON_SEARCH_PROVIDER | type: leaf`

- $.message.catalog.providers[*].descriptor.images[*].url must be present in the payload

**REQUIRED_PROVIDER_IMAGES_SIZE_TYPE**
`group: ON_SEARCH_PROVIDER | type: leaf`

- $.message.catalog.providers[*].descriptor.images[*].size_type must be present in the payload

---

## ON_SEARCH_PROVIDER_CONTACT_INFO

This is a group of **2** sub-validation(s) that all must pass: REQUIRED_CONTACT_INFO_TAG_GROUP and REQUIRED_CONTACT_INFO_LIST.

---

**REQUIRED_CONTACT_INFO_TAG_GROUP**
`group: ON_SEARCH_PROVIDER_CONTACT_INFO | type: leaf`

- At least one of $.message.catalog.providers[*].tags[*].descriptor.code must be in ["CONTACT_INFO"]

**REQUIRED_CONTACT_INFO_LIST**
`group: ON_SEARCH_PROVIDER_CONTACT_INFO | type: leaf | scope: $.message.catalog.providers[*].tags[?(@.descriptor.code=='CONTACT_INFO')]`

- All elements of $.message.catalog.providers[*].tags[?(@.descriptor.code=='CONTACT_INFO')].list[*].descriptor.code must be in ["GRO_NAME", "GRO_EMAIL", "GRO_CONTACT_NUMBER", "CUSTOMER_SUPPORT_LINK", "CUSTOMER_SUPPORT_CONTACT_NUMBER", "CUSTOMER_SUPPORT_EMAIL"]

> **Skip if:**
>
>     - $.message.catalog.providers[*].tags[?(@.descriptor.code=='CONTACT_INFO')].list[*].descriptor.code is not in the payload

---

## ON_SEARCH_PROVIDER_LSP_INFO

This is a group of **2** sub-validation(s) that all must pass: REQUIRED_LSP_INFO_TAG_GROUP and REQUIRED_LSP_INFO_LIST.

---

**REQUIRED_LSP_INFO_TAG_GROUP**
`group: ON_SEARCH_PROVIDER_LSP_INFO | type: leaf`

- At least one of $.message.catalog.providers[*].tags[*].descriptor.code must be in ["LSP_INFO"]

**REQUIRED_LSP_INFO_LIST**
`group: ON_SEARCH_PROVIDER_LSP_INFO | type: leaf | scope: $.message.catalog.providers[*].tags[?(@.descriptor.code=='LSP_INFO')]`

- All elements of $.message.catalog.providers[*].tags[?(@.descriptor.code=='LSP_INFO')].list[*].descriptor.code must be in ["LSP_NAME", "LSP_EMAIL", "LSP_CONTACT_NUMBER", "LSP_ADDRESS"]

> **Skip if:**
>
>     - $.message.catalog.providers[*].tags[?(@.descriptor.code=='LSP_INFO')].list[*].descriptor.code is not in the payload

---

## ON_SEARCH_PAYMENT

This is a group of **7** sub-validation(s) that all must pass: REQUIRED_PAYMENT_COLLECTED_BY, VALID_PAYMENT_COLLECTED_BY_ENUM, REQUIRED_BUYER_FINDER_FEES_TAG, REQUIRED_BUYER_FINDER_FEES_LIST, VALID_BUYER_FINDER_FEES_TYPE_VALUE, REQUIRED_SETTLEMENT_TERMS_TAG, and REQUIRED_SETTLEMENT_TERMS_LIST.

---

**REQUIRED_PAYMENT_COLLECTED_BY**
`group: ON_SEARCH_PAYMENT | type: leaf`

- $.message.catalog.providers[*].payments[*].collected_by must be present in the payload

**VALID_PAYMENT_COLLECTED_BY_ENUM**
`group: ON_SEARCH_PAYMENT | type: leaf`

- All elements of $.message.catalog.providers[*].payments[*].collected_by must be in ["BPP", "BAP"]

**REQUIRED_BUYER_FINDER_FEES_TAG**
`group: ON_SEARCH_PAYMENT | type: leaf`

- At least one of $.message.catalog.providers[*].payments[*].tags[*].descriptor.code must be in ["BUYER_FINDER_FEES"]

**REQUIRED_BUYER_FINDER_FEES_LIST**
`group: ON_SEARCH_PAYMENT | type: leaf | scope: $.message.catalog.providers[*].payments[*].tags[?(@.descriptor.code=='BUYER_FINDER_FEES')]`

- All elements of $.message.catalog.providers[*].payments[*].tags[?(@.descriptor.code=='BUYER_FINDER_FEES')].list[*].descriptor.code must be in ["BUYER_FINDER_FEES_TYPE", "BUYER_FINDER_FEES_PERCENTAGE"]

> **Skip if:**
>
>     - $.message.catalog.providers[*].payments[*].tags[?(@.descriptor.code=='BUYER_FINDER_FEES')].list[*].descriptor.code is not in the payload

**VALID_BUYER_FINDER_FEES_TYPE_VALUE**
`group: ON_SEARCH_PAYMENT | type: leaf | scope: $.message.catalog.providers[*].payments[*].tags[?(@.descriptor.code=='BUYER_FINDER_FEES')].list[?(@.descriptor.code=='BUYER_FINDER_FEES_TYPE')]`

- All elements of $.message.catalog.providers[*].payments[*].tags[?(@.descriptor.code=='BUYER_FINDER_FEES')].list[?(@.descriptor.code=='BUYER_FINDER_FEES_TYPE')].value must be in ["PERCENT_ANNUALIZED"]

**REQUIRED_SETTLEMENT_TERMS_TAG**
`group: ON_SEARCH_PAYMENT | type: leaf`

- At least one of $.message.catalog.providers[*].payments[*].tags[*].descriptor.code must be in ["SETTLEMENT_TERMS"]

**REQUIRED_SETTLEMENT_TERMS_LIST**
`group: ON_SEARCH_PAYMENT | type: leaf | scope: $.message.catalog.providers[*].payments[*].tags[?(@.descriptor.code=='SETTLEMENT_TERMS')]`

- All elements of $.message.catalog.providers[*].payments[*].tags[?(@.descriptor.code=='SETTLEMENT_TERMS')].list[*].descriptor.code must be in ["SETTLEMENT_WINDOW", "SETTLEMENT_BASIS", "MANDATORY_ARBITRATION", "COURT_JURISDICTION", "STATIC_TERMS", "OFFLINE_CONTRACT"]

> **Skip if:**
>
>     - $.message.catalog.providers[*].payments[*].tags[?(@.descriptor.code=='SETTLEMENT_TERMS')].list[*].descriptor.code is not in the payload

---

## ON_SEARCH_ITEMS

This is a group of **8** sub-validation(s) that all must pass: REQUIRED_ITEM_ID, REQUIRED_ITEM_CATEGORY_IDS, REQUIRED_ITEM_DESCRIPTOR_NAME, REQUIRED_GENERAL_INFO_TAG_GROUP, REQUIRED_GENERAL_INFO_LIST, REQUIRED_XINPUT, REQUIRED_XINPUT_FORM_URL, and VALID_XINPUT_HEADINGS_ENUM.

> **Skip if:**
> - $.message.catalog.providers[*].items[*].id must **not** be present in the payload

---

**REQUIRED_ITEM_ID**
`group: ON_SEARCH_ITEMS | type: leaf`

- $.message.catalog.providers[*].items[*].id must be present in the payload

**REQUIRED_ITEM_CATEGORY_IDS**
`group: ON_SEARCH_ITEMS | type: leaf`

- $.message.catalog.providers[*].items[*].category_ids[*] must be present in the payload

**REQUIRED_ITEM_DESCRIPTOR_NAME**
`group: ON_SEARCH_ITEMS | type: leaf`

- $.message.catalog.providers[*].items[*].descriptor.name must be present in the payload

**REQUIRED_GENERAL_INFO_TAG_GROUP**
`group: ON_SEARCH_ITEMS | type: leaf`

- At least one of $.message.catalog.providers[*].items[*].tags[*].descriptor.code must be in ["GENERAL_INFO"]

**REQUIRED_GENERAL_INFO_LIST**
`group: ON_SEARCH_ITEMS | type: leaf | scope: $.message.catalog.providers[*].items[*].tags[?(@.descriptor.code=='GENERAL_INFO')]`

- All elements of $.message.catalog.providers[*].items[*].tags[?(@.descriptor.code=='GENERAL_INFO')].list[*].descriptor.code must be in ["MIN_INTEREST_RATE", "MAX_INTEREST_RATE", "MIN_TENURE", "MAX_TENURE", "MIN_LOAN_AMOUNT", "MAX_LOAN_AMOUNT"]

> **Skip if:**
>
>     - $.message.catalog.providers[*].items[*].tags[?(@.descriptor.code=='GENERAL_INFO')].list[*].descriptor.code is not in the payload

**REQUIRED_XINPUT**
`group: ON_SEARCH_ITEMS | type: leaf`

- $.message.catalog.providers[*].items[*].xinput.required must be present in the payload

**REQUIRED_XINPUT_FORM_URL**
`group: ON_SEARCH_ITEMS | type: leaf`

- $.message.catalog.providers[*].items[*].xinput.form.url must be present in the payload

**VALID_XINPUT_HEADINGS_ENUM**
`group: ON_SEARCH_ITEMS | type: leaf`

- All elements of $.message.catalog.providers[*].items[*].xinput.head.headings[*] must be in ["KYC", "BUREAU_CONSENT", "AA_CONSENT", "Personal Information", "Set Loan Amount", "Know your Customer", "Account Information", "Emandate", "Loan Agreement", "PERSONAL_INFORMATION", "Loan Details"]
