---
action: on_select
codeName: L1validations
numTests: 67
generated: 2026-03-18
domain: ONDC:FIS12
version: 2.0.2
---

# L1validations — `on_select` Validations

These are the validation rules applied when processing the `on_select` API call in the L1validations flow.
There are **67** validation rules organized into **14** top-level group(s).

---
## ON_SELECT_CONTEXT

This group contains **3** sub-group(s)/validation(s): CONTEXT_REQUIRED, CONTEXT_ENUM, and CONTEXT_REGEX.

---

### CONTEXT_REQUIRED

This is a group of **12** sub-validation(s) that all must pass: REQUIRED_CONTEXT_LOCATION_COUNTRY_CODE, REQUIRED_CONTEXT_LOCATION_CITY_CODE, REQUIRED_CONTEXT_DOMAIN, REQUIRED_CONTEXT_TIMESTAMP, REQUIRED_CONTEXT_BAP_ID, REQUIRED_CONTEXT_BAP_URI, REQUIRED_CONTEXT_BPP_ID, REQUIRED_CONTEXT_BPP_URI, REQUIRED_CONTEXT_TRANSACTION_ID, REQUIRED_CONTEXT_MESSAGE_ID, REQUIRED_CONTEXT_VERSION, and REQUIRED_CONTEXT_TTL.

---

**REQUIRED_CONTEXT_LOCATION_COUNTRY_CODE**
`group: ON_SELECT_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.location.country.code must be present in the payload

**REQUIRED_CONTEXT_LOCATION_CITY_CODE**
`group: ON_SELECT_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.location.city.code must be present in the payload

**REQUIRED_CONTEXT_DOMAIN**
`group: ON_SELECT_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.domain must be present in the payload

**REQUIRED_CONTEXT_TIMESTAMP**
`group: ON_SELECT_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.timestamp must be present in the payload

**REQUIRED_CONTEXT_BAP_ID**
`group: ON_SELECT_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.bap_id must be present in the payload

**REQUIRED_CONTEXT_BAP_URI**
`group: ON_SELECT_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.bap_uri must be present in the payload

**REQUIRED_CONTEXT_BPP_ID**
`group: ON_SELECT_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.bpp_id must be present in the payload

> **Skip if:**
>
>     - all elements of ["on_select"] are in ["search"]

**REQUIRED_CONTEXT_BPP_URI**
`group: ON_SELECT_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.bpp_uri must be present in the payload

> **Skip if:**
>
>     - all elements of ["on_select"] are in ["search"]

**REQUIRED_CONTEXT_TRANSACTION_ID**
`group: ON_SELECT_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.transaction_id must be present in the payload

**REQUIRED_CONTEXT_MESSAGE_ID**
`group: ON_SELECT_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.message_id must be present in the payload

**REQUIRED_CONTEXT_VERSION**
`group: ON_SELECT_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.version must be present in the payload

**REQUIRED_CONTEXT_TTL**
`group: ON_SELECT_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.ttl must be present in the payload

### CONTEXT_ENUM

This is a group of **2** sub-validation(s) that all must pass: VALID_CONTEXT_LOCATION_COUNTRY_CODE and VALID_CONTEXT_DOMAIN.

---

**VALID_CONTEXT_LOCATION_COUNTRY_CODE**
`group: ON_SELECT_CONTEXT > CONTEXT_ENUM | type: leaf`

- At least one of $.context.location.country.code must be in ["IND"]

> **Skip if:**
>
>     - $.context.location.country.code is not in the payload

**VALID_CONTEXT_DOMAIN**
`group: ON_SELECT_CONTEXT > CONTEXT_ENUM | type: leaf`

- All elements of $.context.domain must be in ["ONDC:FIS12"]

> **Skip if:**
>
>     - $.context.domain is not in the payload

### CONTEXT_REGEX

This is a group of **5** sub-validation(s) that all must pass: REGEX_CONTEXT_LOCATION_CITY_CODE, REGEX_CONTEXT_TIMESTAMP, REGEX_CONTEXT_BAP_ID, REGEX_CONTEXT_BAP_URI, and REGEX_CONTEXT_TTL.

---

**REGEX_CONTEXT_LOCATION_CITY_CODE**
`group: ON_SELECT_CONTEXT > CONTEXT_REGEX | type: leaf`

- All elements of $.context.location.city.code must follow every regex in ["^\*$"]

> **Skip if:**
>
>     - $.context.location.city.code is not in the payload

