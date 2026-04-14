---
action: select
codeName: L1validations
numTests: 39
generated: 2026-04-14
domain: ONDC:FIS12
version: 2.3.0
---

# L1validations — `select` Validations

These are the validation rules applied when processing the `select` API call in the L1validations flow.
There are **39** validation rules organized into **4** top-level group(s).

---
## SELECT_CONTEXT

This group contains **3** sub-group(s)/validation(s): CONTEXT_REQUIRED, CONTEXT_ENUM, and CONTEXT_REGEX.

---

### CONTEXT_REQUIRED

This is a group of **12** sub-validation(s) that all must pass: REQUIRED_CONTEXT_LOCATION_COUNTRY_CODE, REQUIRED_CONTEXT_LOCATION_CITY_CODE, REQUIRED_CONTEXT_DOMAIN, REQUIRED_CONTEXT_TIMESTAMP, REQUIRED_CONTEXT_BAP_ID, REQUIRED_CONTEXT_BAP_URI, REQUIRED_CONTEXT_TRANSACTION_ID, REQUIRED_CONTEXT_MESSAGE_ID, REQUIRED_CONTEXT_VERSION, REQUIRED_CONTEXT_TTL, REQUIRED_CONTEXT_BPP_ID, and REQUIRED_CONTEXT_BPP_URI.

---

**REQUIRED_CONTEXT_LOCATION_COUNTRY_CODE**
`group: SELECT_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.location.country.code must be present in the payload

**REQUIRED_CONTEXT_LOCATION_CITY_CODE**
`group: SELECT_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.location.city.code must be present in the payload

**REQUIRED_CONTEXT_DOMAIN**
`group: SELECT_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.domain must be present in the payload

**REQUIRED_CONTEXT_TIMESTAMP**
`group: SELECT_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.timestamp must be present in the payload

**REQUIRED_CONTEXT_BAP_ID**
`group: SELECT_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.bap_id must be present in the payload

**REQUIRED_CONTEXT_BAP_URI**
`group: SELECT_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.bap_uri must be present in the payload

**REQUIRED_CONTEXT_TRANSACTION_ID**
`group: SELECT_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.transaction_id must be present in the payload

**REQUIRED_CONTEXT_MESSAGE_ID**
`group: SELECT_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.message_id must be present in the payload

**REQUIRED_CONTEXT_VERSION**
`group: SELECT_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.version must be present in the payload

**REQUIRED_CONTEXT_TTL**
`group: SELECT_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.ttl must be present in the payload

**REQUIRED_CONTEXT_BPP_ID**
`group: SELECT_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.bpp_id must be present in the payload

**REQUIRED_CONTEXT_BPP_URI**
`group: SELECT_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.bpp_uri must be present in the payload

### CONTEXT_ENUM

This is a group of **2** sub-validation(s) that all must pass: VALID_CONTEXT_LOCATION_COUNTRY_CODE and VALID_CONTEXT_DOMAIN.

---

**VALID_CONTEXT_LOCATION_COUNTRY_CODE**
`group: SELECT_CONTEXT > CONTEXT_ENUM | type: leaf`

- All elements of $.context.location.country.code must be in ["IND"]

> **Skip if:**
>
>     - $.context.location.country.code is not in the payload

**VALID_CONTEXT_DOMAIN**
`group: SELECT_CONTEXT > CONTEXT_ENUM | type: leaf`

- All elements of $.context.domain must be in ["ONDC:FIS12"]

> **Skip if:**
>
>     - $.context.domain is not in the payload

### CONTEXT_REGEX

This is a group of **7** sub-validation(s) that all must pass: REGEX_CONTEXT_LOCATION_CITY_CODE, REGEX_CONTEXT_TIMESTAMP_1, REGEX_CONTEXT_BAP_ID, REGEX_CONTEXT_BAP_URI, REQUIRED_CONTEXT_TTL, REGEX_CONTEXT_BPP_ID, and REGEX_CONTEXT_BPP_URI.

---

**REGEX_CONTEXT_LOCATION_CITY_CODE**
`group: SELECT_CONTEXT > CONTEXT_REGEX | type: leaf`

- All elements of $.context.location.city.code must follow every regex in ["(\\*)|(^std\\:[0-9]{2,4}$)"]

> **Skip if:**
>
>     - $.context.location.city.code is not in the payload

**REGEX_CONTEXT_TIMESTAMP_1**
`group: SELECT_CONTEXT > CONTEXT_REGEX | type: leaf`

- All elements of $.context.timestamp must follow every regex in ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[+-]\\d{2}:\\d{2})$"]

> **Skip if:**
>
>     - $.context.timestamp is not in the payload

