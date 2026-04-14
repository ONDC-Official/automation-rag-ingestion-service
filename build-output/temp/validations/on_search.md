---
action: on_search
codeName: L1validations
numTests: 115
generated: 2026-04-14
domain: ONDC:FIS12
version: 2.3.0
---

# L1validations — `on_search` Validations

These are the validation rules applied when processing the `on_search` API call in the L1validations flow.
There are **115** validation rules organized into **10** top-level group(s).

---
## ON_SEARCH_CONTEXT

This group contains **3** sub-group(s)/validation(s): CONTEXT_REQUIRED, CONTEXT_ENUM, and CONTEXT_REGEX.

---

### CONTEXT_REQUIRED

This is a group of **12** sub-validation(s) that all must pass: REQUIRED_CONTEXT_LOCATION_COUNTRY_CODE, REQUIRED_CONTEXT_LOCATION_CITY_CODE, REQUIRED_CONTEXT_DOMAIN, REQUIRED_CONTEXT_TIMESTAMP, REQUIRED_CONTEXT_BAP_ID, REQUIRED_CONTEXT_BAP_URI, REQUIRED_CONTEXT_TRANSACTION_ID, REQUIRED_CONTEXT_MESSAGE_ID, REQUIRED_CONTEXT_VERSION, REQUIRED_CONTEXT_TTL, REQUIRED_CONTEXT_BPP_ID, and REQUIRED_CONTEXT_BPP_URI.

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

**REQUIRED_CONTEXT_BPP_ID**
`group: ON_SEARCH_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.bpp_id must be present in the payload

**REQUIRED_CONTEXT_BPP_URI**
`group: ON_SEARCH_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.bpp_uri must be present in the payload

### CONTEXT_ENUM

This is a group of **2** sub-validation(s) that all must pass: VALID_CONTEXT_LOCATION_COUNTRY_CODE and VALID_CONTEXT_DOMAIN.

---

**VALID_CONTEXT_LOCATION_COUNTRY_CODE**
`group: ON_SEARCH_CONTEXT > CONTEXT_ENUM | type: leaf`

- All elements of $.context.location.country.code must be in ["IND"]

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

This is a group of **7** sub-validation(s) that all must pass: REGEX_CONTEXT_LOCATION_CITY_CODE, REGEX_CONTEXT_TIMESTAMP_1, REGEX_CONTEXT_BAP_ID, REGEX_CONTEXT_BAP_URI, REQUIRED_CONTEXT_TTL, REGEX_CONTEXT_BPP_ID, and REGEX_CONTEXT_BPP_URI.

---

**REGEX_CONTEXT_LOCATION_CITY_CODE**
`group: ON_SEARCH_CONTEXT > CONTEXT_REGEX | type: leaf`

- All elements of $.context.location.city.code must follow every regex in ["(\\*)|(^std\\:[0-9]{2,4}$)"]

> **Skip if:**
>
>     - $.context.location.city.code is not in the payload

**REGEX_CONTEXT_TIMESTAMP_1**
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

- All elements of $.context.bap_uri must follow every regex in ["^https:\/\/(www\.)?[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)+(/)?$"]

> **Skip if:**
>
>     - $.context.bap_uri is not in the payload

**REQUIRED_CONTEXT_TTL**
`group: ON_SEARCH_CONTEXT > CONTEXT_REGEX | type: leaf`

- All elements of $.context.ttl must follow every regex in ["^P(?=\\d|T\\d)(\\d+Y)?(\\d+M)?(\\d+D)?(T(\\d+H)?(\\d+M)?(\\d+S)?)?$"]

> **Skip if:**
>
>     - $.context.ttl is not in the payload

**REGEX_CONTEXT_BPP_ID**
`group: ON_SEARCH_CONTEXT > CONTEXT_REGEX | type: leaf`

- All elements of $.context.bpp_id must follow every regex in ["^(?!.*\b(?:http|https|www)\b)[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)+$"]

> **Skip if:**
>
>     - $.context.bpp_id is not in the payload

**REGEX_CONTEXT_BPP_URI**
`group: ON_SEARCH_CONTEXT > CONTEXT_REGEX | type: leaf`

- All elements of $.context.bpp_uri must follow every regex in ["^https:\/\/(www\.)?[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)+(/)?$"]

> **Skip if:**
>
>     - $.context.bpp_uri is not in the payload

---

## ON_SEARCH_CATALOG_NAME

`group: top-level | type: leaf`

- $.message.catalog.descriptor.name must be present in the payload

---

## ON_SEARCH_PROVIDER

This is a group of **4** sub-validation(s) that all must pass: ON_SEARCH_PROVIDER_ID, ON_SEARCH_PROVIDER_NAME, ON_SEARCH_PROVIDER_IMAGES_URL, and ON_SEARCH_PROVIDER_IMAGES_SIZE_TYPE.

---

**ON_SEARCH_PROVIDER_ID**
`group: ON_SEARCH_PROVIDER | type: leaf`

- $.message.catalog.providers[*].id must be present in the payload

**ON_SEARCH_PROVIDER_NAME**
`group: ON_SEARCH_PROVIDER | type: leaf`

- $.message.catalog.providers[*].descriptor.name must be present in the payload

**ON_SEARCH_PROVIDER_IMAGES_URL**
`group: ON_SEARCH_PROVIDER | type: leaf`

- $.message.catalog.providers[*].descriptor.images[*].url must be present in the payload

**ON_SEARCH_PROVIDER_IMAGES_SIZE_TYPE**
`group: ON_SEARCH_PROVIDER | type: leaf`

- $.message.catalog.providers[*].descriptor.images[*].size_type must be present in the payload

---

## ON_SEARCH_CATEGORIES

This is a group of **5** sub-validation(s) that all must pass: ON_SEARCH_CATEGORIES_NAME, ON_SEARCH_CATEGORIES_CODE, ON_SEARCH_CATEGORIES_ID, ON_SEARCH_CATEGORIES_PARENT_ID, and VALID_ENUM_CATEGORY_CODE.

> **Skip if:**
> - $.message.catalog.providers[*].categories[*].id must **not** be present in the payload

---

**ON_SEARCH_CATEGORIES_NAME**
`group: ON_SEARCH_CATEGORIES | type: leaf`

- $.message.catalog.providers[*].categories[*].descriptor.name must be present in the payload