**REGEX_CONTEXT_TIMESTAMP**
`group: ON_SELECT_CONTEXT > CONTEXT_REGEX | type: leaf`

- All elements of $.context.timestamp must follow every regex in ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[+-]\\d{2}:\\d{2})$"]

> **Skip if:**
>
>     - $.context.timestamp is not in the payload

**REGEX_CONTEXT_BAP_ID**
`group: ON_SELECT_CONTEXT > CONTEXT_REGEX | type: leaf`

- All elements of $.context.bap_id must follow every regex in ["^(?!.*\b(?:http|https|www)\b)[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)+$"]

> **Skip if:**
>
>     - $.context.bap_id is not in the payload

**REGEX_CONTEXT_BAP_URI**
`group: ON_SELECT_CONTEXT > CONTEXT_REGEX | type: leaf`

- All elements of $.context.bap_uri must follow every regex in ["^https?://([a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*|localhost)(:\d+)?(/.*)?$"]

> **Skip if:**
>
>     - $.context.bap_uri is not in the payload

**REGEX_CONTEXT_TTL**
`group: ON_SELECT_CONTEXT > CONTEXT_REGEX | type: leaf`

- All elements of $.context.ttl must follow every regex in ["^P(?=\\d|T\\d)(\\d+Y)?(\\d+M)?(\\d+D)?(T(\\d+H)?(\\d+M)?(\\d+S)?)?$"]

> **Skip if:**
>
>     - $.context.ttl is not in the payload

---

## ON_SELECT_PROVIDER

This is a group of **2** sub-validation(s) that all must pass: REQUIRED_PROVIDER_ID and REQUIRED_PROVIDER_NAME.

---

**REQUIRED_PROVIDER_ID**
`group: ON_SELECT_PROVIDER | type: leaf`

- $.message.order.provider.id must be present in the payload

**REQUIRED_PROVIDER_NAME**
`group: ON_SELECT_PROVIDER | type: leaf`

- $.message.order.provider.descriptor.name must be present in the payload

---

## ON_SELECT_PROVIDER_LOCATIONS_GOLD

This is a group of **3** sub-validation(s) that all must pass: REQUIRED_PROVIDER_LOCATIONS, REQUIRED_PROVIDER_LOCATION_GPS, and REQUIRED_PROVIDER_LOCATION_ADDRESS.

> **Skip if:**
> **Any of these must be true:**
>   - None of $.message.order.items[*].descriptor.code may be in ["LOAN"]
>   - $.message.order.provider.locations[*].id must **not** be present in the payload

---

**REQUIRED_PROVIDER_LOCATIONS**
`group: ON_SELECT_PROVIDER_LOCATIONS_GOLD | type: leaf`

- $.message.order.provider.locations[*].id must be present in the payload

**REQUIRED_PROVIDER_LOCATION_GPS**
`group: ON_SELECT_PROVIDER_LOCATIONS_GOLD | type: leaf`

- $.message.order.provider.locations[*].gps must be present in the payload

**REQUIRED_PROVIDER_LOCATION_ADDRESS**
`group: ON_SELECT_PROVIDER_LOCATIONS_GOLD | type: leaf`

- $.message.order.provider.locations[*].address must be present in the payload

---

## ON_SELECT_PROVIDER_TAGS

This is a group of **4** sub-validation(s) that all must pass: REQUIRED_CONTACT_INFO_TAG_GROUP, REQUIRED_CONTACT_INFO_LIST, REQUIRED_LSP_INFO_TAG_GROUP, and REQUIRED_LSP_INFO_LIST.

---

**REQUIRED_CONTACT_INFO_TAG_GROUP**
`group: ON_SELECT_PROVIDER_TAGS | type: leaf`

- At least one of $.message.order.provider.tags[*].descriptor.code must be in ["CONTACT_INFO"]

**REQUIRED_CONTACT_INFO_LIST**
`group: ON_SELECT_PROVIDER_TAGS | type: leaf | scope: $.message.order.provider.tags[?(@.descriptor.code=='CONTACT_INFO')]`

- All elements of $.message.order.provider.tags[?(@.descriptor.code=='CONTACT_INFO')].list[*].descriptor.code must be in ["GRO_NAME", "GRO_EMAIL", "GRO_CONTACT_NUMBER", "GRO_DESIGNATION", "GRO_ADDRESS", "CUSTOMER_SUPPORT_LINK", "CUSTOMER_SUPPORT_CONTACT_NUMBER", "CUSTOMER_SUPPORT_EMAIL"]

