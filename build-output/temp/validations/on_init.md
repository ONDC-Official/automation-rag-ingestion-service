---
action: on_init
codeName: L1validations
numTests: 47
generated: 2026-04-15
domain: ONDC:FIS12
version: 2.3.0
---

# L1validations — `on_init` Validations

These are the validation rules applied when processing the `on_init` API call in the L1validations flow.
There are **47** validation rules organized into **8** top-level group(s).

---
## ON_INIT_CONTEXT

This group contains **3** sub-group(s)/validation(s): CONTEXT_REQUIRED, CONTEXT_ENUM, and CONTEXT_REGEX.

---

### CONTEXT_REQUIRED

This is a group of **12** sub-validation(s) that all must pass: REQUIRED_CONTEXT_LOCATION_COUNTRY_CODE, REQUIRED_CONTEXT_LOCATION_CITY_CODE, REQUIRED_CONTEXT_DOMAIN, REQUIRED_CONTEXT_TIMESTAMP, REQUIRED_CONTEXT_BAP_ID, REQUIRED_CONTEXT_BAP_URI, REQUIRED_CONTEXT_BPP_ID, REQUIRED_CONTEXT_BPP_URI, REQUIRED_CONTEXT_TRANSACTION_ID, REQUIRED_CONTEXT_MESSAGE_ID, REQUIRED_CONTEXT_VERSION, and REQUIRED_CONTEXT_TTL.

---

**REQUIRED_CONTEXT_LOCATION_COUNTRY_CODE**
`group: ON_INIT_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.location.country.code must be present in the payload

**REQUIRED_CONTEXT_LOCATION_CITY_CODE**
`group: ON_INIT_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.location.city.code must be present in the payload

**REQUIRED_CONTEXT_DOMAIN**
`group: ON_INIT_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.domain must be present in the payload

**REQUIRED_CONTEXT_TIMESTAMP**
`group: ON_INIT_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.timestamp must be present in the payload

**REQUIRED_CONTEXT_BAP_ID**
`group: ON_INIT_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.bap_id must be present in the payload

**REQUIRED_CONTEXT_BAP_URI**
`group: ON_INIT_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.bap_uri must be present in the payload

**REQUIRED_CONTEXT_BPP_ID**
`group: ON_INIT_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.bpp_id must be present in the payload

> **Skip if:**
>
>     - all elements of ["on_init"] are in ["search"]

**REQUIRED_CONTEXT_BPP_URI**
`group: ON_INIT_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.bpp_uri must be present in the payload

> **Skip if:**
>
>     - all elements of ["on_init"] are in ["search"]

**REQUIRED_CONTEXT_TRANSACTION_ID**
`group: ON_INIT_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.transaction_id must be present in the payload

**REQUIRED_CONTEXT_MESSAGE_ID**
`group: ON_INIT_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.message_id must be present in the payload

**REQUIRED_CONTEXT_VERSION**
`group: ON_INIT_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.version must be present in the payload

**REQUIRED_CONTEXT_TTL**
`group: ON_INIT_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.ttl must be present in the payload

### CONTEXT_ENUM

This is a group of **2** sub-validation(s) that all must pass: VALID_CONTEXT_LOCATION_COUNTRY_CODE and VALID_CONTEXT_DOMAIN.

---

**VALID_CONTEXT_LOCATION_COUNTRY_CODE**
`group: ON_INIT_CONTEXT > CONTEXT_ENUM | type: leaf`

- At least one of $.context.location.country.code must be in ["IND"]

> **Skip if:**
>
>     - $.context.location.country.code is not in the payload

**VALID_CONTEXT_DOMAIN**
`group: ON_INIT_CONTEXT > CONTEXT_ENUM | type: leaf`

- All elements of $.context.domain must be in ["ONDC:FIS12"]

> **Skip if:**
>
>     - $.context.domain is not in the payload

### CONTEXT_REGEX

This is a group of **5** sub-validation(s) that all must pass: REGEX_CONTEXT_LOCATION_CITY_CODE, REGEX_CONTEXT_TIMESTAMP, REGEX_CONTEXT_BAP_ID, REGEX_CONTEXT_BAP_URI, and REGEX_CONTEXT_TTL.