**REGEX_CONTEXT_BAP_ID**
`group: SELECT_CONTEXT > CONTEXT_REGEX | type: leaf`

- All elements of $.context.bap_id must follow every regex in ["^(?!.*\b(?:http|https|www)\b)[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)+$"]

> **Skip if:**
>
>     - $.context.bap_id is not in the payload

**REGEX_CONTEXT_BAP_URI**
`group: SELECT_CONTEXT > CONTEXT_REGEX | type: leaf`

- All elements of $.context.bap_uri must follow every regex in ["^https:\/\/(www\.)?[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)+(/)?$"]

> **Skip if:**
>
>     - $.context.bap_uri is not in the payload

**REQUIRED_CONTEXT_TTL**
`group: SELECT_CONTEXT > CONTEXT_REGEX | type: leaf`

- All elements of $.context.ttl must follow every regex in ["^P(?=\\d|T\\d)(\\d+Y)?(\\d+M)?(\\d+D)?(T(\\d+H)?(\\d+M)?(\\d+S)?)?$"]

> **Skip if:**
>
>     - $.context.ttl is not in the payload

**REGEX_CONTEXT_BPP_ID**
`group: SELECT_CONTEXT > CONTEXT_REGEX | type: leaf`

- All elements of $.context.bpp_id must follow every regex in ["^(?!.*\b(?:http|https|www)\b)[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)+$"]

> **Skip if:**
>
>     - $.context.bpp_id is not in the payload

**REGEX_CONTEXT_BPP_URI**
`group: SELECT_CONTEXT > CONTEXT_REGEX | type: leaf`

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

This group contains **4** sub-group(s)/validation(s): REQUIRED_ITEM_ID, REQUIRED_PARENT_ITEM_ID, REQUIRED_XINPUT_ITEMS, and VALID_TAGS.

---

**REQUIRED_ITEM_ID**
`group: REQUIRED_ITEM_FIELDS | type: leaf`

- $.message.order.items[*].id must be present in the payload

**REQUIRED_PARENT_ITEM_ID**
`group: REQUIRED_ITEM_FIELDS | type: leaf`

- $.message.order.items[*].parent_item_id must be present in the payload

### REQUIRED_XINPUT_ITEMS

This group contains **3** sub-group(s)/validation(s): SET_LOAN_AMOUNT_FORM, REQUIRED_FORM_SUBMISSION_ID, and BUSINESS_KYC_FORM.

> **Skip if:**
> - $.message.order.items[*].xinput.form.id must **not** be present in the payload

---

#### SET_LOAN_AMOUNT_FORM

This is a group of **1** sub-validation(s) that all must pass: REQUIRED_REQUEST_AMOUNT.

> **Skip if:**
> - $.message.order.items[*].xinput.head.descriptor.code must **not** equal ["SET_LOAN_AMOUNT"]

---

**REQUIRED_REQUEST_AMOUNT**
`group: REQUIRED_ITEM_FIELDS > REQUIRED_XINPUT_ITEMS > SET_LOAN_AMOUNT_FORM | type: leaf`

- $.message.order.items[*].xinput.form.data.requestAmount.value must be present in the payload

**REQUIRED_FORM_SUBMISSION_ID**
`group: REQUIRED_ITEM_FIELDS > REQUIRED_XINPUT_ITEMS | type: leaf`

- $.message.order.items[*].xinput.form_response.submission_id must be present in the payload

> **Skip if:**
>
>     - not all elements of $.message.order.items[*].xinput.head.descriptor.code are in ["INDIVIDUAL_KYC", "MANUAL_VERIFICATION"]

#### BUSINESS_KYC_FORM

This is a group of **4** sub-validation(s) that all must pass: REQUIRED_COMPANY_PAN, REQUIRED_GST_CERTIFICATE, REQUIRED_BUSINESS_PROOF, and REQUIRED_APPLICATION_FORM.

> **Skip if:**
> - $.message.order.items[*].xinput.head.descriptor.code must **not** equal ["BUSINESS_KYC"]

---

**REQUIRED_COMPANY_PAN**
`group: REQUIRED_ITEM_FIELDS > REQUIRED_XINPUT_ITEMS > BUSINESS_KYC_FORM | type: leaf`

- $.message.order.items[*].xinput.form.data.companyPan.value must be present in the payload

**REQUIRED_GST_CERTIFICATE**
`group: REQUIRED_ITEM_FIELDS > REQUIRED_XINPUT_ITEMS > BUSINESS_KYC_FORM | type: leaf`

- $.message.order.items[*].xinput.form.data.gstCertificate.value must be present in the payload

**REQUIRED_BUSINESS_PROOF**
`group: REQUIRED_ITEM_FIELDS > REQUIRED_XINPUT_ITEMS > BUSINESS_KYC_FORM | type: leaf`