> **Skip if:**
>
>     - $.message.order.provider.tags[?(@.descriptor.code=='CONTACT_INFO')].list[*].descriptor.code is not in the payload

**REQUIRED_LSP_INFO_TAG_GROUP**
`group: ON_SELECT_PROVIDER_TAGS | type: leaf`

- At least one of $.message.order.provider.tags[*].descriptor.code must be in ["LSP_INFO"]

**REQUIRED_LSP_INFO_LIST**
`group: ON_SELECT_PROVIDER_TAGS | type: leaf | scope: $.message.order.provider.tags[?(@.descriptor.code=='LSP_INFO')]`

- All elements of $.message.order.provider.tags[?(@.descriptor.code=='LSP_INFO')].list[*].descriptor.code must be in ["LSP_NAME", "LSP_EMAIL", "LSP_CONTACT_NUMBER", "LSP_ADDRESS"]

> **Skip if:**
>
>     - $.message.order.provider.tags[?(@.descriptor.code=='LSP_INFO')].list[*].descriptor.code is not in the payload

---

## ON_SELECT_ITEMS_BASIC

This is a group of **4** sub-validation(s) that all must pass: REQUIRED_ITEM_ID, REQUIRED_ITEM_DESCRIPTOR_CODE, VALID_ITEM_DESCRIPTOR_CODE_ENUM, and REQUIRED_ITEM_DESCRIPTOR_NAME.

---

**REQUIRED_ITEM_ID**
`group: ON_SELECT_ITEMS_BASIC | type: leaf`

- $.message.order.items[*].id must be present in the payload

**REQUIRED_ITEM_DESCRIPTOR_CODE**
`group: ON_SELECT_ITEMS_BASIC | type: leaf`

- $.message.order.items[*].descriptor.code must be present in the payload

**VALID_ITEM_DESCRIPTOR_CODE_ENUM**
`group: ON_SELECT_ITEMS_BASIC | type: leaf`

- All elements of $.message.order.items[*].descriptor.code must be in ["LOAN", "PERSONAL_LOAN"]

**REQUIRED_ITEM_DESCRIPTOR_NAME**
`group: ON_SELECT_ITEMS_BASIC | type: leaf`

- $.message.order.items[*].descriptor.name must be present in the payload

---

## ON_SELECT_1_AA_CONSENT_ITEMS

This is a group of **2** sub-validation(s) that all must pass: REQUIRED_CONSENT_INFO_TAG and REQUIRED_CONSENT_HANDLER.

> **Skip if:**
> - $.message.order.items[*].price.value must be present in the payload

---

**REQUIRED_CONSENT_INFO_TAG**
`group: ON_SELECT_1_AA_CONSENT_ITEMS | type: leaf`

- At least one of $.message.order.items[*].tags[*].descriptor.code must be in ["CONSENT_INFO"]

**REQUIRED_CONSENT_HANDLER**
`group: ON_SELECT_1_AA_CONSENT_ITEMS | type: leaf | scope: $.message.order.items[*].tags[?(@.descriptor.code=='CONSENT_INFO')]`

- At least one of $.message.order.items[*].tags[?(@.descriptor.code=='CONSENT_INFO')].list[*].descriptor.code must be in ["CONSENT_HANDLER"]

---

## ON_SELECT_1_AA_CONSENT_XINPUT

This is a group of **4** sub-validation(s) that all must pass: REQUIRED_XINPUT_FORM, REQUIRED_XINPUT_FORM_RESPONSE, VALID_XINPUT_FORM_RESPONSE_STATUS, and REQUIRED_XINPUT_FORM_RESPONSE_SUBMISSION_ID.

> **Skip if:**
> - $.message.order.items[*].price.value must be present in the payload

---

**REQUIRED_XINPUT_FORM**
`group: ON_SELECT_1_AA_CONSENT_XINPUT | type: leaf`

- $.message.order.items[*].xinput.form.id must be present in the payload

**REQUIRED_XINPUT_FORM_RESPONSE**
`group: ON_SELECT_1_AA_CONSENT_XINPUT | type: leaf`

- $.message.order.items[*].xinput.form_response.status must be present in the payload

**VALID_XINPUT_FORM_RESPONSE_STATUS**
`group: ON_SELECT_1_AA_CONSENT_XINPUT | type: leaf`

- All elements of $.message.order.items[*].xinput.form_response.status must be in ["PENDING", "SUCCESS"]

**REQUIRED_XINPUT_FORM_RESPONSE_SUBMISSION_ID**
`group: ON_SELECT_1_AA_CONSENT_XINPUT | type: leaf`