---

**REGEX_CONTEXT_LOCATION_CITY_CODE**
`group: ON_INIT_CONTEXT > CONTEXT_REGEX | type: leaf`

- All elements of $.context.location.city.code must follow every regex in ["^\*$"]

> **Skip if:**
>
>     - $.context.location.city.code is not in the payload

**REGEX_CONTEXT_TIMESTAMP**
`group: ON_INIT_CONTEXT > CONTEXT_REGEX | type: leaf`

- All elements of $.context.timestamp must follow every regex in ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[+-]\\d{2}:\\d{2})$"]

> **Skip if:**
>
>     - $.context.timestamp is not in the payload

**REGEX_CONTEXT_BAP_ID**
`group: ON_INIT_CONTEXT > CONTEXT_REGEX | type: leaf`

- All elements of $.context.bap_id must follow every regex in ["^(?!.*\b(?:http|https|www)\b)[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)+$"]

> **Skip if:**
>
>     - $.context.bap_id is not in the payload

**REGEX_CONTEXT_BAP_URI**
`group: ON_INIT_CONTEXT > CONTEXT_REGEX | type: leaf`

- All elements of $.context.bap_uri must follow every regex in ["^https?://([a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*|localhost)(:\d+)?(/.*)?$"]

> **Skip if:**
>
>     - $.context.bap_uri is not in the payload

**REGEX_CONTEXT_TTL**
`group: ON_INIT_CONTEXT > CONTEXT_REGEX | type: leaf`

- All elements of $.context.ttl must follow every regex in ["^P(?=\\d|T\\d)(\\d+Y)?(\\d+M)?(\\d+D)?(T(\\d+H)?(\\d+M)?(\\d+S)?)?$"]

> **Skip if:**
>
>     - $.context.ttl is not in the payload

---

## ON_INIT_PROVIDER

This group contains **3** sub-group(s)/validation(s): REQUIRED_PROVIDER_ID, REQUIRED_PROVIDER_NAME, and REQUIRED_PROVIDER_TAGS.

---

**REQUIRED_PROVIDER_ID**
`group: ON_INIT_PROVIDER | type: leaf`

- $.message.order.provider.id must be present in the payload

**REQUIRED_PROVIDER_NAME**
`group: ON_INIT_PROVIDER | type: leaf`

- $.message.order.provider.descriptor.name must be present in the payload

### REQUIRED_PROVIDER_TAGS

This is a group of **2** sub-validation(s) that all must pass: REQUIRED_CONTACT_INFO_TAG_GROUP and REQUIRED_LSP_INFO_TAG_GROUP.

---

**REQUIRED_CONTACT_INFO_TAG_GROUP**
`group: ON_INIT_PROVIDER > REQUIRED_PROVIDER_TAGS | type: leaf`

- At least one of $.message.order.provider.tags[*].descriptor.code must be in ["CONTACT_INFO"]

**REQUIRED_LSP_INFO_TAG_GROUP**
`group: ON_INIT_PROVIDER > REQUIRED_PROVIDER_TAGS | type: leaf`

- At least one of $.message.order.provider.tags[*].descriptor.code must be in ["LSP_INFO"]

---

## ON_INIT_ITEMS

This is a group of **5** sub-validation(s) that all must pass: REQUIRED_ITEM_ID, REQUIRED_ITEM_DESCRIPTOR_CODE, REQUIRED_ITEM_PRICE_VALUE, REQUIRED_ITEM_PRICE_CURRENCY, and REQUIRED_LOAN_INFO_TAG_GROUP.

---

**REQUIRED_ITEM_ID**
`group: ON_INIT_ITEMS | type: leaf`

- $.message.order.items[*].id must be present in the payload

**REQUIRED_ITEM_DESCRIPTOR_CODE**
`group: ON_INIT_ITEMS | type: leaf`

- All elements of $.message.order.items[*].descriptor.code must be in ["LOAN", "PERSONAL_LOAN", "CREDIT_CARD"]

**REQUIRED_ITEM_PRICE_VALUE**
`group: ON_INIT_ITEMS | type: leaf`