- $.message.order.items[*].xinput.form.data.businessProof.value must be present in the payload

**REQUIRED_APPLICATION_FORM**
`group: REQUIRED_ITEM_FIELDS > REQUIRED_XINPUT_ITEMS > BUSINESS_KYC_FORM | type: leaf`

- $.message.order.items[*].xinput.form.data.applicationForm.value must be present in the payload

### VALID_TAGS

This is a group of **2** sub-validation(s) that all must pass: VALID_ITEM_TAGS and VALID_PLEDGE_TAGS.

> **Skip if:**
> - $.message.order.items[*].tags[*].descriptor.code must **not** be present in the payload

---

**VALID_ITEM_TAGS**
`group: REQUIRED_ITEM_FIELDS > VALID_TAGS | type: leaf`

- All elements of $.message.order.items[*].tags[*].descriptor.code must be in ["PLEDGE_REQUIREMENTS"]

> **Skip if:**
>
>     - $.message.order.items[*].tags[*].descriptor.code is not in the payload

**VALID_PLEDGE_TAGS**
`group: REQUIRED_ITEM_FIELDS > VALID_TAGS | type: leaf | scope: $.message.order.items[*].tags[?(@.descriptor.code == 'PLEDGE_REQUIREMENTS')]`

- All elements of $.message.order.items[*].tags[?(@.descriptor.code == 'PLEDGE_REQUIREMENTS')].list[*].descriptor.code must be in ["SCHEME_CODE", "UNITS_PLEDGED"]

---

## REQUIRED_FULFILMENT_ITEMS

This group contains **2** sub-group(s)/validation(s): REQUIRED_FULFILLMENT_ID and REQUIRED_CUSTOMER_ITEMS.

---

**REQUIRED_FULFILLMENT_ID**
`group: REQUIRED_FULFILMENT_ITEMS | type: leaf`

- $.message.order.fulfillments[*].id must be present in the payload

### REQUIRED_CUSTOMER_ITEMS

This group contains **5** sub-group(s)/validation(s): REQUIRED_CUSTOMER_DOB, REQUIRED_CUSTOMER_GENDER, REQUIRED_CREDS, REQUIRED_CUSTOMER_CONTACT_EMAIL, and REQUIRED_CUSTOMER_CONTACT_PHONE.

> **Skip if:**
> - $.message.order.fulfillments[*].customer.person.name must **not** be present in the payload

---

**REQUIRED_CUSTOMER_DOB**
`group: REQUIRED_FULFILMENT_ITEMS > REQUIRED_CUSTOMER_ITEMS | type: leaf`

- $._EXTERNAL._SELF.message.order.fulfillments[*].customer.person.name must be present in the payload

**REQUIRED_CUSTOMER_GENDER**
`group: REQUIRED_FULFILMENT_ITEMS > REQUIRED_CUSTOMER_ITEMS | type: leaf`

- $._EXTERNAL._SELF.message.order.fulfillments[*].customer.person.name must be present in the payload

#### REQUIRED_CREDS

This is a group of **2** sub-validation(s) that all must pass: REQUIRED_CUSTOMER_CREDS_ID and REQUIRED_CUSTOMER_CREDS_TYPE.

> **Skip if:**
> - $.message.order.fulfillments[*].customer.person.creds[*].id must **not** be present in the payload

---

**REQUIRED_CUSTOMER_CREDS_ID**
`group: REQUIRED_FULFILMENT_ITEMS > REQUIRED_CUSTOMER_ITEMS > REQUIRED_CREDS | type: leaf`

- $._EXTERNAL._SELF.message.order.fulfillments[*].customer.person.creds[*].id must be present in the payload

**REQUIRED_CUSTOMER_CREDS_TYPE**
`group: REQUIRED_FULFILMENT_ITEMS > REQUIRED_CUSTOMER_ITEMS > REQUIRED_CREDS | type: leaf`

- $._EXTERNAL._SELF.message.order.fulfillments[*].customer.person.creds[*].id must be present in the payload

**REQUIRED_CUSTOMER_CONTACT_EMAIL**
`group: REQUIRED_FULFILMENT_ITEMS > REQUIRED_CUSTOMER_ITEMS | type: leaf`

- $._EXTERNAL._SELF.message.order.fulfillments[*].customer.person.name must be present in the payload

**REQUIRED_CUSTOMER_CONTACT_PHONE**
`group: REQUIRED_FULFILMENT_ITEMS > REQUIRED_CUSTOMER_ITEMS | type: leaf`

- $._EXTERNAL._SELF.message.order.fulfillments[*].customer.person.name must be present in the payload