**ON_SEARCH_CATEGORIES_CODE**
`group: ON_SEARCH_CATEGORIES | type: leaf`

- $.message.catalog.providers[*].categories[*].descriptor.code must be present in the payload

**ON_SEARCH_CATEGORIES_ID**
`group: ON_SEARCH_CATEGORIES | type: leaf`

- $.message.catalog.providers[*].categories[*].id must be present in the payload

**ON_SEARCH_CATEGORIES_PARENT_ID**
`group: ON_SEARCH_CATEGORIES | type: leaf`

- $.message.catalog.providers[*].categories[*].parent_category_id must be present in the payload

> **Skip if:**
>
>     - any of $.message.catalog.providers[*].categories[*].descriptor.code are in ["LOAN"]

**VALID_ENUM_CATEGORY_CODE**
`group: ON_SEARCH_CATEGORIES | type: leaf`

- All elements of $.message.catalog.providers[*].categories[*].descriptor.code must be in ["LOAN", "UNSECURED_PERSONAL", "SECURED_PERSONAL", "OFFERS", "ADDITIONAL_DATA", "PERSONAL_FINANCING", "CONSUMER_INVOICE_FINANCING", "AGRI_PURCHASE_FINANCE", "ELECTRONICS_PURCHASE_FINANCE", "BUSINESS", "SOLE_PROPRIETORSHIP", "OTHER", "PARTNERSHIP_FIRM", "PRIVATE_LTD", "INVOICE_FINANCING", "GOLD_LOAN", "LAMF", "TERM_LOAN", "CREDIT_LINE", "DOCUMENT_BASED_DRAWDOWN", "NON_DOCUMENT_BASED_DRAWDOWN", "BANKING", "STATEMENT_UPLOAD", "AA_BANKING", "GST", "AA_GST", "GSP", "RETURN_UPLOAD", "MUTUAL_FUND", "AA_LOAN", "MFC", "ITR", "UPLOAD", "BUREAU_LOAN", "DERIVED_DATA", "ADDITIONAL_UPLOAD", "RTA"]

> **Skip if:**
>
>     - $.message.catalog.providers[*].categories[*].descriptor.code is not in the payload

---

## ON_SEARCH_ITEMS

This group contains **2** sub-group(s)/validation(s): REQUIRED_ITEMS and VALID_ENUM_ITEMS.

---

### REQUIRED_ITEMS

This group contains **6** sub-group(s)/validation(s): REQUIRED_ITEM_ID, REQUIRED_ITEM_CODE, REQUIRED_ITEM_CATEGORY_ID, CHECK_CATEGORY_ID, REQUIRED_ITEM_FULFILLMENT_ID, and REQUIRED_XINPUT_FIELDS.

---

**REQUIRED_ITEM_ID**
`group: ON_SEARCH_ITEMS > REQUIRED_ITEMS | type: leaf`

- $.message.catalog.providers[*].items[*].id must be present in the payload

**REQUIRED_ITEM_CODE**
`group: ON_SEARCH_ITEMS > REQUIRED_ITEMS | type: leaf`

- $.message.catalog.providers[*].items[*].descriptor.code must be present in the payload

**REQUIRED_ITEM_CATEGORY_ID**
`group: ON_SEARCH_ITEMS > REQUIRED_ITEMS | type: leaf`

- $.message.catalog.providers[*].items[*].category_ids[*] must be present in the payload

**CHECK_CATEGORY_ID**
`group: ON_SEARCH_ITEMS > REQUIRED_ITEMS | type: leaf`

- At least one of $.message.catalog.providers[*].items[*].category_ids[*] must be in $.message.catalog.providers[*].categories[*].id

> **Skip if:**
>
>     - $.message.catalog.providers[*].categories[*].id is not in the payload

**REQUIRED_ITEM_FULFILLMENT_ID**
`group: ON_SEARCH_ITEMS > REQUIRED_ITEMS | type: leaf`

- $.message.catalog.providers[*].items[*].fulfillment_ids[*] must be present in the payload

#### REQUIRED_XINPUT_FIELDS

This group contains **14** sub-group(s)/validation(s): REQUIRED_HEAD_CODE, REQUIRED_HEAD_NAME, REQUIRED_FORM_HEADINGS, REQUIRED_FORM_ID, REQUIRED_FORM_MIME_TYPE, PERSONAL_LOAN_FIELDS, REQUIRED_CONSENT_FIELDS, INVOICE_LOAN_FIELDS, GOLD_LOAN_FIELDS, WORKING_CAPITAL_LOAN_FIELDS, BUSINESS_AND_FINANCIAL_DOCUMENTS_FIELDS, TERM_LOAN_FIELDS, TERM_LOAN_FIELDS_GST, and LAMF_FIELDS.

> **Skip if:**
> **All of the following must be true:**
>   - $.message.catalog.providers[*].items[*].tags[*].descriptor.code must **not** be present in the payload
>   - Not all elements of $.message.catalog.providers[*].items[*].tags[*].descriptor.code may be in ["LOAN_INFO"]

---

**REQUIRED_HEAD_CODE**
`group: ON_SEARCH_ITEMS > REQUIRED_ITEMS > REQUIRED_XINPUT_FIELDS | type: leaf`

- $.message.catalog.providers[*].items[*].xinput.head.descriptor.code must be present in the payload

**REQUIRED_HEAD_NAME**
`group: ON_SEARCH_ITEMS > REQUIRED_ITEMS > REQUIRED_XINPUT_FIELDS | type: leaf`

- $.message.catalog.providers[*].items[*].xinput.head.descriptor.name must be present in the payload

**REQUIRED_FORM_HEADINGS**
`group: ON_SEARCH_ITEMS > REQUIRED_ITEMS > REQUIRED_XINPUT_FIELDS | type: leaf`

- $.message.catalog.providers[*].items[*].xinput.head.headings[*] must be present in the payload

**REQUIRED_FORM_ID**
`group: ON_SEARCH_ITEMS > REQUIRED_ITEMS > REQUIRED_XINPUT_FIELDS | type: leaf`

- $.message.catalog.providers[*].items[*].xinput.form.id must be present in the payload

**REQUIRED_FORM_MIME_TYPE**
`group: ON_SEARCH_ITEMS > REQUIRED_ITEMS > REQUIRED_XINPUT_FIELDS | type: leaf`

- $.message.catalog.providers[*].items[*].xinput.form.mime_type must be present in the payload