- $.message.order.items[*].xinput.form_response.submission_id must be present in the payload

---

## ON_SELECT_2_OFFER_ITEMS_PRICE

This is a group of **2** sub-validation(s) that all must pass: REQUIRED_ITEM_PRICE and REQUIRED_ITEM_PRICE_CURRENCY.

> **Skip if:**
> - $.message.order.items[*].price.value must **not** be present in the payload

---

**REQUIRED_ITEM_PRICE**
`group: ON_SELECT_2_OFFER_ITEMS_PRICE | type: leaf`

- $.message.order.items[*].price.value must be present in the payload

**REQUIRED_ITEM_PRICE_CURRENCY**
`group: ON_SELECT_2_OFFER_ITEMS_PRICE | type: leaf`

- All elements of $.message.order.items[*].price.currency must be in ["INR"]

---

## ON_SELECT_2_OFFER_LOAN_INFO

This is a group of **3** sub-validation(s) that all must pass: REQUIRED_LOAN_INFO_TAG_GROUP, REQUIRED_LOAN_INFO_LIST_COMMON, and REQUIRED_LOAN_INFO_LTV_RATIO_GOLD.

> **Skip if:**
> - $.message.order.items[*].price.value must **not** be present in the payload

---

**REQUIRED_LOAN_INFO_TAG_GROUP**
`group: ON_SELECT_2_OFFER_LOAN_INFO | type: leaf`

- At least one of $.message.order.items[*].tags[*].descriptor.code must be in ["LOAN_INFO"]

**REQUIRED_LOAN_INFO_LIST_COMMON**
`group: ON_SELECT_2_OFFER_LOAN_INFO | type: leaf | scope: $.message.order.items[*].tags[?(@.descriptor.code=='LOAN_INFO')]`

- At least one of $.message.order.items[*].tags[?(@.descriptor.code=='LOAN_INFO')].list[*].descriptor.code must be in ["INTEREST_RATE", "TERM", "INTEREST_RATE_TYPE", "APPLICATION_FEE", "FORECLOSURE_FEE", "INTEREST_RATE_CONVERSION_CHARGE", "DELAY_PENALTY_FEE", "OTHER_PENALTY_FEE", "ANNUAL_PERCENTAGE_RATE", "REPAYMENT_FREQUENCY", "NUMBER_OF_INSTALLMENTS_OF_REPAYMENT", "TNC_LINK", "COOL_OFF_PERIOD", "INSTALLMENT_AMOUNT"]

> **Skip if:**
>
>     - $.message.order.items[*].tags[?(@.descriptor.code=='LOAN_INFO')].list[*].descriptor.code is not in the payload

**REQUIRED_LOAN_INFO_LTV_RATIO_GOLD**
`group: ON_SELECT_2_OFFER_LOAN_INFO | type: leaf | scope: $.message.order.items[?(@.descriptor.code=='LOAN')].tags[?(@.descriptor.code=='LOAN_INFO')]`

- At least one of $.message.order.items[?(@.descriptor.code=='LOAN')].tags[?(@.descriptor.code=='LOAN_INFO')].list[*].descriptor.code must be in ["LTV_RATIO"]

---

## ON_SELECT_2_OFFER_QUOTE

This group contains **4** sub-group(s)/validation(s): REQUIRED_QUOTE_ID, REQUIRED_QUOTE_PRICE, REQUIRED_QUOTE_BREAKUP, and REQUIRED_QUOTE_TTL.

> **Skip if:**
> - $.message.order.items[*].price.value must **not** be present in the payload

---

**REQUIRED_QUOTE_ID**
`group: ON_SELECT_2_OFFER_QUOTE | type: leaf`

- $.message.order.quote.id must be present in the payload

### REQUIRED_QUOTE_PRICE

This is a group of **2** sub-validation(s) that all must pass: REQUIRED_QUOTE_PRICE_VALUE and REQUIRED_QUOTE_PRICE_CURRENCY.

---

**REQUIRED_QUOTE_PRICE_VALUE**
`group: ON_SELECT_2_OFFER_QUOTE > REQUIRED_QUOTE_PRICE | type: leaf`

- $.message.order.quote.price.value must be present in the payload

**REQUIRED_QUOTE_PRICE_CURRENCY**
`group: ON_SELECT_2_OFFER_QUOTE > REQUIRED_QUOTE_PRICE | type: leaf`

- All elements of $.message.order.quote.price.currency must be in ["INR"]

### REQUIRED_QUOTE_BREAKUP

