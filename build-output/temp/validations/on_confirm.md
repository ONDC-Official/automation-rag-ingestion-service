---
action: on_confirm
codeName: L1validations
numTests: 108
generated: 2026-04-14
domain: ONDC:FIS12
version: 2.3.0
---

# L1validations — `on_confirm` Validations

These are the validation rules applied when processing the `on_confirm` API call in the L1validations flow.
There are **108** validation rules organized into **13** top-level group(s).

---
## ON_CONFIRM_CONTEXT

This group contains **3** sub-group(s)/validation(s): CONTEXT_REQUIRED, CONTEXT_ENUM, and CONTEXT_REGEX.

---

### CONTEXT_REQUIRED

This is a group of **12** sub-validation(s) that all must pass: REQUIRED_CONTEXT_LOCATION_COUNTRY_CODE, REQUIRED_CONTEXT_LOCATION_CITY_CODE, REQUIRED_CONTEXT_DOMAIN, REQUIRED_CONTEXT_TIMESTAMP, REQUIRED_CONTEXT_BAP_ID, REQUIRED_CONTEXT_BAP_URI, REQUIRED_CONTEXT_TRANSACTION_ID, REQUIRED_CONTEXT_MESSAGE_ID, REQUIRED_CONTEXT_VERSION, REQUIRED_CONTEXT_TTL, REQUIRED_CONTEXT_BPP_ID, and REQUIRED_CONTEXT_BPP_URI.

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

**REQUIRED_CONTEXT_BPP_ID**
`group: ON_CONFIRM_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.bpp_id must be present in the payload

**REQUIRED_CONTEXT_BPP_URI**
`group: ON_CONFIRM_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.bpp_uri must be present in the payload

### CONTEXT_ENUM

This is a group of **2** sub-validation(s) that all must pass: VALID_CONTEXT_LOCATION_COUNTRY_CODE and VALID_CONTEXT_DOMAIN.

---

**VALID_CONTEXT_LOCATION_COUNTRY_CODE**
`group: ON_CONFIRM_CONTEXT > CONTEXT_ENUM | type: leaf`

- All elements of $.context.location.country.code must be in ["IND"]

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

This is a group of **7** sub-validation(s) that all must pass: REGEX_CONTEXT_LOCATION_CITY_CODE, REGEX_CONTEXT_TIMESTAMP_1, REGEX_CONTEXT_BAP_ID, REGEX_CONTEXT_BAP_URI, REQUIRED_CONTEXT_TTL, REGEX_CONTEXT_BPP_ID, and REGEX_CONTEXT_BPP_URI.

---

**REGEX_CONTEXT_LOCATION_CITY_CODE**
`group: ON_CONFIRM_CONTEXT > CONTEXT_REGEX | type: leaf`

- All elements of $.context.location.city.code must follow every regex in ["(\\*)|(^std\\:[0-9]{2,4}$)"]

> **Skip if:**
>
>     - $.context.location.city.code is not in the payload

**REGEX_CONTEXT_TIMESTAMP_1**
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

- All elements of $.context.bap_uri must follow every regex in ["^https:\/\/(www\.)?[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)+(/)?$"]

> **Skip if:**
>
>     - $.context.bap_uri is not in the payload

**REQUIRED_CONTEXT_TTL**
`group: ON_CONFIRM_CONTEXT > CONTEXT_REGEX | type: leaf`

- All elements of $.context.ttl must follow every regex in ["^P(?=\\d|T\\d)(\\d+Y)?(\\d+M)?(\\d+D)?(T(\\d+H)?(\\d+M)?(\\d+S)?)?$"]

> **Skip if:**
>
>     - $.context.ttl is not in the payload

**REGEX_CONTEXT_BPP_ID**
`group: ON_CONFIRM_CONTEXT > CONTEXT_REGEX | type: leaf`

- All elements of $.context.bpp_id must follow every regex in ["^(?!.*\b(?:http|https|www)\b)[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)+$"]

> **Skip if:**
>
>     - $.context.bpp_id is not in the payload

**REGEX_CONTEXT_BPP_URI**
`group: ON_CONFIRM_CONTEXT > CONTEXT_REGEX | type: leaf`

- All elements of $.context.bpp_uri must follow every regex in ["^https:\/\/(www\.)?[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)+(/)?$"]

> **Skip if:**
>
>     - $.context.bpp_uri is not in the payload

---

## REQUIRED_ORDER_ITEMS

This group contains **2** sub-group(s)/validation(s): REQUIRED_ITEMS and VALID_ENUM_ITEMS.

---

### REQUIRED_ITEMS

This is a group of **5** sub-validation(s) that all must pass: REQUIRED_ORDER_ID, REQUIRED_ORDER_STATUS, REQUIRED_ORDER_CREATED_AT, REQUIRED_ORDER_UPDATED_AT, and CREATED_AT_UPDATED_AT_EQUALITY.

---

**REQUIRED_ORDER_ID**
`group: REQUIRED_ORDER_ITEMS > REQUIRED_ITEMS | type: leaf`

- $.message.order.id must be present in the payload

**REQUIRED_ORDER_STATUS**
`group: REQUIRED_ORDER_ITEMS > REQUIRED_ITEMS | type: leaf`

- $.message.order.status must be present in the payload

**REQUIRED_ORDER_CREATED_AT**
`group: REQUIRED_ORDER_ITEMS > REQUIRED_ITEMS | type: leaf`

- $.message.order.created_at must be present in the payload