##### PERSONAL_LOAN_FIELDS

This is a group of **9** sub-validation(s) that all must pass: REQUIRED_FIELD_PAN_NAME, REQUIRED_FIELD_DOB, REQUIRED_FIELD_GENDER, REQUIRED_FIELD_PAN, REQUIRED_FIELD_CONTACT_NUMBER, REQUIRED_FIELD_EMPLOYMENT_TYPE, REQUIRED_FIELD_INCOME, REQUIRED_FIELD_COMPANY_NAME, and REQUIRED_FIELD_BUREAU_CONSENT.

> **Skip if:**
> - Not all elements of $.message.catalog.providers[*].items[*].xinput.head.descriptor.code may be in ["PERSONAL_INFORMATION"]

---

**REQUIRED_FIELD_PAN_NAME**
`group: ON_SEARCH_ITEMS > REQUIRED_ITEMS > REQUIRED_XINPUT_FIELDS > PERSONAL_LOAN_FIELDS | type: leaf`

- $.message.catalog.providers[*].items[*].xinput.form.data.panName.type must be present in the payload

**REQUIRED_FIELD_DOB**
`group: ON_SEARCH_ITEMS > REQUIRED_ITEMS > REQUIRED_XINPUT_FIELDS > PERSONAL_LOAN_FIELDS | type: leaf`

- $.message.catalog.providers[*].items[*].xinput.form.data.dob.type must be present in the payload

**REQUIRED_FIELD_GENDER**
`group: ON_SEARCH_ITEMS > REQUIRED_ITEMS > REQUIRED_XINPUT_FIELDS > PERSONAL_LOAN_FIELDS | type: leaf`

- $.message.catalog.providers[*].items[*].xinput.form.data.gender.type must be present in the payload

**REQUIRED_FIELD_PAN**
`group: ON_SEARCH_ITEMS > REQUIRED_ITEMS > REQUIRED_XINPUT_FIELDS > PERSONAL_LOAN_FIELDS | type: leaf`

- $.message.catalog.providers[*].items[*].xinput.form.data.pan.type must be present in the payload

**REQUIRED_FIELD_CONTACT_NUMBER**
`group: ON_SEARCH_ITEMS > REQUIRED_ITEMS > REQUIRED_XINPUT_FIELDS > PERSONAL_LOAN_FIELDS | type: leaf`

- $.message.catalog.providers[*].items[*].xinput.form.data.contactNumber.type must be present in the payload

**REQUIRED_FIELD_EMPLOYMENT_TYPE**
`group: ON_SEARCH_ITEMS > REQUIRED_ITEMS > REQUIRED_XINPUT_FIELDS > PERSONAL_LOAN_FIELDS | type: leaf`

- $.message.catalog.providers[*].items[*].xinput.form.data.employmentType.type must be present in the payload

**REQUIRED_FIELD_INCOME**
`group: ON_SEARCH_ITEMS > REQUIRED_ITEMS > REQUIRED_XINPUT_FIELDS > PERSONAL_LOAN_FIELDS | type: leaf`

- $.message.catalog.providers[*].items[*].xinput.form.data.income.type must be present in the payload

**REQUIRED_FIELD_COMPANY_NAME**
`group: ON_SEARCH_ITEMS > REQUIRED_ITEMS > REQUIRED_XINPUT_FIELDS > PERSONAL_LOAN_FIELDS | type: leaf`

- $.message.catalog.providers[*].items[*].xinput.form.data.companyName.type must be present in the payload

**REQUIRED_FIELD_BUREAU_CONSENT**
`group: ON_SEARCH_ITEMS > REQUIRED_ITEMS > REQUIRED_XINPUT_FIELDS > PERSONAL_LOAN_FIELDS | type: leaf`

- $.message.catalog.providers[*].items[*].xinput.form.data.bureauConsent.type must be present in the payload

##### REQUIRED_CONSENT_FIELDS

This is a group of **1** sub-validation(s) that all must pass: REQUIRED_FIELD_CONSENT_HANDLER.

> **Skip if:**
> - None of $.message.catalog.providers[*].items[*].xinput.head.descriptor.code may be in ["CONSENT_APPROVAL"]

---

**REQUIRED_FIELD_CONSENT_HANDLER**
`group: ON_SEARCH_ITEMS > REQUIRED_ITEMS > REQUIRED_XINPUT_FIELDS > REQUIRED_CONSENT_FIELDS | type: leaf`

- $.message.catalog.providers[*].items[*].xinput.form.data.consent_handler must be present in the payload

##### INVOICE_LOAN_FIELDS

This is a group of **1** sub-validation(s) that all must pass: REQUIRED_FIELD_BUREAU_CONSENT.

> **Skip if:**
> - Not all elements of $.message.catalog.providers[*].items[*].xinput.head.descriptor.code may be in ["ORGANIZATION_INFORMATION"]

---

**REQUIRED_FIELD_BUREAU_CONSENT**
`group: ON_SEARCH_ITEMS > REQUIRED_ITEMS > REQUIRED_XINPUT_FIELDS > INVOICE_LOAN_FIELDS | type: leaf`

- $.message.catalog.providers[*].items[*].xinput.form.data.bureauConsent.type must be present in the payload

##### GOLD_LOAN_FIELDS

This group contains **10** sub-group(s)/validation(s): REQUIRED_FIELD_PAN, REQUIRED_FULL_NAME, REQUIRED_FIELD_GENDER, REQUIRED_FIELD_DOB, REQUIRED_FIELD_CONTACT_NUMBER, REQUIRED_FIELD_PINCODE, REQUIRED_FIELD_JWELLERY, REQUIRED_FIELD_PURITY, REQUIRED_FIELD_BUREAU_CONSENT, and REQUIRED_CONSENT_FIELDS.

> **Skip if:**
> - Not all elements of $.message.catalog.providers[*].items[*].xinput.head.descriptor.code may be in ["PERSONAL_INFORMATION_GOLD"]

---

**REQUIRED_FIELD_PAN**
`group: ON_SEARCH_ITEMS > REQUIRED_ITEMS > REQUIRED_XINPUT_FIELDS > GOLD_LOAN_FIELDS | type: leaf`

- $.message.catalog.providers[*].items[*].xinput.form.data.pan.type must be present in the payload

**REQUIRED_FULL_NAME**
`group: ON_SEARCH_ITEMS > REQUIRED_ITEMS > REQUIRED_XINPUT_FIELDS > GOLD_LOAN_FIELDS | type: leaf`