This is a group of **4** sub-validation(s) that all must pass: REQUIRED_QUOTE_BREAKUP_TITLE, VALID_QUOTE_BREAKUP_TITLE_ENUM, REQUIRED_QUOTE_BREAKUP_PRICE, and REQUIRED_QUOTE_BREAKUP_PRICE_CURRENCY.

---

**REQUIRED_QUOTE_BREAKUP_TITLE**
`group: ON_SELECT_2_OFFER_QUOTE > REQUIRED_QUOTE_BREAKUP | type: leaf`

- $.message.order.quote.breakup[*].title must be present in the payload

**VALID_QUOTE_BREAKUP_TITLE_ENUM**
`group: ON_SELECT_2_OFFER_QUOTE > REQUIRED_QUOTE_BREAKUP | type: leaf`

- At least one of $.message.order.quote.breakup[*].title must be in ["PRINCIPAL", "INTEREST", "PROCESSING_FEE", "OTHER_UPFRONT_CHARGES", "INSURANCE_CHARGES", "NET_DISBURSED_AMOUNT", "OTHER_CHARGES"]

**REQUIRED_QUOTE_BREAKUP_PRICE**
`group: ON_SELECT_2_OFFER_QUOTE > REQUIRED_QUOTE_BREAKUP | type: leaf`

- $.message.order.quote.breakup[*].price.value must be present in the payload

**REQUIRED_QUOTE_BREAKUP_PRICE_CURRENCY**
`group: ON_SELECT_2_OFFER_QUOTE > REQUIRED_QUOTE_BREAKUP | type: leaf`

- All elements of $.message.order.quote.breakup[*].price.currency must be in ["INR"]

**REQUIRED_QUOTE_TTL**
`group: ON_SELECT_2_OFFER_QUOTE | type: leaf`

- $.message.order.quote.ttl must be present in the payload

---

## ON_SELECT_2_OFFER_FULFILLMENT_GOLD

This is a group of **3** sub-validation(s) that all must pass: REQUIRED_FULFILLMENT_TYPE, REQUIRED_FULFILLMENT_AGENT_NAME, and REQUIRED_FULFILLMENT_AGENT_CONTACT.

> **Skip if:**
> **Any of these must be true:**
>   - None of $.message.order.items[*].descriptor.code may be in ["LOAN"]
>   - $.message.order.items[*].price.value must **not** be present in the payload

---

**REQUIRED_FULFILLMENT_TYPE**
`group: ON_SELECT_2_OFFER_FULFILLMENT_GOLD | type: leaf`

- All elements of $.message.order.fulfillments[*].type must be in ["LOAN"]

> **Skip if:**
>
>     - $.message.order.fulfillments[*].type is not in the payload

**REQUIRED_FULFILLMENT_AGENT_NAME**
`group: ON_SELECT_2_OFFER_FULFILLMENT_GOLD | type: leaf`

- $.message.order.fulfillments[*].agent.person.name must be present in the payload

> **Skip if:**
>
>     - $.message.order.fulfillments[*].agent.person.name is not in the payload

**REQUIRED_FULFILLMENT_AGENT_CONTACT**
`group: ON_SELECT_2_OFFER_FULFILLMENT_GOLD | type: leaf`

- $.message.order.fulfillments[*].agent.contact.phone must be present in the payload

> **Skip if:**
>
>     - $.message.order.fulfillments[*].agent.contact.phone is not in the payload

---

## ON_SELECT_2_OFFER_XINPUT_COMMON

This is a group of **3** sub-validation(s) that all must pass: REQUIRED_XINPUT_REQUIRED, REQUIRED_XINPUT_FORM_ID, and REQUIRED_XINPUT_FORM_URL.

> **Skip if:**
> - $.message.order.items[*].price.value must **not** be present in the payload

---

**REQUIRED_XINPUT_REQUIRED**
`group: ON_SELECT_2_OFFER_XINPUT_COMMON | type: leaf`

- $.message.order.items[*].xinput.required must be present in the payload

**REQUIRED_XINPUT_FORM_ID**
`group: ON_SELECT_2_OFFER_XINPUT_COMMON | type: leaf`

- $.message.order.items[*].xinput.form.id must be present in the payload

**REQUIRED_XINPUT_FORM_URL**
`group: ON_SELECT_2_OFFER_XINPUT_COMMON | type: leaf`

- $.message.order.items[*].xinput.form.url must be present in the payload

---

## ON_SELECT_2_OFFER_XINPUT_PERSONAL_LOAN