**REQUIRED_ORDER_UPDATED_AT**
`group: REQUIRED_ORDER_ITEMS > REQUIRED_ITEMS | type: leaf`

- $.message.order.updated_at must be present in the payload

**CREATED_AT_UPDATED_AT_EQUALITY**
`group: REQUIRED_ORDER_ITEMS > REQUIRED_ITEMS | type: leaf`

- $.message.order.created_at must equal $.message.order.updated_at

### VALID_ENUM_ITEMS

This is a group of **3** sub-validation(s) that all must pass: VALID_ENUM_ORDER_STATUS, REGEX_ON_CONFIRM_CREATED_AT, and REGEX_ON_CONFIRM_UPDATED_AT.

---

**VALID_ENUM_ORDER_STATUS**
`group: REQUIRED_ORDER_ITEMS > VALID_ENUM_ITEMS | type: leaf`

- At least one of $.message.order.status must be in ["ACTIVE", "COMPLETED", "CANCELLED"]

**REGEX_ON_CONFIRM_CREATED_AT**
`group: REQUIRED_ORDER_ITEMS > VALID_ENUM_ITEMS | type: leaf`

- All elements of $.message.order.created_at must follow every regex in ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[+-]\\d{2}:\\d{2})$"]

**REGEX_ON_CONFIRM_UPDATED_AT**
`group: REQUIRED_ORDER_ITEMS > VALID_ENUM_ITEMS | type: leaf`

- All elements of $.message.order.updated_at must follow every regex in ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[+-]\\d{2}:\\d{2})$"]

---

## ON_SELECT_PROVIDER

This is a group of **4** sub-validation(s) that all must pass: ON_SELECT_PROVIDER_ID, ON_SELECT_PROVIDER_NAME, ON_SELECT_PROVIDER_IMAGES_URL, and ON_SELECT_PROVIDER_IMAGES_SIZE_TYPE.

> **Skip if:**
> - $.message.order.provider.id must **not** be present in the payload

---

**ON_SELECT_PROVIDER_ID**
`group: ON_SELECT_PROVIDER | type: leaf`

- $.message.order.provider.id must be present in the payload

**ON_SELECT_PROVIDER_NAME**
`group: ON_SELECT_PROVIDER | type: leaf`

- $.message.order.provider.descriptor.name must be present in the payload

**ON_SELECT_PROVIDER_IMAGES_URL**
`group: ON_SELECT_PROVIDER | type: leaf`

- $.message.order.provider.descriptor.images[*].url must be present in the payload

**ON_SELECT_PROVIDER_IMAGES_SIZE_TYPE**
`group: ON_SELECT_PROVIDER | type: leaf`

- $.message.order.provider.descriptor.images[*].size_type must be present in the payload

---

## ON_SELECT_PROVIDER_TAGS

This is a group of **3** sub-validation(s) that all must pass: VALID_PROVODER_TAGS, REQUIRED_CONTACT_INFO, and REQUIRED_LSP_INFO.

---

**VALID_PROVODER_TAGS**
`group: ON_SELECT_PROVIDER_TAGS | type: leaf`

- All elements of $.message.order.provider.tags[*].descriptor.code must be in ["CONTACT_INFO", "LSP_INFO"]

> **Skip if:**
>
>     - $.message.order.provider.tags[*].descriptor.code is not in the payload

**REQUIRED_CONTACT_INFO**
`group: ON_SELECT_PROVIDER_TAGS | type: leaf | scope: $.message.order.provider.tags[?(@.descriptor.code == 'CONTACT_INFO')]`

- All elements of $.message.order.provider.tags[?(@.descriptor.code == 'CONTACT_INFO')].list[*].descriptor.code must be in ["GRO_NAME", "GRO_EMAIL", "GRO_CONTACT_NUMBER", "CUSTOMER_SUPPORT_LINK", "CUSTOMER_SUPPORT_CONTACT_NUMBER", "CUSTOMER_SUPPORT_EMAIL", "GRO_DESIGNATION", "GRO_ADDRESS"]

**REQUIRED_LSP_INFO**
`group: ON_SELECT_PROVIDER_TAGS | type: leaf | scope: $.message.order.provider.tags[?(@.descriptor.code == 'LSP_INFO')]`

- All elements of $.message.order.provider.tags[?(@.descriptor.code == 'LSP_INFO')].list[*].descriptor.code must be in ["LSP_NAME", "LSP_EMAIL", "LSP_CONTACT_NUMBER", "LSP_ADDRESS"]

---

## ON_INIT_ITEMS

This group contains **1** sub-group(s)/validation(s): REQUIRED_ITEMS.

---

### REQUIRED_ITEMS

This group contains **8** sub-group(s)/validation(s): REQUIRED_ITEM_ID, REQUIRED_PARENT_ITEM_ID, REQUIRED_ITEM_DESCRIPTOR_CODE, REQUIRED_ITEM_CATEGORY_ID, ON_SEARCH_ITEM_PRICE_CURRENCY, ON_SEARCH_ITEM_PRICE_VALUE, ON_SELECT_ITEM_FULFILLMENT_IDS, and REQUIRED_XINPUT_FIELDS.

---

**REQUIRED_ITEM_ID**
`group: ON_INIT_ITEMS > REQUIRED_ITEMS | type: leaf`

- $.message.order.items[*].id must be present in the payload

**REQUIRED_PARENT_ITEM_ID**
`group: ON_INIT_ITEMS > REQUIRED_ITEMS | type: leaf`

- $.message.order.items[*].parent_item_id must be present in the payload