- $.message.order.items[*].price.value must be present in the payload

> **Skip if:**
>
>     - $.message.order.items[*].price.value is not in the payload

**REQUIRED_ITEM_PRICE_CURRENCY**
`group: ON_INIT_ITEMS | type: leaf`

- All elements of $.message.order.items[*].price.currency must be in ["INR"]

> **Skip if:**
>
>     - $.message.order.items[*].price.currency is not in the payload

**REQUIRED_LOAN_INFO_TAG_GROUP**
`group: ON_INIT_ITEMS | type: leaf`

- At least one of $.message.order.items[*].tags[*].descriptor.code must be in ["LOAN_INFO", "CONTACT_INFO", "LSP_INFO", "GENERAL_INFO"]

---

## ON_INIT_QUOTE

This is a group of **6** sub-validation(s) that all must pass: REQUIRED_QUOTE_ID, REQUIRED_QUOTE_PRICE, REQUIRED_QUOTE_PRICE_CURRENCY, REQUIRED_QUOTE_TTL, VALID_QUOTE_TTL_REGEX, and REQUIRED_QUOTE_BREAKUP. It validates the `$.message.order.items[*].tags[?(@.descriptor.code=='PERSONAL_LOAN')]` path in the payload.

---

**REQUIRED_QUOTE_ID**
`group: ON_INIT_QUOTE | type: leaf`

- $.message.order.quote.id must be present in the payload

**REQUIRED_QUOTE_PRICE**
`group: ON_INIT_QUOTE | type: leaf`

- $.message.order.quote.price.value must be present in the payload

**REQUIRED_QUOTE_PRICE_CURRENCY**
`group: ON_INIT_QUOTE | type: leaf`

- All elements of $.message.order.quote.price.currency must be in ["INR"]

**REQUIRED_QUOTE_TTL**
`group: ON_INIT_QUOTE | type: leaf`

- $.message.order.quote.ttl must be present in the payload

**VALID_QUOTE_TTL_REGEX**
`group: ON_INIT_QUOTE | type: leaf`

- All elements of $.message.order.quote.ttl must follow every regex in ["^P(?:(\\d+Y)?(\\d+M)?(\\d+D)?(T(\\d+H)?(\\d+M)?(\\d+S)?)?|T\\d+D)$"]

**REQUIRED_QUOTE_BREAKUP**
`group: ON_INIT_QUOTE | type: leaf`

- At least one of $.message.order.quote.breakup[*].title must be in ["PRINCIPAL", "INTEREST", "PROCESSING_FEE", "OTHER_UPFRONT_CHARGES", "INSURANCE_CHARGES", "NET_DISBURSED_AMOUNT", "OTHER_CHARGES"]

---

## ON_INIT_PAYMENTS

This is a group of **2** sub-validation(s) that all must pass: REQUIRED_PAYMENT_TYPE and VALID_PAYMENT_TYPE_ENUM. It validates the `$.message.order.items[*].tags[?(@.descriptor.code=='PERSONAL_LOAN')]` path in the payload.

---

**REQUIRED_PAYMENT_TYPE**
`group: ON_INIT_PAYMENTS | type: leaf`

- $.message.order.payments[*].type must be present in the payload

**VALID_PAYMENT_TYPE_ENUM**
`group: ON_INIT_PAYMENTS | type: leaf`

- All elements of $.message.order.payments[*].type must be in ["ON_ORDER", "ON_FULFILLMENT", "POST_FULFILLMENT"]

---

## ON_INIT_PAYMENTS_ON_ORDER

This group contains **2** sub-group(s)/validation(s): REQUIRED_PAYMENT_COLLECTED_BY and REQUIRED_PAYMENT_TAGS. It validates the `$.message.order.payments[?(@.type=='ON_ORDER')]` path in the payload.

---

**REQUIRED_PAYMENT_COLLECTED_BY**
`group: ON_INIT_PAYMENTS_ON_ORDER | type: leaf`

- $.message.order.payments[?(@.type=='ON_ORDER')].collected_by must be present in the payload

### REQUIRED_PAYMENT_TAGS