- $.message.catalog.providers[*].items[*].xinput.form.data.fullName.type must be present in the payload

**REQUIRED_FIELD_GENDER**
`group: ON_SEARCH_ITEMS > REQUIRED_ITEMS > REQUIRED_XINPUT_FIELDS > GOLD_LOAN_FIELDS | type: leaf`

- $.message.catalog.providers[*].items[*].xinput.form.data.gender.type must be present in the payload

**REQUIRED_FIELD_DOB**
`group: ON_SEARCH_ITEMS > REQUIRED_ITEMS > REQUIRED_XINPUT_FIELDS > GOLD_LOAN_FIELDS | type: leaf`

- $.message.catalog.providers[*].items[*].xinput.form.data.dob.type must be present in the payload

**REQUIRED_FIELD_CONTACT_NUMBER**
`group: ON_SEARCH_ITEMS > REQUIRED_ITEMS > REQUIRED_XINPUT_FIELDS > GOLD_LOAN_FIELDS | type: leaf`

- $.message.catalog.providers[*].items[*].xinput.form.data.contactNumber.type must be present in the payload

**REQUIRED_FIELD_PINCODE**
`group: ON_SEARCH_ITEMS > REQUIRED_ITEMS > REQUIRED_XINPUT_FIELDS > GOLD_LOAN_FIELDS | type: leaf`

- $.message.catalog.providers[*].items[*].xinput.form.data.pincode.type must be present in the payload

**REQUIRED_FIELD_JWELLERY**
`group: ON_SEARCH_ITEMS > REQUIRED_ITEMS > REQUIRED_XINPUT_FIELDS > GOLD_LOAN_FIELDS | type: leaf`

- $.message.catalog.providers[*].items[*].xinput.form.data.jewellery.type must be present in the payload

**REQUIRED_FIELD_PURITY**
`group: ON_SEARCH_ITEMS > REQUIRED_ITEMS > REQUIRED_XINPUT_FIELDS > GOLD_LOAN_FIELDS | type: leaf`

- $.message.catalog.providers[*].items[*].xinput.form.data.purity.type must be present in the payload

**REQUIRED_FIELD_BUREAU_CONSENT**
`group: ON_SEARCH_ITEMS > REQUIRED_ITEMS > REQUIRED_XINPUT_FIELDS > GOLD_LOAN_FIELDS | type: leaf`

- $.message.catalog.providers[*].items[*].xinput.form.data.bureauConsent.type must be present in the payload

###### REQUIRED_CONSENT_FIELDS

This is a group of **1** sub-validation(s) that all must pass: REQUIRED_FIELD_AA_ID.

> **Skip if:**
> - None of $.message.order.items[*].xinput.head.descriptor.code may be in ["CONSENT_APPROVAL"]

---

**REQUIRED_FIELD_AA_ID**
`group: ON_SEARCH_ITEMS > REQUIRED_ITEMS > REQUIRED_XINPUT_FIELDS > GOLD_LOAN_FIELDS > REQUIRED_CONSENT_FIELDS | type: leaf`

- $._EXTERNAL._SELF.message.catalog.providers[*].items[*].xinput.form.data.bureauConsent.type must be present in the payload

##### WORKING_CAPITAL_LOAN_FIELDS

This is a group of **8** sub-validation(s) that all must pass: REQUIRED_FIELD_GSTIN_PROFILE_1, REQUIRED_FIELD_GSTR_B2B_INVOICE_1, REQUIRED_FIELD_GSTR_B2B_CDNR_1, REQUIRED_FIELD_GSTR_B2B_INVOICES_1, REQUIRED_FIELD_GSTR_3B_SUMMARY_1, REQUIRED_FIELD_BANK_STATEMENT_FILES, REQUIRED_FIELD_BANK_NAME, and REQUIRED_FIELD_MIME_TYPE.

> **Skip if:**
> - Not all elements of $.message.catalog.providers[*].items[*].xinput.head.descriptor.code may be in ["BANK_STATEMENT_AND_GST_RETURNS"]

---

**REQUIRED_FIELD_GSTIN_PROFILE_1**
`group: ON_SEARCH_ITEMS > REQUIRED_ITEMS > REQUIRED_XINPUT_FIELDS > WORKING_CAPITAL_LOAN_FIELDS | type: leaf`

- $.message.catalog.providers[*].items[*].xinput.form.data.gstinProfile_1.type must be present in the payload

**REQUIRED_FIELD_GSTR_B2B_INVOICE_1**
`group: ON_SEARCH_ITEMS > REQUIRED_ITEMS > REQUIRED_XINPUT_FIELDS > WORKING_CAPITAL_LOAN_FIELDS | type: leaf`

- $.message.catalog.providers[*].items[*].xinput.form.data.gstr1B2bInvoice_1.type must be present in the payload

**REQUIRED_FIELD_GSTR_B2B_CDNR_1**
`group: ON_SEARCH_ITEMS > REQUIRED_ITEMS > REQUIRED_XINPUT_FIELDS > WORKING_CAPITAL_LOAN_FIELDS | type: leaf`

- $.message.catalog.providers[*].items[*].xinput.form.data.gstr1B2bCdnr_1.type must be present in the payload

**REQUIRED_FIELD_GSTR_B2B_INVOICES_1**
`group: ON_SEARCH_ITEMS > REQUIRED_ITEMS > REQUIRED_XINPUT_FIELDS > WORKING_CAPITAL_LOAN_FIELDS | type: leaf`

- $.message.catalog.providers[*].items[*].xinput.form.data.gstr2aB2bInvoices_1.type must be present in the payload

**REQUIRED_FIELD_GSTR_3B_SUMMARY_1**
`group: ON_SEARCH_ITEMS > REQUIRED_ITEMS > REQUIRED_XINPUT_FIELDS > WORKING_CAPITAL_LOAN_FIELDS | type: leaf`

- $.message.catalog.providers[*].items[*].xinput.form.data.gstr3bSummary_1.type must be present in the payload

**REQUIRED_FIELD_BANK_STATEMENT_FILES**
`group: ON_SEARCH_ITEMS > REQUIRED_ITEMS > REQUIRED_XINPUT_FIELDS > WORKING_CAPITAL_LOAN_FIELDS | type: leaf`