**REQUIRED_ITEM_DESCRIPTOR_CODE**
`group: ON_INIT_ITEMS > REQUIRED_ITEMS | type: leaf`

- $.message.order.items[*].descriptor.code must be present in the payload

**REQUIRED_ITEM_CATEGORY_ID**
`group: ON_INIT_ITEMS > REQUIRED_ITEMS | type: leaf`

- $.message.order.items[*].category_ids[*] must be present in the payload

**ON_SEARCH_ITEM_PRICE_CURRENCY**
`group: ON_INIT_ITEMS > REQUIRED_ITEMS | type: leaf`

- $.message.order.items[*].price.currency must be present in the payload

**ON_SEARCH_ITEM_PRICE_VALUE**
`group: ON_INIT_ITEMS > REQUIRED_ITEMS | type: leaf`

- $.message.order.items[*].price.value must be present in the payload

**ON_SELECT_ITEM_FULFILLMENT_IDS**
`group: ON_INIT_ITEMS > REQUIRED_ITEMS | type: leaf`

- $.message.order.items[*].fulfillment_ids[*] must be present in the payload

#### REQUIRED_XINPUT_FIELDS

This group contains **2** sub-group(s)/validation(s): REQUIRED_XINPUT_ITEMS and VALID_XINPUT_FIELDS.

> **Skip if:**
> - $.message.order.items[*].xinput.form.id must **not** be present in the payload

---

##### REQUIRED_XINPUT_ITEMS

This group contains **7** sub-group(s)/validation(s): REQUIRED_HEAD_CODE, REQUIRED_HEAD_NAME, REQUIRED_FORM_HEADINGS, REQUIRED_FORM_ID, REQUIRED_FORM_MIME_TYPE, REQUIRED_FORM_RESPONSE, and REQUIRED_SUBMISSION_ID.

---

**REQUIRED_HEAD_CODE**
`group: ON_INIT_ITEMS > REQUIRED_ITEMS > REQUIRED_XINPUT_FIELDS > REQUIRED_XINPUT_ITEMS | type: leaf`

- $.message.order.items[*].xinput.head.descriptor.code must be present in the payload

> **Skip if:**
>
>     - $.message.order.items[*].xinput.form_response.status is in the payload

**REQUIRED_HEAD_NAME**
`group: ON_INIT_ITEMS > REQUIRED_ITEMS > REQUIRED_XINPUT_FIELDS > REQUIRED_XINPUT_ITEMS | type: leaf`

- $.message.order.items[*].xinput.head.descriptor.name must be present in the payload

> **Skip if:**
>
>     - $.message.order.items[*].xinput.form_response.status is in the payload

**REQUIRED_FORM_HEADINGS**
`group: ON_INIT_ITEMS > REQUIRED_ITEMS > REQUIRED_XINPUT_FIELDS > REQUIRED_XINPUT_ITEMS | type: leaf`

- $.message.order.items[*].xinput.head.headings[*] must be present in the payload

> **Skip if:**
>
>     - $.message.order.items[*].xinput.form_response.status is in the payload

**REQUIRED_FORM_ID**
`group: ON_INIT_ITEMS > REQUIRED_ITEMS > REQUIRED_XINPUT_FIELDS > REQUIRED_XINPUT_ITEMS | type: leaf`

- $.message.order.items[*].xinput.form.id must be present in the payload

**REQUIRED_FORM_MIME_TYPE**
`group: ON_INIT_ITEMS > REQUIRED_ITEMS > REQUIRED_XINPUT_FIELDS > REQUIRED_XINPUT_ITEMS | type: leaf`

- $.message.order.items[*].xinput.form.mime_type must be present in the payload

> **Skip if:**
>
>     - $.message.order.items[*].xinput.form_response.status is in the payload

###### REQUIRED_FORM_RESPONSE

This is a group of **2** sub-validation(s) that all must pass: REQUIRED_FORM_STATUS and REQUIRED_FORM_SUBMISSION_ID.

> **Skip if:**
> - $.message.order.items[*].xinput.form_response.status must **not** be present in the payload

---

**REQUIRED_FORM_STATUS**
`group: ON_INIT_ITEMS > REQUIRED_ITEMS > REQUIRED_XINPUT_FIELDS > REQUIRED_XINPUT_ITEMS > REQUIRED_FORM_RESPONSE | type: leaf`

- $.message.order.items[*].xinput.form_response.status must be present in the payload

**REQUIRED_FORM_SUBMISSION_ID**
`group: ON_INIT_ITEMS > REQUIRED_ITEMS > REQUIRED_XINPUT_FIELDS > REQUIRED_XINPUT_ITEMS > REQUIRED_FORM_RESPONSE | type: leaf`

- $.message.order.items[*].xinput.form_response.status must be present in the payload

**REQUIRED_SUBMISSION_ID**
`group: ON_INIT_ITEMS > REQUIRED_ITEMS > REQUIRED_XINPUT_FIELDS > REQUIRED_XINPUT_ITEMS | type: leaf`

- $.message.order.items[*].xinput.form_response.submission_id must be present in the payload

> **Skip if:**
>
>     - $.message.order.items[*].xinput.form_response.submission_id is not in the payload

##### VALID_XINPUT_FIELDS

This is a group of **1** sub-validation(s) that all must pass: VALID_FORM_HEADINGS.

---

**VALID_FORM_HEADINGS**
`group: ON_INIT_ITEMS > REQUIRED_ITEMS > REQUIRED_XINPUT_FIELDS > VALID_XINPUT_FIELDS | type: leaf`