This is a group of **2** sub-validation(s) that all must pass: REQUIRED_BUYER_FINDER_FEES_TAG and REQUIRED_SETTLEMENT_TERMS_TAG.

---

**REQUIRED_BUYER_FINDER_FEES_TAG**
`group: ON_INIT_PAYMENTS_ON_ORDER > REQUIRED_PAYMENT_TAGS | type: leaf`

- At least one of $.message.order.payments[?(@.type=='ON_ORDER')].tags[*].descriptor.code must be in ["BUYER_FINDER_FEES", "SETTLEMENT_TERMS"]

**REQUIRED_SETTLEMENT_TERMS_TAG**
`group: ON_INIT_PAYMENTS_ON_ORDER > REQUIRED_PAYMENT_TAGS | type: leaf`

- At least one of $.message.order.payments[?(@.type=='ON_ORDER')].tags[*].descriptor.code must be in ["SETTLEMENT_TERMS"]

---

## ON_INIT_FULFILLMENTS

This is a group of **3** sub-validation(s) that all must pass: REQUIRED_FULFILLMENT_TYPE, REQUIRED_FULFILLMENT_CUSTOMER_PERSON_NAME, and REQUIRED_FULFILLMENT_STATE_CODE.

---

**REQUIRED_FULFILLMENT_TYPE**
`group: ON_INIT_FULFILLMENTS | type: leaf`

- All elements of $.message.order.fulfillments[*].type must be in ["LOAN"]

> **Skip if:**
>
>     - $.message.order.fulfillments[*].type is not in the payload

**REQUIRED_FULFILLMENT_CUSTOMER_PERSON_NAME**
`group: ON_INIT_FULFILLMENTS | type: leaf`

- $.message.order.fulfillments[*].customer.person.name must be present in the payload

**REQUIRED_FULFILLMENT_STATE_CODE**
`group: ON_INIT_FULFILLMENTS | type: leaf`

- $.message.order.fulfillments[*].state.descriptor.code must be present in the payload

---

## ON_INIT_XINPUT_PERSONAL_LOAN

This group contains **3** sub-group(s)/validation(s): REQUIRED_XINPUT_HEAD_INDEX, REQUIRED_XINPUT_HEAD_DESCRIPTOR_NAME, and REQUIRED_XINPUT_HEAD_HEADINGS.

> **Skip if:**
> **Any of these must be true:**
>   - None of $.message.order.items[*].descriptor.code may be in ["PERSONAL_LOAN"]
>   - $.message.order.items[*].xinput.form.id must **not** be present in the payload

---

### REQUIRED_XINPUT_HEAD_INDEX

This is a group of **3** sub-validation(s) that all must pass: REQUIRED_XINPUT_HEAD_INDEX_MIN, REQUIRED_XINPUT_HEAD_INDEX_CUR, and REQUIRED_XINPUT_HEAD_INDEX_MAX.

---

**REQUIRED_XINPUT_HEAD_INDEX_MIN**
`group: ON_INIT_XINPUT_PERSONAL_LOAN > REQUIRED_XINPUT_HEAD_INDEX | type: leaf`

- $.message.order.items[*].xinput.head.index.min must be present in the payload

**REQUIRED_XINPUT_HEAD_INDEX_CUR**
`group: ON_INIT_XINPUT_PERSONAL_LOAN > REQUIRED_XINPUT_HEAD_INDEX | type: leaf`

- $.message.order.items[*].xinput.head.index.cur must be present in the payload

**REQUIRED_XINPUT_HEAD_INDEX_MAX**
`group: ON_INIT_XINPUT_PERSONAL_LOAN > REQUIRED_XINPUT_HEAD_INDEX | type: leaf`

- $.message.order.items[*].xinput.head.index.max must be present in the payload

**REQUIRED_XINPUT_HEAD_DESCRIPTOR_NAME**
`group: ON_INIT_XINPUT_PERSONAL_LOAN | type: leaf`

- $.message.order.items[*].xinput.head.descriptor.name must be present in the payload

**REQUIRED_XINPUT_HEAD_HEADINGS**
`group: ON_INIT_XINPUT_PERSONAL_LOAN | type: leaf`

- $.message.order.items[*].xinput.head.headings[*] must be present in the payload