- $.message.catalog.providers[*].items[*].xinput.form.data.bankStatementFiles_1.type must be present in the payload

**REQUIRED_FIELD_BANK_NAME**
`group: ON_SEARCH_ITEMS > REQUIRED_ITEMS > REQUIRED_XINPUT_FIELDS > WORKING_CAPITAL_LOAN_FIELDS | type: leaf`

- $.message.catalog.providers[*].items[*].xinput.form.data.bankName_1.type must be present in the payload

**REQUIRED_FIELD_MIME_TYPE**
`group: ON_SEARCH_ITEMS > REQUIRED_ITEMS > REQUIRED_XINPUT_FIELDS > WORKING_CAPITAL_LOAN_FIELDS | type: leaf`

- $.message.catalog.providers[*].items[*].xinput.form.data.mimeType_1.type must be present in the payload

##### BUSINESS_AND_FINANCIAL_DOCUMENTS_FIELDS

This is a group of **3** sub-validation(s) that all must pass: REQUIRED_FIELD_FINANCIAL_STATEMENTS, REQUIRED_FIELD_SHAREHOLDING_PATTERN, and REQUIRED_FIELD_ITR.

> **Skip if:**
> - Not all elements of $.message.catalog.providers[*].items[*].xinput.head.descriptor.code may be in ["BUSINESS_AND_FINANCIAL_DOCUMENTS"]

---

**REQUIRED_FIELD_FINANCIAL_STATEMENTS**
`group: ON_SEARCH_ITEMS > REQUIRED_ITEMS > REQUIRED_XINPUT_FIELDS > BUSINESS_AND_FINANCIAL_DOCUMENTS_FIELDS | type: leaf`

- $.message.catalog.providers[*].items[*].xinput.form.data.financialStatements.type must be present in the payload

**REQUIRED_FIELD_SHAREHOLDING_PATTERN**
`group: ON_SEARCH_ITEMS > REQUIRED_ITEMS > REQUIRED_XINPUT_FIELDS > BUSINESS_AND_FINANCIAL_DOCUMENTS_FIELDS | type: leaf`

- $.message.catalog.providers[*].items[*].xinput.form.data.shareholdingPattern.type must be present in the payload

**REQUIRED_FIELD_ITR**
`group: ON_SEARCH_ITEMS > REQUIRED_ITEMS > REQUIRED_XINPUT_FIELDS > BUSINESS_AND_FINANCIAL_DOCUMENTS_FIELDS | type: leaf`

- $.message.catalog.providers[*].items[*].xinput.form.data.itr.type must be present in the payload

##### TERM_LOAN_FIELDS

This is a group of **9** sub-validation(s) that all must pass: REQUIRED_FIELD_PAN, REQUIRED_FULL_NAME, REQUIRED_DOB, REQUIRED_CONSTITUTION, REQUIRED_BUSINESS_PAN, REQUIRED_DOI, REQUIRED_NATURE_OF_BUSINESS, REQUIRED_ANNUAL_TURNOVER, and REQUIRED_BUSINESS_PINCODE.

> **Skip if:**
> - Not all elements of $.message.catalog.providers[*].items[*].xinput.head.descriptor.code may be in ["PERSONAL_INFORMATION_TERM"]

---

**REQUIRED_FIELD_PAN**
`group: ON_SEARCH_ITEMS > REQUIRED_ITEMS > REQUIRED_XINPUT_FIELDS > TERM_LOAN_FIELDS | type: leaf`

- $.message.catalog.providers[*].items[*].xinput.form.data.pan.type must be present in the payload

**REQUIRED_FULL_NAME**
`group: ON_SEARCH_ITEMS > REQUIRED_ITEMS > REQUIRED_XINPUT_FIELDS > TERM_LOAN_FIELDS | type: leaf`

- $.message.catalog.providers[*].items[*].xinput.form.data.fullName.type must be present in the payload

**REQUIRED_DOB**
`group: ON_SEARCH_ITEMS > REQUIRED_ITEMS > REQUIRED_XINPUT_FIELDS > TERM_LOAN_FIELDS | type: leaf`

- $.message.catalog.providers[*].items[*].xinput.form.data.dob.type must be present in the payload

**REQUIRED_CONSTITUTION**
`group: ON_SEARCH_ITEMS > REQUIRED_ITEMS > REQUIRED_XINPUT_FIELDS > TERM_LOAN_FIELDS | type: leaf`

- $.message.catalog.providers[*].items[*].xinput.form.data.constitution.type must be present in the payload

**REQUIRED_BUSINESS_PAN**
`group: ON_SEARCH_ITEMS > REQUIRED_ITEMS > REQUIRED_XINPUT_FIELDS > TERM_LOAN_FIELDS | type: leaf`

- $.message.catalog.providers[*].items[*].xinput.form.data.businessPan.type must be present in the payload

**REQUIRED_DOI**
`group: ON_SEARCH_ITEMS > REQUIRED_ITEMS > REQUIRED_XINPUT_FIELDS > TERM_LOAN_FIELDS | type: leaf`

- $.message.catalog.providers[*].items[*].xinput.form.data.doi.type must be present in the payload

**REQUIRED_NATURE_OF_BUSINESS**
`group: ON_SEARCH_ITEMS > REQUIRED_ITEMS > REQUIRED_XINPUT_FIELDS > TERM_LOAN_FIELDS | type: leaf`

- $.message.catalog.providers[*].items[*].xinput.form.data.natureOfBusiness.type must be present in the payload

**REQUIRED_ANNUAL_TURNOVER**
`group: ON_SEARCH_ITEMS > REQUIRED_ITEMS > REQUIRED_XINPUT_FIELDS > TERM_LOAN_FIELDS | type: leaf`

- $.message.catalog.providers[*].items[*].xinput.form.data.annualTurnover.type must be present in the payload

**REQUIRED_BUSINESS_PINCODE**
`group: ON_SEARCH_ITEMS > REQUIRED_ITEMS > REQUIRED_XINPUT_FIELDS > TERM_LOAN_FIELDS | type: leaf`

- $.message.catalog.providers[*].items[*].xinput.form.data.businessPincode.type must be present in the payload

##### TERM_LOAN_FIELDS_GST

This is a group of **1** sub-validation(s) that all must pass: REQUIRED_FIELD_BUREAU_CONSENT.