- All elements of $.message.order.items[*].xinput.head.headings[*] must be in ["KYC", "EMANDATE", "LOAN_AGREEMENT", "INDIVIDUAL_KYC", "ENTITY_KYC", "ENACH", "ESIGN", "KYC_OFFLINE", "JOURNEY_OFFLINE", "LIEN_MARKING", "ACCOUNT_MONITORING", "INVOICE_UPLOAD"]

> **Skip if:**
>
>     - $.message.order.items[*].xinput.form_response.submission_id is in the payload

---

## ON_SELECT_ITEM_TAGS

This is a group of **2** sub-validation(s) that all must pass: REQUIRED_LOAN_INFO and REQUIRED_LOAN_OFFER.

> **Skip if:**
> **All of the following must be true:**
>   - $.message.order.items[*].tags[*].descriptor.code must **not** be present in the payload
>   - Not all elements of $.message.order.items[*].tags[*].descriptor.code may be in ["LOAN_INFO", "LOAN_OFFER"]

---

**REQUIRED_LOAN_INFO**
`group: ON_SELECT_ITEM_TAGS | type: leaf | scope: $.message.order.items[*].tags[?(@.descriptor.code == 'LOAN_INFO')]`

- All elements of $.message.order.items[*].tags[?(@.descriptor.code == 'LOAN_INFO')].list[*].descriptor.code must be in ["INTEREST_RATE", "TERM", "INTEREST_RATE_TYPE", "APPLICATION_FEE", "FORECLOSURE_FEE", "INTEREST_RATE_CONVERSION_CHARGE", "DELAY_PENALTY_FEE", "OTHER_PENALTY_FEE", "ANNUAL_PERCENTAGE_RATE", "REPAYMENT_FREQUENCY", "NUMBER_OF_INSTALLMENTS", "TNC_LINK", "COOL_OFF_PERIOD", "INSTALLMENT_AMOUNT", "KFS_LINK", "INVOICE_NUMBER", "WORKING_CAPITAL_LIMIT", "INSURANCE_CHARGES", "RATE_ANNUALISED_PENAL_CHARGES", "KYC_MODE", "CO_APPLICANT", "MINIMUM_DOWNPAYMENT", "SUBVENTION_RATE", "SELLER_SUBVENTION_RATE"]

**REQUIRED_LOAN_OFFER**
`group: ON_SELECT_ITEM_TAGS | type: leaf | scope: $.message.order.items[*].tags[?(@.descriptor.code == 'LOAN_OFFER')]`

- All elements of $.message.order.items[*].tags[?(@.descriptor.code == 'LOAN_OFFER')].list[*].descriptor.code must be in ["PRINCIPAL_AMOUNT", "INTEREST_AMOUNT", "PROCESSING_FEE", "OTHER_UPFRONT_CHARGES", "INSURANCE_CHARGES", "NET_DISBURSED_AMOUNT", "OTHER_CHARGES", "OFFER_VALIDITY", "WORKING_CAPITAL_LIMIT", "CURRENT_UTLIZATION", "MINIMUM_DOWNPAYMENT", "SUBVENTION_RATE", "SELLER_SUBVENTION_RATE", "WORKING_CAPITAL_LIMIT", "CURRENT_UTILIZATION"]

---

## ON_INIT_FULFILLMENTS

This group contains **3** sub-group(s)/validation(s): REQUIRED_FULFILLMENT_ITEMS, VALID_FULFILLMENT_ITEMS, and VALID_FULFILLMENT_TAGS.

---

### REQUIRED_FULFILLMENT_ITEMS

This group contains **6** sub-group(s)/validation(s): REQUIRED_FULFILLMENT_ID, REQUIRED_FULFILLMENT_TYPE, REQUIRED_CREDS, REQUIRED_CUSTOMER_NAME, REQUIRED_CUSTOMER_CONTACT_DETAILS, and REQUIRED_CUSTOMER_ORG_DETAILS.

---

**REQUIRED_FULFILLMENT_ID**
`group: ON_INIT_FULFILLMENTS > REQUIRED_FULFILLMENT_ITEMS | type: leaf`

- $.message.order.fulfillments[*].id must be present in the payload

**REQUIRED_FULFILLMENT_TYPE**
`group: ON_INIT_FULFILLMENTS > REQUIRED_FULFILLMENT_ITEMS | type: leaf`

- $.message.order.fulfillments[*].type must be present in the payload

#### REQUIRED_CREDS

This is a group of **2** sub-validation(s) that all must pass: REQUIRED_CUSTOMER_CREDS_ID and REQUIRED_CUSTOMER_CREDS_TYPE.

> **Skip if:**
> - $.message.order.fulfillments[*].customer.person.creds[*].id must **not** be present in the payload

---

**REQUIRED_CUSTOMER_CREDS_ID**
`group: ON_INIT_FULFILLMENTS > REQUIRED_FULFILLMENT_ITEMS > REQUIRED_CREDS | type: leaf`

- $._EXTERNAL._SELF.message.order.fulfillments[*].customer.person.creds[*].id must be present in the payload

**REQUIRED_CUSTOMER_CREDS_TYPE**
`group: ON_INIT_FULFILLMENTS > REQUIRED_FULFILLMENT_ITEMS > REQUIRED_CREDS | type: leaf`

- $._EXTERNAL._SELF.message.order.fulfillments[*].customer.person.creds[*].id must be present in the payload

**REQUIRED_CUSTOMER_NAME**
`group: ON_INIT_FULFILLMENTS > REQUIRED_FULFILLMENT_ITEMS | type: leaf`