This group contains **3** sub-group(s)/validation(s): REQUIRED_XINPUT_HEAD_INDEX, REQUIRED_XINPUT_HEAD_DESCRIPTOR_NAME, and REQUIRED_XINPUT_HEAD_HEADINGS.

> **Skip if:**
> **Any of these must be true:**
>   - None of $.message.order.items[*].descriptor.code may be in ["PERSONAL_LOAN"]
>   - $.message.order.items[*].price.value must **not** be present in the payload

---

### REQUIRED_XINPUT_HEAD_INDEX

This is a group of **3** sub-validation(s) that all must pass: REQUIRED_XINPUT_HEAD_INDEX_MIN, REQUIRED_XINPUT_HEAD_INDEX_CUR, and REQUIRED_XINPUT_HEAD_INDEX_MAX.

---

**REQUIRED_XINPUT_HEAD_INDEX_MIN**
`group: ON_SELECT_2_OFFER_XINPUT_PERSONAL_LOAN > REQUIRED_XINPUT_HEAD_INDEX | type: leaf`

- $.message.order.items[*].xinput.head.index.min must be present in the payload

**REQUIRED_XINPUT_HEAD_INDEX_CUR**
`group: ON_SELECT_2_OFFER_XINPUT_PERSONAL_LOAN > REQUIRED_XINPUT_HEAD_INDEX | type: leaf`

- $.message.order.items[*].xinput.head.index.cur must be present in the payload

**REQUIRED_XINPUT_HEAD_INDEX_MAX**
`group: ON_SELECT_2_OFFER_XINPUT_PERSONAL_LOAN > REQUIRED_XINPUT_HEAD_INDEX | type: leaf`

- $.message.order.items[*].xinput.head.index.max must be present in the payload

**REQUIRED_XINPUT_HEAD_DESCRIPTOR_NAME**
`group: ON_SELECT_2_OFFER_XINPUT_PERSONAL_LOAN | type: leaf`

- $.message.order.items[*].xinput.head.descriptor.name must be present in the payload

**REQUIRED_XINPUT_HEAD_HEADINGS**
`group: ON_SELECT_2_OFFER_XINPUT_PERSONAL_LOAN | type: leaf`

- $.message.order.items[*].xinput.head.headings[*] must be present in the payload

---

## ON_SELECT_2_OFFER_XINPUT_GOLD

This group contains **3** sub-group(s)/validation(s): REQUIRED_XINPUT_HEAD_INDEX, REQUIRED_XINPUT_HEAD_DESCRIPTOR_NAME, and REQUIRED_XINPUT_HEAD_HEADINGS.

> **Skip if:**
> **Any of these must be true:**
>   - None of $.message.order.items[*].descriptor.code may be in ["LOAN"]
>   - $.message.order.items[*].price.value must **not** be present in the payload

---

### REQUIRED_XINPUT_HEAD_INDEX

This is a group of **3** sub-validation(s) that all must pass: REQUIRED_XINPUT_HEAD_INDEX_MIN, REQUIRED_XINPUT_HEAD_INDEX_CUR, and REQUIRED_XINPUT_HEAD_INDEX_MAX.

---

**REQUIRED_XINPUT_HEAD_INDEX_MIN**
`group: ON_SELECT_2_OFFER_XINPUT_GOLD > REQUIRED_XINPUT_HEAD_INDEX | type: leaf`

- $.message.order.items[*].xinput.head.index.min must be present in the payload

**REQUIRED_XINPUT_HEAD_INDEX_CUR**
`group: ON_SELECT_2_OFFER_XINPUT_GOLD > REQUIRED_XINPUT_HEAD_INDEX | type: leaf`

- $.message.order.items[*].xinput.head.index.cur must be present in the payload

**REQUIRED_XINPUT_HEAD_INDEX_MAX**
`group: ON_SELECT_2_OFFER_XINPUT_GOLD > REQUIRED_XINPUT_HEAD_INDEX | type: leaf`

- $.message.order.items[*].xinput.head.index.max must be present in the payload

**REQUIRED_XINPUT_HEAD_DESCRIPTOR_NAME**
`group: ON_SELECT_2_OFFER_XINPUT_GOLD | type: leaf`

- $.message.order.items[*].xinput.head.descriptor.name must be present in the payload

**REQUIRED_XINPUT_HEAD_HEADINGS**
`group: ON_SELECT_2_OFFER_XINPUT_GOLD | type: leaf`

- $.message.order.items[*].xinput.head.headings[*] must be present in the payload