> **Skip if:**
> - Not all elements of $.message.catalog.providers[*].items[*].xinput.head.descriptor.code may be in ["PERSONAL_INFORMATION_TERM_GST"]

---

**REQUIRED_FIELD_BUREAU_CONSENT**
`group: ON_SEARCH_ITEMS > REQUIRED_ITEMS > REQUIRED_XINPUT_FIELDS > TERM_LOAN_FIELDS_GST | type: leaf`

- $.message.catalog.providers[*].items[*].xinput.form.data.bureauConsent.type must be present in the payload

##### LAMF_FIELDS

This is a group of **9** sub-validation(s) that all must pass: REQUIRED_FIELD_PAN, REQUIRED_FIELD_FULL_NAME, REQUIRED_FIELD_CONSTITUION, REQUIRED_FIELD_GENDER, REQUIRED_FIELD_EMPLOYMENT_TYPE, REQUIRED_FIELD_DOB, REQUIRED_FIELD_ANNUAL_INCOME, REQUIRED_FIELD_MOBILE_NUMBER, and REQUIRED_FIELD_EMAIL_ID.

> **Skip if:**
> - Not all elements of $.message.catalog.providers[*].items[*].xinput.head.descriptor.code may be in ["PERSONAL_INFORMATION_LAMF"]

---

**REQUIRED_FIELD_PAN**
`group: ON_SEARCH_ITEMS > REQUIRED_ITEMS > REQUIRED_XINPUT_FIELDS > LAMF_FIELDS | type: leaf`

- $.message.catalog.providers[*].items[*].xinput.form.data.pan.type must be present in the payload

**REQUIRED_FIELD_FULL_NAME**
`group: ON_SEARCH_ITEMS > REQUIRED_ITEMS > REQUIRED_XINPUT_FIELDS > LAMF_FIELDS | type: leaf`

- $.message.catalog.providers[*].items[*].xinput.form.data.fullName.type must be present in the payload

**REQUIRED_FIELD_CONSTITUION**
`group: ON_SEARCH_ITEMS > REQUIRED_ITEMS > REQUIRED_XINPUT_FIELDS > LAMF_FIELDS | type: leaf`

- $.message.catalog.providers[*].items[*].xinput.form.data.constitution.type must be present in the payload

**REQUIRED_FIELD_GENDER**
`group: ON_SEARCH_ITEMS > REQUIRED_ITEMS > REQUIRED_XINPUT_FIELDS > LAMF_FIELDS | type: leaf`

- $.message.catalog.providers[*].items[*].xinput.form.data.gender.type must be present in the payload

**REQUIRED_FIELD_EMPLOYMENT_TYPE**
`group: ON_SEARCH_ITEMS > REQUIRED_ITEMS > REQUIRED_XINPUT_FIELDS > LAMF_FIELDS | type: leaf`

- $.message.catalog.providers[*].items[*].xinput.form.data.employmentType.type must be present in the payload

**REQUIRED_FIELD_DOB**
`group: ON_SEARCH_ITEMS > REQUIRED_ITEMS > REQUIRED_XINPUT_FIELDS > LAMF_FIELDS | type: leaf`

- $.message.catalog.providers[*].items[*].xinput.form.data.dob.type must be present in the payload

**REQUIRED_FIELD_ANNUAL_INCOME**
`group: ON_SEARCH_ITEMS > REQUIRED_ITEMS > REQUIRED_XINPUT_FIELDS > LAMF_FIELDS | type: leaf`

- $.message.catalog.providers[*].items[*].xinput.form.data.annualIncome.type must be present in the payload

**REQUIRED_FIELD_MOBILE_NUMBER**
`group: ON_SEARCH_ITEMS > REQUIRED_ITEMS > REQUIRED_XINPUT_FIELDS > LAMF_FIELDS | type: leaf`

- $.message.catalog.providers[*].items[*].xinput.form.data.mobileNumber.type must be present in the payload

**REQUIRED_FIELD_EMAIL_ID**
`group: ON_SEARCH_ITEMS > REQUIRED_ITEMS > REQUIRED_XINPUT_FIELDS > LAMF_FIELDS | type: leaf`

- $.message.catalog.providers[*].items[*].xinput.form.data.emailId.type must be present in the payload

### VALID_ENUM_ITEMS

This is a group of **2** sub-validation(s) that all must pass: VALID_ITEM_CODE and VALID_HEAD_CODE.

---

**VALID_ITEM_CODE**
`group: ON_SEARCH_ITEMS > VALID_ENUM_ITEMS | type: leaf`

- All elements of $.message.catalog.providers[*].items[*].descriptor.code must be in ["LOAN"]

> **Skip if:**
>
>     - $.message.catalog.providers[*].items[*].descriptor.code is not in the payload

**VALID_HEAD_CODE**
`group: ON_SEARCH_ITEMS > VALID_ENUM_ITEMS | type: leaf`

- All elements of $.message.catalog.providers[*].items[*].xinput.head.descriptor.code must be in ["PERSONAL_INFORMATION", "CONSENT_APPROVAL", "ORGANIZATION_INFORMATION", "MERCHANT_AND_PRDOUCT_DETAILS", "BANK_STATEMENT_AND_GST_RETURNS", "BUSINESS_AND_FINANCIAL_DOCUMENTS", "ORGANIZATION_INFORMATION", "PERSONAL_INFORMATION_TERM", "PERSONAL_INFORMATION_GOLD", "PERSONAL_INFORMATION_TERM_GST", "PERSONAL_INFORMATION_BUSINESS_TERM", "PERSONAL_INFORMATION_LAMF", "PERSONAL_INFORMATION_BUSINESS_TERM_GST"]

> **Skip if:**
>
>     - $.message.catalog.providers[*].items[*].xinput.head.descriptor.code is not in the payload

---

## ON_SEARCH_FULFILLMENTS

This group contains **3** sub-group(s)/validation(s): REQUIRED_FULFILLMENT_ITEMS, VALID_FULFILLMENT_ITEMS, and VALID_FULFILLMENT_TAGS.

---

### REQUIRED_FULFILLMENT_ITEMS

This is a group of **2** sub-validation(s) that all must pass: REQUIRED_FULFILLMENT_ID and REQUIRED_FULFILLMENT_TYPE.

---

**REQUIRED_FULFILLMENT_ID**
`group: ON_SEARCH_FULFILLMENTS > REQUIRED_FULFILLMENT_ITEMS | type: leaf`