- $.message.order.fulfillments[*].customer.person.name must be present in the payload

> **Skip if:**
>
>     - $.message.order.fulfillments[*].customer.person.name is not in the payload

#### REQUIRED_CUSTOMER_CONTACT_DETAILS

This is a group of **2** sub-validation(s) that all must pass: REQUIRED_CUSTOMER_CONTACT_NUMBER and REQUIRED_CUSTOMER_CONTACT_EMAIL.

> **Skip if:**
> - $.message.order.fulfillments[*].customer.contact.phone must **not** be present in the payload

---

**REQUIRED_CUSTOMER_CONTACT_NUMBER**
`group: ON_INIT_FULFILLMENTS > REQUIRED_FULFILLMENT_ITEMS > REQUIRED_CUSTOMER_CONTACT_DETAILS | type: leaf`

- $._EXTERNAL._SELF.message.order.fulfillments[*].customer.contact.phone must be present in the payload

**REQUIRED_CUSTOMER_CONTACT_EMAIL**
`group: ON_INIT_FULFILLMENTS > REQUIRED_FULFILLMENT_ITEMS > REQUIRED_CUSTOMER_CONTACT_DETAILS | type: leaf`

- $._EXTERNAL._SELF.message.order.fulfillments[*].customer.contact.phone must be present in the payload

#### REQUIRED_CUSTOMER_ORG_DETAILS

This is a group of **6** sub-validation(s) that all must pass: REQUIRED_ORG_ADDRESS, REQUIRED_ORG_STATE, REQUIRED_ORG_CITY, REQUIRED_ORG_CODE, REQUIRED_ORG_CONTACT_PHONE, and REQUIRED_ORG_CONTACT_EMAIL.

> **Skip if:**
> - $.message.order.fulfillments[*].customer.organization.address must **not** be present in the payload

---

**REQUIRED_ORG_ADDRESS**
`group: ON_INIT_FULFILLMENTS > REQUIRED_FULFILLMENT_ITEMS > REQUIRED_CUSTOMER_ORG_DETAILS | type: leaf`

- $._EXTERNAL._SELF.message.order.fulfillments[*].customer.organization.address must be present in the payload

**REQUIRED_ORG_STATE**
`group: ON_INIT_FULFILLMENTS > REQUIRED_FULFILLMENT_ITEMS > REQUIRED_CUSTOMER_ORG_DETAILS | type: leaf`

- $._EXTERNAL._SELF.message.order.fulfillments[*].customer.organization.address must be present in the payload

**REQUIRED_ORG_CITY**
`group: ON_INIT_FULFILLMENTS > REQUIRED_FULFILLMENT_ITEMS > REQUIRED_CUSTOMER_ORG_DETAILS | type: leaf`

- $._EXTERNAL._SELF.message.order.fulfillments[*].customer.organization.address must be present in the payload

**REQUIRED_ORG_CODE**
`group: ON_INIT_FULFILLMENTS > REQUIRED_FULFILLMENT_ITEMS > REQUIRED_CUSTOMER_ORG_DETAILS | type: leaf`

- $._EXTERNAL._SELF.message.order.fulfillments[*].customer.organization.address must be present in the payload

**REQUIRED_ORG_CONTACT_PHONE**
`group: ON_INIT_FULFILLMENTS > REQUIRED_FULFILLMENT_ITEMS > REQUIRED_CUSTOMER_ORG_DETAILS | type: leaf`

- $._EXTERNAL._SELF.message.order.fulfillments[*].customer.organization.address must be present in the payload

**REQUIRED_ORG_CONTACT_EMAIL**
`group: ON_INIT_FULFILLMENTS > REQUIRED_FULFILLMENT_ITEMS > REQUIRED_CUSTOMER_ORG_DETAILS | type: leaf`

- $._EXTERNAL._SELF.message.order.fulfillments[*].customer.organization.address must be present in the payload

### VALID_FULFILLMENT_ITEMS

This is a group of **2** sub-validation(s) that all must pass: VALID_FULFILLMENT_TYPE and VALID_FULFILLMENT_STATE_CODE.

---

**VALID_FULFILLMENT_TYPE**
`group: ON_INIT_FULFILLMENTS > VALID_FULFILLMENT_ITEMS | type: leaf`

- All elements of $.message.order.fulfillments[*].type must be in ["ONLINE", "SEMI_ONLINE", "BASE_ORDER"]

> **Skip if:**
>
>     - $.message.order.fulfillments[*].type is not in the payload

**VALID_FULFILLMENT_STATE_CODE**
`group: ON_INIT_FULFILLMENTS > VALID_FULFILLMENT_ITEMS | type: leaf`

- All elements of $.message.order.fulfillments[*].state.descriptor.code must be in ["INITIATED", "SANCTIONED", "DISBURSED", "CONSENT_REQUIRED", "DELIVERED"]

> **Skip if:**
>
>     - $.message.order.fulfillments[*].state.descriptor.code is not in the payload

### VALID_FULFILLMENT_TAGS

This is a group of **2** sub-validation(s) that all must pass: REQUIRED_FULFILLMENT_TAGS and REQUIRED_CHECKLISTS_ITEM. It validates the `$.message.order.providers[*].fulfillments[*][?(@.type != 'BASE_ORDER')]` path in the payload.

---

**REQUIRED_FULFILLMENT_TAGS**
`group: ON_INIT_FULFILLMENTS > VALID_FULFILLMENT_TAGS | type: leaf`

- All elements of $.message.order.fulfillments[*].tags[*].descriptor.code must be in ["CHECKLISTS"]

> **Skip if:**
>
>     - $.message.order.fulfillments[*].tags[*].descriptor.code is not in the payload

**REQUIRED_CHECKLISTS_ITEM**
`group: ON_INIT_FULFILLMENTS > VALID_FULFILLMENT_TAGS | type: leaf | scope: $.message.order.fulfillments[*].tags[?(@.descriptor.code == 'CHECKLISTS')]`

- All elements of $.message.order.fulfillments[*].tags[?(@.descriptor.code == 'CHECKLISTS')].list[*].descriptor.code must be in ["PERSONAL_INFORMATION", "CONSENT_APPROVAL", "SET_LOAN_AMOUNT", "KYC", "KYC_OFFLINE", "EMANDATE", "LOAN_AGREEMENT", "ACCOUNT_MONITORING", "ORGANIZATION_INFORMATION", "INDIVIDUAL_KYC", "ENTITY_KYC", "MERCHANT_AND_PRDOUCT_DETAILS", "SET_DOWN_PAYMENT", "ESIGN", "BANK_STATEMENT_AND_GST_RETURNS", "BUSINESS_AND_FINANCIAL_DOCUMENTS", "BUSINESS_KYC", "PERSONAL_DISCUSSION", "PHYSICAL_VERIFICATION", "ENACH", "PROCESSING_FEE", "MANUAL_VERIFICATION", "LIEN_MARKING", "PERSONAL_INFORMATION_TERM", "PERSONAL_INFORMATION_LAMF", "PERSONAL_INFORMATION_TERM_GST", "KYC_OFFLINE", "JOURNEY_OFFLINE", "PERSONAL_INFORMATION_BUSINESS_TERM_GST", "PERSONAL_INFORMATION_BUSINESS_TERM", "INVOICE_UPLOAD"]

---

## ON_SELECT_QUOTE

This group contains **2** sub-group(s)/validation(s): REQUIRED_COMMON_QUOTE_ITEMS and VALID_COMMON_QUOTE_ITEMS.

> **Skip if:**
> - $.message.order.quote.id must **not** be present in the payload

---

### REQUIRED_COMMON_QUOTE_ITEMS

This is a group of **7** sub-validation(s) that all must pass: REQUIRED_QUOTE_ID, REQUIRED_QUOTE_PRICE_VALUE, REQUIRED_QUOTE_PRICE_CURRENCY, REQUIRED_BREAKUP_TITLE, REQUIRED_BREAKUP_PRICE_VALUE, REQUIRED_BREAKUP_PRICE_CURRENCY, and REQUIRED_QUOTE_TTL.

---

**REQUIRED_QUOTE_ID**
`group: ON_SELECT_QUOTE > REQUIRED_COMMON_QUOTE_ITEMS | type: leaf`

- $.message.order.quote.id must be present in the payload

**REQUIRED_QUOTE_PRICE_VALUE**
`group: ON_SELECT_QUOTE > REQUIRED_COMMON_QUOTE_ITEMS | type: leaf`

- $.message.order.quote.price.value must be present in the payload

**REQUIRED_QUOTE_PRICE_CURRENCY**
`group: ON_SELECT_QUOTE > REQUIRED_COMMON_QUOTE_ITEMS | type: leaf`

- $.message.order.quote.price.currency must be present in the payload

**REQUIRED_BREAKUP_TITLE**
`group: ON_SELECT_QUOTE > REQUIRED_COMMON_QUOTE_ITEMS | type: leaf`

- $.message.order.quote.breakup[*].title must be present in the payload

**REQUIRED_BREAKUP_PRICE_VALUE**
`group: ON_SELECT_QUOTE > REQUIRED_COMMON_QUOTE_ITEMS | type: leaf`

- $.message.order.quote.breakup[*].price.value must be present in the payload

**REQUIRED_BREAKUP_PRICE_CURRENCY**
`group: ON_SELECT_QUOTE > REQUIRED_COMMON_QUOTE_ITEMS | type: leaf`

- $.message.order.quote.breakup[*].price.currency must be present in the payload

**REQUIRED_QUOTE_TTL**
`group: ON_SELECT_QUOTE > REQUIRED_COMMON_QUOTE_ITEMS | type: leaf`

- $.message.order.quote.ttl must be present in the payload

### VALID_COMMON_QUOTE_ITEMS

This is a group of **2** sub-validation(s) that all must pass: VALID_ENUM_BREAKUP_PRICE_CURRENCY and VALID_ENUM_BREAKUP_TITLE.

---

**VALID_ENUM_BREAKUP_PRICE_CURRENCY**
`group: ON_SELECT_QUOTE > VALID_COMMON_QUOTE_ITEMS | type: leaf`

- At least one of $.message.order.quote.breakup[*].price.currency must be in ["INR"]

**VALID_ENUM_BREAKUP_TITLE**
`group: ON_SELECT_QUOTE > VALID_COMMON_QUOTE_ITEMS | type: leaf`

- At least one of $.message.order.quote.breakup[*].title must be in ["PRINCIPAL_AMOUNT", "INTEREST_AMOUNT", "PROCESSING_FEE", "OTHER_UPFRONT_CHARGES", "INSURANCE_CHARGES", "NET_DISBURSED_AMOUNT", "OTHER_CHARGES", "WORKING_CAPITAL_LIMIT", "CURRENT_UTLIZATION"]

---

## ON_INIT_PAYMENTS