- $.message.catalog.providers[*].fulfillments[*].id must be present in the payload

**REQUIRED_FULFILLMENT_TYPE**
`group: ON_SEARCH_FULFILLMENTS > REQUIRED_FULFILLMENT_ITEMS | type: leaf`

- $.message.catalog.providers[*].fulfillments[*].type must be present in the payload

### VALID_FULFILLMENT_ITEMS

This is a group of **1** sub-validation(s) that all must pass: VALID_FULFILLMENT_TYPE.

---

**VALID_FULFILLMENT_TYPE**
`group: ON_SEARCH_FULFILLMENTS > VALID_FULFILLMENT_ITEMS | type: leaf`

- All elements of $.message.catalog.providers[*].fulfillments[*].type must be in ["ONLINE", "SEMI_ONLINE", "BASE_ORDER"]

> **Skip if:**
>
>     - $.message.catalog.providers[*].fulfillments[*].type is not in the payload

### VALID_FULFILLMENT_TAGS

This is a group of **2** sub-validation(s) that all must pass: REQUIRED_FULFILLMENT_TAGS and REQUIRED_CHECKLISTS_ITEM. It validates the `$.message.catalog.providers[*].fulfillments[*][?(@.type != 'BASE_ORDER')]` path in the payload.

---

**REQUIRED_FULFILLMENT_TAGS**
`group: ON_SEARCH_FULFILLMENTS > VALID_FULFILLMENT_TAGS | type: leaf`

- All elements of $.message.catalog.providers[*].fulfillments[*].tags[*].descriptor.code must be in ["CHECKLISTS"]

> **Skip if:**
>
>     - $.message.catalog.providers[*].fulfillments[*].tags[*].descriptor.code is not in the payload

**REQUIRED_CHECKLISTS_ITEM**
`group: ON_SEARCH_FULFILLMENTS > VALID_FULFILLMENT_TAGS | type: leaf | scope: $.message.catalog.providers[*].fulfillments[*].tags[?(@.descriptor.code == 'CHECKLISTS')]`

- All elements of $.message.catalog.providers[*].fulfillments[*].tags[?(@.descriptor.code == 'CHECKLISTS')].list[*].descriptor.code must be in ["PERSONAL_INFORMATION", "CONSENT_APPROVAL", "SET_LOAN_AMOUNT", "KYC", "KYC_OFFLINE", "EMANDATE", "LOAN_AGREEMENT", "ACCOUNT_MONITORING", "ORGANIZATION_INFORMATION", "INDIVIDUAL_KYC", "ENTITY_KYC", "MERCHANT_AND_PRDOUCT_DETAILS", "SET_DOWN_PAYMENT", "ESIGN", "BANK_STATEMENT_AND_GST_RETURNS", "BUSINESS_AND_FINANCIAL_DOCUMENTS", "BUSINESS_KYC", "PERSONAL_DISCUSSION", "PHYSICAL_VERIFICATION", "ENACH", "PROCESSING_FEE", "MANUAL_VERIFICATION", "LIEN_MARKING", "PERSONAL_INFORMATION_TERM", "PERSONAL_INFORMATION_LAMF", "PERSONAL_INFORMATION_TERM_GST", "KYC_OFFLINE", "JOURNEY_OFFLINE", "PERSONAL_INFORMATION_BUSINESS_TERM_GST", "PERSONAL_INFORMATION_BUSINESS_TERM", "INVOICE_UPLOAD"]

---

## ON_SEARCH_PAYMENTS

This group contains **2** sub-group(s)/validation(s): REQUIRED_PAYMENT_ITEMS and VALID_PAYMENT_ITEMS.

---

### REQUIRED_PAYMENT_ITEMS

This is a group of **5** sub-validation(s) that all must pass: REQUIRED_PAYMENT_TYPE, REQUIRED_PAYMENT_ID, REQUIRED_PAYMENT_STATUS, REQUIRED_PAYMENT_COLLECTED_BY, and REQUIRED_PAYMENT_TIME_LABEL.

---

**REQUIRED_PAYMENT_TYPE**
`group: ON_SEARCH_PAYMENTS > REQUIRED_PAYMENT_ITEMS | type: leaf`

- $.message.catalog.providers[*].payments[*].type must be present in the payload

**REQUIRED_PAYMENT_ID**
`group: ON_SEARCH_PAYMENTS > REQUIRED_PAYMENT_ITEMS | type: leaf`

- $.message.catalog.providers[*].payments[*].id must be present in the payload

**REQUIRED_PAYMENT_STATUS**
`group: ON_SEARCH_PAYMENTS > REQUIRED_PAYMENT_ITEMS | type: leaf`

- $.message.catalog.providers[*].payments[*].status must be present in the payload

**REQUIRED_PAYMENT_COLLECTED_BY**
`group: ON_SEARCH_PAYMENTS > REQUIRED_PAYMENT_ITEMS | type: leaf`

- $.message.catalog.providers[*].payments[*].collected_by must be present in the payload

**REQUIRED_PAYMENT_TIME_LABEL**
`group: ON_SEARCH_PAYMENTS > REQUIRED_PAYMENT_ITEMS | type: leaf`

- $.message.catalog.providers[*].payments[*].time.label must be present in the payload

### VALID_PAYMENT_ITEMS

This is a group of **4** sub-validation(s) that all must pass: VALID_PAYMENT_TYPE, VALID_PAYMENT_STATUS, VALID_PAYMENT_COLLECTOR, and VALID_PAYMENT_LABEL.

---

**VALID_PAYMENT_TYPE**
`group: ON_SEARCH_PAYMENTS > VALID_PAYMENT_ITEMS | type: leaf`

- All elements of $.message.catalog.providers[*].payments[*].type must be in ["ON_ORDER", "ON_FULFILLMENT", "POST_FULFILLMENT", "PRE_ORDER"]

> **Skip if:**
>
>     - $.message.catalog.providers[*].payments[*].type is not in the payload

**VALID_PAYMENT_STATUS**
`group: ON_SEARCH_PAYMENTS > VALID_PAYMENT_ITEMS | type: leaf`

- All elements of $.message.catalog.providers[*].payments[*].status must be in ["NOT-PAID", "PAID", "DEFERRED", "DELAYED"]

> **Skip if:**
>
>     - $.message.catalog.providers[*].payments[*].status is not in the payload