This group contains **1** sub-group(s)/validation(s): REQUIRED_PAYMENT_ITEMS.

> **Skip if:**
> - $.message.order.ref_order_ids[*] must be present in the payload

---

### REQUIRED_PAYMENT_ITEMS

This group contains **10** sub-group(s)/validation(s): REQUIRED_PAYMENT_ITEMS, REQUIRED_PAYMENT_ID, REQUIRED_PAYMENT_STATUS, REQUIRED_PAYMENT_COLLECTED_BY, REQUIRED_PAYMENT_BANK_ACCOUNT_NUMBER, REQUIRED_PAYMENT_BANK_CODE, REQUIRED_PAYMENT_LABEL, REQUIRED_PARAMS_DETAILS, REQUIRED_PAYMENT_URL, and REQUIRED_TIME_RANGE.

---

**REQUIRED_PAYMENT_ITEMS**
`group: ON_INIT_PAYMENTS > REQUIRED_PAYMENT_ITEMS | type: leaf`

- $.message.order.payments[*].type must be present in the payload

**REQUIRED_PAYMENT_ID**
`group: ON_INIT_PAYMENTS > REQUIRED_PAYMENT_ITEMS | type: leaf`

- $.message.order.payments[*].id must be present in the payload

**REQUIRED_PAYMENT_STATUS**
`group: ON_INIT_PAYMENTS > REQUIRED_PAYMENT_ITEMS | type: leaf`

- $.message.order.payments[*].status must be present in the payload

**REQUIRED_PAYMENT_COLLECTED_BY**
`group: ON_INIT_PAYMENTS > REQUIRED_PAYMENT_ITEMS | type: leaf`

- $.message.order.payments[*].collected_by must be present in the payload

> **Skip if:**
>
>     - not all elements of $.message.order.payments[*].time.label are in ["LOAN_DISBURSMENT"]

#### REQUIRED_PAYMENT_BANK_ACCOUNT_NUMBER

This is a group of **1** sub-validation(s) that all must pass: REQUIRED_PAYMENT_BANK_ACCOUNT_NUMBER. It validates the `$.message.order.payments[*][?(@.time.label=='LOAN_DISBURSMENT')]` path in the payload.

---

**REQUIRED_PAYMENT_BANK_ACCOUNT_NUMBER**
`group: ON_INIT_PAYMENTS > REQUIRED_PAYMENT_ITEMS > REQUIRED_PAYMENT_BANK_ACCOUNT_NUMBER | type: leaf`

- $.message.order.payments[*].params.bank_account_number must be present in the payload

#### REQUIRED_PAYMENT_BANK_CODE

This is a group of **1** sub-validation(s) that all must pass: REQUIRED_PAYMENT_BANK_CODE. It validates the `$.message.order.payments[*][?(@.time.label=='LOAN_DISBURSMENT')]` path in the payload.

---

**REQUIRED_PAYMENT_BANK_CODE**
`group: ON_INIT_PAYMENTS > REQUIRED_PAYMENT_ITEMS > REQUIRED_PAYMENT_BANK_CODE | type: leaf`

- $.message.order.payments[*].params.bank_code must be present in the payload

**REQUIRED_PAYMENT_LABEL**
`group: ON_INIT_PAYMENTS > REQUIRED_PAYMENT_ITEMS | type: leaf`

- $.message.order.payments[*].time.label must be present in the payload

#### REQUIRED_PARAMS_DETAILS

This is a group of **3** sub-validation(s) that all must pass: REQUIRED_TRANSACTION_ID, REQUIRED_PAYMENTS_AMOUNT, and REQUIRED_PAYMENTS_CURRENCY.

> **Skip if:**
> - Not all elements of $.message.order.payments[*].status may be in ["PAID"]

---

**REQUIRED_TRANSACTION_ID**
`group: ON_INIT_PAYMENTS > REQUIRED_PAYMENT_ITEMS > REQUIRED_PARAMS_DETAILS | type: leaf`

- $.message.order.payments[*].params.transaction_id must be present in the payload

**REQUIRED_PAYMENTS_AMOUNT**
`group: ON_INIT_PAYMENTS > REQUIRED_PAYMENT_ITEMS > REQUIRED_PARAMS_DETAILS | type: leaf`

- $.message.order.payments[*].params.amount must be present in the payload

**REQUIRED_PAYMENTS_CURRENCY**
`group: ON_INIT_PAYMENTS > REQUIRED_PAYMENT_ITEMS > REQUIRED_PARAMS_DETAILS | type: leaf`

- $.message.order.payments[*].params.currency must be present in the payload

#### REQUIRED_PAYMENT_URL

This is a group of **1** sub-validation(s) that all must pass: REQUIRED_TIME_DURATION.

> **Skip if:**
> - $.message.order.payments[*].url must **not** be present in the payload

---

**REQUIRED_TIME_DURATION**
`group: ON_INIT_PAYMENTS > REQUIRED_PAYMENT_ITEMS > REQUIRED_PAYMENT_URL | type: leaf`

- $.message.order.payments[*].time.duration must be present in the payload

#### REQUIRED_TIME_RANGE

This is a group of **2** sub-validation(s) that all must pass: REQUIRED_TIME_START_RANGE and REQUIRED_TIME_END_RANGE.

> **Skip if:**
> - Not all elements of $.message.order.payments[*].time.label may be in ["INSTALLMENT"]

---

**REQUIRED_TIME_START_RANGE**
`group: ON_INIT_PAYMENTS > REQUIRED_PAYMENT_ITEMS > REQUIRED_TIME_RANGE | type: leaf`

- $.message.order.payments[*].time.range.start must be present in the payload

**REQUIRED_TIME_END_RANGE**
`group: ON_INIT_PAYMENTS > REQUIRED_PAYMENT_ITEMS > REQUIRED_TIME_RANGE | type: leaf`

- $.message.order.payments[*].time.range.end must be present in the payload

---

## ON_INIT_PAYMENT_TAGS

This is a group of **3** sub-validation(s) that all must pass: VALID_PAYMENT_TAGS, REQUIRED_ACCOUNT_DETAILS, and REQUIRED_BREAKUP_DETAILS.

---

**VALID_PAYMENT_TAGS**
`group: ON_INIT_PAYMENT_TAGS | type: leaf`

- All elements of $.message.order.payments[*].tags[*].descriptor.code must be in ["ACCOUNT_DETAILS", "BREAKUP"]

> **Skip if:**
>
>     - $.message.order.payments[*].tags[*].descriptor.code is not in the payload

**REQUIRED_ACCOUNT_DETAILS**
`group: ON_INIT_PAYMENT_TAGS | type: leaf | scope: $.message.order.payments[*].tags[?(@.descriptor.code == 'ACCOUNT_DETAILS')]`

- All elements of $.message.order.payments[*].tags[?(@.descriptor.code == 'ACCOUNT_DETAILS')].list[*].descriptor.code must be in ["ACCOUNT_TYPE", "ACCOUNT_HOLDER_NAME", "BANK_NAME"]

**REQUIRED_BREAKUP_DETAILS**
`group: ON_INIT_PAYMENT_TAGS | type: leaf | scope: $.message.order.payments[*].tags[?(@.descriptor.code == 'BREAKUP')]`

- All elements of $.message.order.payments[*].tags[?(@.descriptor.code == 'BREAKUP')].list[*].descriptor.code must be in ["PRINCIPAL_AMOUNT", "INTEREST_AMOUNT", "FORECLOSURE_CHARGES", "LATE_FEE_AMOUNT"]

---

## ON_INIT_CANCELLATION_TERMS

This group contains **2** sub-group(s)/validation(s): EXTERNAL_REF_TERMS and FULFILLMENT_STATE_TERMS.

---

### EXTERNAL_REF_TERMS

This is a group of **2** sub-validation(s) that all must pass: REQUIRED_EXTERNAL_REF_MIME_TYPE and REQUIRED_EXTERNAL_REF_URL.

> **Skip if:**
> - $.message.order.cancellation_terms[*].external_ref.mimetype must **not** be present in the payload

---

**REQUIRED_EXTERNAL_REF_MIME_TYPE**
`group: ON_INIT_CANCELLATION_TERMS > EXTERNAL_REF_TERMS | type: leaf`

- $.message.order.cancellation_terms[*].external_ref.mimetype must be present in the payload

**REQUIRED_EXTERNAL_REF_URL**
`group: ON_INIT_CANCELLATION_TERMS > EXTERNAL_REF_TERMS | type: leaf`

- $.message.order.cancellation_terms[*].external_ref.url must be present in the payload

### FULFILLMENT_STATE_TERMS

This is a group of **2** sub-validation(s) that all must pass: REQUIRED_FULFILLMENT_STATE_CODE and REQUIRED_CANCELLATION_FEE.

> **Skip if:**
> - $.message.order.cancellation_terms[*].fulfillment_state.descriptor.code must **not** be present in the payload

---

**REQUIRED_FULFILLMENT_STATE_CODE**
`group: ON_INIT_CANCELLATION_TERMS > FULFILLMENT_STATE_TERMS | type: leaf`

- $.message.order.cancellation_terms[*].fulfillment_state.descriptor.code must be present in the payload

**REQUIRED_CANCELLATION_FEE**
`group: ON_INIT_CANCELLATION_TERMS > FULFILLMENT_STATE_TERMS | type: leaf`

- $.message.order.cancellation_terms[*].cancellation_fee.percentage must be present in the payload

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

---

## REQUIRED_ORDER_DOCUMENTS

This is a group of **5** sub-validation(s) that all must pass: REQUIRED_DOCUMENT_CODE, REQUIRED_DOCUMENT_NAME, REQUIRED_DOCUMENT_TYPE, REQUIRED_DOCUMENT_URL, and VALID_DESCRIPTOR_CODE.

> **Skip if:**
> - $.message.order.ref_order_ids[*] must be present in the payload

---

**REQUIRED_DOCUMENT_CODE**
`group: REQUIRED_ORDER_DOCUMENTS | type: leaf`

- $.message.order.documents[*].descriptor.code must be present in the payload

**REQUIRED_DOCUMENT_NAME**
`group: REQUIRED_ORDER_DOCUMENTS | type: leaf`

- $.message.order.documents[*].descriptor.name must be present in the payload

**REQUIRED_DOCUMENT_TYPE**
`group: REQUIRED_ORDER_DOCUMENTS | type: leaf`

- $.message.order.documents[*].mime_type must be present in the payload

**REQUIRED_DOCUMENT_URL**
`group: REQUIRED_ORDER_DOCUMENTS | type: leaf`

- $.message.order.documents[*].url must be present in the payload

**VALID_DESCRIPTOR_CODE**
`group: REQUIRED_ORDER_DOCUMENTS | type: leaf`

- All elements of $.message.order.documents[*].descriptor.code must be in ["LOAN_AGREEMENT", "LOAN_CANCELLATION"]