**VALID_PAYMENT_COLLECTOR**
`group: ON_SEARCH_PAYMENTS > VALID_PAYMENT_ITEMS | type: leaf`

- All elements of $.message.catalog.providers[*].payments[*].collected_by must be in ["BPP", "CONSUMER", "BAP"]

> **Skip if:**
>
>     - $.message.catalog.providers[*].payments[*].collected_by is not in the payload

**VALID_PAYMENT_LABEL**
`group: ON_SEARCH_PAYMENTS > VALID_PAYMENT_ITEMS | type: leaf`

- All elements of ["INSTALLMENT", "LOAN_DISBURSMENT"] must be in $.message.catalog.providers[*].payments[*].time.label

> **Skip if:**
>
>     - $.message.catalog.providers[*].payments[*].time.label is not in the payload

---

## ON_SEARCH_TAGS

This is a group of **2** sub-validation(s) that all must pass: REQUIRED_PAYMENT_TAGS and REQUIRED_BPP_TERMS.

---

**REQUIRED_PAYMENT_TAGS**
`group: ON_SEARCH_TAGS | type: leaf`

- All elements of $.message.catalog.tags[*].descriptor.code must be in ["BAP_TERMS", "BPP_TERMS"]

> **Skip if:**
>
>     - $.message.catalog.tags[*].descriptor.code is not in the payload

**REQUIRED_BPP_TERMS**
`group: ON_SEARCH_TAGS | type: leaf | scope: $.message.catalog.tags[?(@.descriptor.code == 'BPP_TERMS')]`

- All elements of $.message.catalog.tags[?(@.descriptor.code == 'BPP_TERMS')].list[*].descriptor.code must be in ["STATIC_TERMS", "OFFLINE_CONTRACT"]

---

## ON_SEARCH_PROVIDER_TAGS

This is a group of **3** sub-validation(s) that all must pass: VALID_PROVODER_TAGS, REQUIRED_CONTACT_INFO, and REQUIRED_LSP_INFO.

---

**VALID_PROVODER_TAGS**
`group: ON_SEARCH_PROVIDER_TAGS | type: leaf`

- All elements of $.message.catalog.providers[*].tags[*].descriptor.code must be in ["CONTACT_INFO", "LSP_INFO"]

> **Skip if:**
>
>     - $.message.catalog.providers[*].tags[*].descriptor.code is not in the payload

**REQUIRED_CONTACT_INFO**
`group: ON_SEARCH_PROVIDER_TAGS | type: leaf | scope: $.message.catalog.providers[*].tags[?(@.descriptor.code == 'CONTACT_INFO')]`

- All elements of $.message.catalog.providers[*].tags[?(@.descriptor.code == 'CONTACT_INFO')].list[*].descriptor.code must be in ["GRO_NAME", "GRO_EMAIL", "GRO_CONTACT_NUMBER", "CUSTOMER_SUPPORT_LINK", "CUSTOMER_SUPPORT_CONTACT_NUMBER", "CUSTOMER_SUPPORT_EMAIL", "GRO_DESIGNATION", "GRO_ADDRESS"]

**REQUIRED_LSP_INFO**
`group: ON_SEARCH_PROVIDER_TAGS | type: leaf | scope: $.message.catalog.providers[*].tags[?(@.descriptor.code == 'LSP_INFO')]`

- All elements of $.message.catalog.providers[*].tags[?(@.descriptor.code == 'LSP_INFO')].list[*].descriptor.code must be in ["LSP_NAME", "LSP_EMAIL", "LSP_CONTACT_NUMBER", "LSP_ADDRESS"]

---

## ON_SEARCH_ITEM_TAGS

This is a group of **2** sub-validation(s) that all must pass: REQUIRED_LOAN_INFO_TAG_GROUP and REQUIRED_LOAN_OFFER_TAGS.

> **Skip if:**
> **All of the following must be true:**
>   - $.message.catalog.providers[*].items[*].tags[*].descriptor.code must **not** be present in the payload
>   - Not all elements of $.message.catalog.providers[*].items[*].tags[*].descriptor.code may be in ["LOAN_INFO", "LOAN_OFFER"]

---

**REQUIRED_LOAN_INFO_TAG_GROUP**
`group: ON_SEARCH_ITEM_TAGS | type: leaf | scope: $.message.catalog.providers[*].items[*].tags[?(@.descriptor.code == 'LOAN_INFO')]`

- All elements of $.message.catalog.providers[*].items[*].tags[?(@.descriptor.code == 'LOAN_INFO')].list[*].descriptor.code must be in ["INTEREST_RATE", "TERM", "INTEREST_RATE_TYPE", "APPLICATION_FEE", "FORECLOSURE_FEE", "INTEREST_RATE_CONVERSION_CHARGE", "DELAY_PENALTY_FEE", "OTHER_PENALTY_FEE", "ANNUAL_PERCENTAGE_RATE", "REPAYMENT_FREQUENCY", "NUMBER_OF_INSTALLMENTS", "TNC_LINK", "COOL_OFF_PERIOD", "INSTALLMENT_AMOUNT", "KFS_LINK", "INVOICE_NUMBER", "WORKING_CAPITAL_LIMIT", "INSURANCE_CHARGES", "RATE_ANNUALISED_PENAL_CHARGES", "KYC_MODE", "CO_APPLICANT", "MINIMUM_DOWNPAYMENT", "SUBVENTION_RATE", "SELLER_SUBVENTION_RATE"]

**REQUIRED_LOAN_OFFER_TAGS**
`group: ON_SEARCH_ITEM_TAGS | type: leaf | scope: $.message.catalog.providers[*].items[*].tags[?(@.descriptor.code == 'LOAN_OFFER')]`

- All elements of $.message.catalog.providers[*].items[*].tags[?(@.descriptor.code == 'LOAN_OFFER')].list[*].descriptor.code must be in ["PRINCIPAL_AMOUNT", "INTEREST_AMOUNT", "PROCESSING_FEE", "OTHER_UPFRONT_CHARGES", "INSURANCE_CHARGES", "NET_DISBURSED_AMOUNT", "OTHER_CHARGES", "OFFER_VALIDITY", "WORKING_CAPITAL_LIMIT", "CURRENT_UTLIZATION", "MINIMUM_DOWNPAYMENT", "SUBVENTION_RATE", "SELLER_SUBVENTION_RATE", "WORKING_CAPITAL_LIMIT", "CURRENT_UTILIZATION"]
