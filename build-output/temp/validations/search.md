---
action: search
codeName: L1validations
numTests: 87
generated: 2026-04-14
domain: ONDC:FIS12
version: 2.3.0
---

# L1validations — `search` Validations

These are the validation rules applied when processing the `search` API call in the L1validations flow.
There are **87** validation rules organized into **6** top-level group(s).

---
## SEARCH_CONTEXT

This group contains **3** sub-group(s)/validation(s): CONTEXT_REQUIRED, CONTEXT_ENUM, and CONTEXT_REGEX.

---

### CONTEXT_REQUIRED

This is a group of **12** sub-validation(s) that all must pass: REQUIRED_CONTEXT_LOCATION_COUNTRY_CODE, REQUIRED_CONTEXT_LOCATION_CITY_CODE, REQUIRED_CONTEXT_DOMAIN, REQUIRED_CONTEXT_TIMESTAMP, REQUIRED_CONTEXT_BAP_ID, REQUIRED_CONTEXT_BAP_URI, REQUIRED_CONTEXT_TRANSACTION_ID, REQUIRED_CONTEXT_MESSAGE_ID, REQUIRED_CONTEXT_VERSION, REQUIRED_CONTEXT_TTL, REQUIRED_CONTEXT_BPP_ID, and REQUIRED_CONTEXT_BPP_URI.

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

**REQUIRED_CONTEXT_BPP_ID**
`group: SEARCH_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.bpp_id must be present in the payload

> **Skip if:**
>
>     - $.message.intent.provider.id is not in the payload

**REQUIRED_CONTEXT_BPP_URI**
`group: SEARCH_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.bpp_uri must be present in the payload

> **Skip if:**
>
>     - $.message.intent.provider.id is not in the payload

### CONTEXT_ENUM

This is a group of **2** sub-validation(s) that all must pass: VALID_CONTEXT_LOCATION_COUNTRY_CODE and VALID_CONTEXT_DOMAIN.

---

**VALID_CONTEXT_LOCATION_COUNTRY_CODE**
`group: SEARCH_CONTEXT > CONTEXT_ENUM | type: leaf`

- All elements of $.context.location.country.code must be in ["IND"]

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

This is a group of **7** sub-validation(s) that all must pass: REGEX_CONTEXT_LOCATION_CITY_CODE, REGEX_CONTEXT_TIMESTAMP_1, REGEX_CONTEXT_BAP_ID, REGEX_CONTEXT_BAP_URI, REQUIRED_CONTEXT_TTL, REGEX_CONTEXT_BPP_ID, and REGEX_CONTEXT_BPP_URI.

---

**REGEX_CONTEXT_LOCATION_CITY_CODE**
`group: SEARCH_CONTEXT > CONTEXT_REGEX | type: leaf`

- All elements of $.context.location.city.code must follow every regex in ["(\\*)|(^std\\:[0-9]{2,4}$)"]

> **Skip if:**
>
>     - $.context.location.city.code is not in the payload

**REGEX_CONTEXT_TIMESTAMP_1**
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

- All elements of $.context.bap_uri must follow every regex in ["^https:\/\/(www\.)?[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)+(/)?$"]

> **Skip if:**
>
>     - $.context.bap_uri is not in the payload

**REQUIRED_CONTEXT_TTL**
`group: SEARCH_CONTEXT > CONTEXT_REGEX | type: leaf`

- All elements of $.context.ttl must follow every regex in ["^P(?=\\d|T\\d)(\\d+Y)?(\\d+M)?(\\d+D)?(T(\\d+H)?(\\d+M)?(\\d+S)?)?$"]

> **Skip if:**
>
>     - $.context.ttl is not in the payload

**REGEX_CONTEXT_BPP_ID**
`group: SEARCH_CONTEXT > CONTEXT_REGEX | type: leaf`

- All elements of $.context.bpp_id must follow every regex in ["^(?!.*\b(?:http|https|www)\b)[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)+$"]

> **Skip if:**
>
>     - **All of the following must be true:**
>       - $.context.bpp_id is not in the payload
>       - $.message.intent.provider.id is not in the payload

**REGEX_CONTEXT_BPP_URI**
`group: SEARCH_CONTEXT > CONTEXT_REGEX | type: leaf`

- All elements of $.context.bpp_uri must follow every regex in ["^https:\/\/(www\.)?[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)+(/)?$"]

> **Skip if:**
>
>     - **All of the following must be true:**
>       - $.context.bpp_uri is not in the payload
>       - $.message.intent.provider.id is not in the payload

---

## SEARCH_CATEGORY_CODE

This is a group of **2** sub-validation(s) that all must pass: REQUIRED_CATEGORY_CODE and VALID_ENUM_CATEGORY_CODE.

> **Skip if:**
> - $.message.intent.provider.id must be present in the payload

---

**REQUIRED_CATEGORY_CODE**
`group: SEARCH_CATEGORY_CODE | type: leaf`

- $.message.intent.category.descriptor.code must be present in the payload

**VALID_ENUM_CATEGORY_CODE**
`group: SEARCH_CATEGORY_CODE | type: leaf`

- All elements of $.message.intent.category.descriptor.code must be in ["LOAN", "UNSECURED_PERSONAL", "SECURED_PERSONAL", "OFFERS", "ADDITIONAL_DATA", "PERSONAL_FINANCING", "CONSUMER_INVOICE_FINANCING", "AGRI_PURCHASE_FINANCE", "ELECTRONICS_PURCHASE_FINANCE", "BUSINESS", "SOLE_PROPRIETORSHIP", "OTHER", "PARTNERSHIP_FIRM", "PRIVATE_LTD", "INVOICE_FINANCING", "GOLD_LOAN", "LAMF", "TERM_LOAN", "CREDIT_LINE", "DOCUMENT_BASED_DRAWDOWN", "NON_DOCUMENT_BASED_DRAWDOWN", "BANKING", "STATEMENT_UPLOAD", "AA_BANKING", "GST", "AA_GST", "GSP", "RETURN_UPLOAD", "MUTUAL_FUND", "AA_LOAN", "MFC", "ITR", "UPLOAD", "BUREAU_LOAN", "DERIVED_DATA", "ADDITIONAL_UPLOAD", "RTA"]

> **Skip if:**
>
>     - $.message.intent.category.descriptor.code is not in the payload

---

## SEARCH_ITEMS

This group contains **1** sub-group(s)/validation(s): REQUIRED_ITEM_FIELDS.

> **Skip if:**
> - $.message.intent.provider.id must **not** be present in the payload

---

### REQUIRED_ITEM_FIELDS

This group contains **4** sub-group(s)/validation(s): REQUIRED_PROVIDER_ID, REQUIRED_PROVIDER_ITEM_ID, REQUIRED_XINPUT_FIELDS, and VALID_XINPUT_ENUMS.

---

**REQUIRED_PROVIDER_ID**
`group: SEARCH_ITEMS > REQUIRED_ITEM_FIELDS | type: leaf`

- $.message.intent.provider.id must be present in the payload

**REQUIRED_PROVIDER_ITEM_ID**
`group: SEARCH_ITEMS > REQUIRED_ITEM_FIELDS | type: leaf`

- $.message.intent.provider.items[*].id must be present in the payload

#### REQUIRED_XINPUT_FIELDS

This group contains **11** sub-group(s)/validation(s): REQUIRED_HEAD_CODE, REQUIRED_FORM_ID, REQUIRED_SUBMISSION_ID, PERSONAL_LOAN_FIELDS, REQUIRED_CONSENT_FIELDS, GOLD_LOAN_FIELDS, WORKING_CAPITAL_LOAN_FIELDS, BUSINESS_AND_FINANCIAL_DOCUMENTS_FIELDS, TERM_LOAN_FIELDS, LAMF_FIELDS, and INVOICE_LOAN_FIELDS.

---

**REQUIRED_HEAD_CODE**
`group: SEARCH_ITEMS > REQUIRED_ITEM_FIELDS > REQUIRED_XINPUT_FIELDS | type: leaf`

- $.message.intent.provider.items[*].xinput.head.descriptor.code must be present in the payload

**REQUIRED_FORM_ID**
`group: SEARCH_ITEMS > REQUIRED_ITEM_FIELDS > REQUIRED_XINPUT_FIELDS | type: leaf`

- $.message.intent.provider.items[*].xinput.form.id must be present in the payload

**REQUIRED_SUBMISSION_ID**
`group: SEARCH_ITEMS > REQUIRED_ITEM_FIELDS > REQUIRED_XINPUT_FIELDS | type: leaf`

- $.message.intent.provider.items[*].xinput.form_response.submission_id must be present in the payload

> **Skip if:**
>
>     - $._EXTERNAL._SELF.message.intent.provider.id is not equal to CONSENT_APPROVAL

##### PERSONAL_LOAN_FIELDS

This is a group of **8** sub-validation(s) that all must pass: REQUIRED_FIELD_PAN_NAME_1, REQUIRED_FIELD_DOB, REQUIRED_FIELD_GENDER, REQUIRED_FIELD_PAN, REQUIRED_FIELD_CONTACT_NUMBER, REQUIRED_FIELD_INCOME, REQUIRED_FIELD_COMPANY_NAME, and REQUIRED_FIELD_BUREAU_CONSENT.

> **Skip if:**
> - Not all elements of $.message.intent.provider.items[*].xinput.head.descriptor.code may be in ["PERSONAL_INFORMATION"]

---

**REQUIRED_FIELD_PAN_NAME_1**
`group: SEARCH_ITEMS > REQUIRED_ITEM_FIELDS > REQUIRED_XINPUT_FIELDS > PERSONAL_LOAN_FIELDS | type: leaf`

- $.message.intent.provider.items[*].xinput.form.data.panName.value must be present in the payload

**REQUIRED_FIELD_DOB**
`group: SEARCH_ITEMS > REQUIRED_ITEM_FIELDS > REQUIRED_XINPUT_FIELDS > PERSONAL_LOAN_FIELDS | type: leaf`

- $.message.intent.provider.items[*].xinput.form.data.dob.value must be present in the payload

**REQUIRED_FIELD_GENDER**
`group: SEARCH_ITEMS > REQUIRED_ITEM_FIELDS > REQUIRED_XINPUT_FIELDS > PERSONAL_LOAN_FIELDS | type: leaf`

- $.message.intent.provider.items[*].xinput.form.data.gender.value must be present in the payload

**REQUIRED_FIELD_PAN**
`group: SEARCH_ITEMS > REQUIRED_ITEM_FIELDS > REQUIRED_XINPUT_FIELDS > PERSONAL_LOAN_FIELDS | type: leaf`

- $.message.intent.provider.items[*].xinput.form.data.pan.value must be present in the payload

**REQUIRED_FIELD_CONTACT_NUMBER**
`group: SEARCH_ITEMS > REQUIRED_ITEM_FIELDS > REQUIRED_XINPUT_FIELDS > PERSONAL_LOAN_FIELDS | type: leaf`

- $.message.intent.provider.items[*].xinput.form.data.contactNumber.value must be present in the payload

**REQUIRED_FIELD_INCOME**
`group: SEARCH_ITEMS > REQUIRED_ITEM_FIELDS > REQUIRED_XINPUT_FIELDS > PERSONAL_LOAN_FIELDS | type: leaf`

- $.message.intent.provider.items[*].xinput.form.data.income.value must be present in the payload

**REQUIRED_FIELD_COMPANY_NAME**
`group: SEARCH_ITEMS > REQUIRED_ITEM_FIELDS > REQUIRED_XINPUT_FIELDS > PERSONAL_LOAN_FIELDS | type: leaf`

- $.message.intent.provider.items[*].xinput.form.data.companyName.value must be present in the payload

**REQUIRED_FIELD_BUREAU_CONSENT**
`group: SEARCH_ITEMS > REQUIRED_ITEM_FIELDS > REQUIRED_XINPUT_FIELDS > PERSONAL_LOAN_FIELDS | type: leaf`

- $.message.intent.provider.items[*].xinput.form.data.bureauConsent.value must be present in the payload

##### REQUIRED_CONSENT_FIELDS

This is a group of **1** sub-validation(s) that all must pass: REQUIRED_FIELD_CONSENT_HANDLER.

> **Skip if:**
> - None of $.message.intent.provider.items[*].xinput.head.descriptor.code may be in ["CONSENT_APPROVAL"]

---

**REQUIRED_FIELD_CONSENT_HANDLER**
`group: SEARCH_ITEMS > REQUIRED_ITEM_FIELDS > REQUIRED_XINPUT_FIELDS > REQUIRED_CONSENT_FIELDS | type: leaf`

- $.message.intent.provider.items[*].xinput.form_response.submission_id must be present in the payload

##### GOLD_LOAN_FIELDS

This is a group of **9** sub-validation(s) that all must pass: REQUIRED_FIELD_PAN, REQUIRED_FULL_NAME, REQUIRED_FIELD_GENDER, REQUIRED_FIELD_DOB, REQUIRED_FIELD_CONTACT_NUMBER, REQUIRED_FIELD_PINCODE, REQUIRED_FIELD_JWELLERY, REQUIRED_FIELD_PURITY, and REQUIRED_FIELD_BUREAU_CONSENT.

> **Skip if:**
> - Not all elements of $.message.intent.provider.items[*].xinput.head.descriptor.code may be in ["PERSONAL_INFORMATION_GOLD"]

---

**REQUIRED_FIELD_PAN**
`group: SEARCH_ITEMS > REQUIRED_ITEM_FIELDS > REQUIRED_XINPUT_FIELDS > GOLD_LOAN_FIELDS | type: leaf`

- $._EXTERNAL._SELF.message.intent.provider.items[*].xinput.head.descriptor.code must be present in the payload

**REQUIRED_FULL_NAME**
`group: SEARCH_ITEMS > REQUIRED_ITEM_FIELDS > REQUIRED_XINPUT_FIELDS > GOLD_LOAN_FIELDS | type: leaf`

- $._EXTERNAL._SELF.message.intent.provider.items[*].xinput.head.descriptor.code must be present in the payload

**REQUIRED_FIELD_GENDER**
`group: SEARCH_ITEMS > REQUIRED_ITEM_FIELDS > REQUIRED_XINPUT_FIELDS > GOLD_LOAN_FIELDS | type: leaf`

- $._EXTERNAL._SELF.message.intent.provider.items[*].xinput.head.descriptor.code must be present in the payload

**REQUIRED_FIELD_DOB**
`group: SEARCH_ITEMS > REQUIRED_ITEM_FIELDS > REQUIRED_XINPUT_FIELDS > GOLD_LOAN_FIELDS | type: leaf`

- $._EXTERNAL._SELF.message.intent.provider.items[*].xinput.head.descriptor.code must be present in the payload

**REQUIRED_FIELD_CONTACT_NUMBER**
`group: SEARCH_ITEMS > REQUIRED_ITEM_FIELDS > REQUIRED_XINPUT_FIELDS > GOLD_LOAN_FIELDS | type: leaf`

- $._EXTERNAL._SELF.message.intent.provider.items[*].xinput.head.descriptor.code must be present in the payload

**REQUIRED_FIELD_PINCODE**
`group: SEARCH_ITEMS > REQUIRED_ITEM_FIELDS > REQUIRED_XINPUT_FIELDS > GOLD_LOAN_FIELDS | type: leaf`

- $._EXTERNAL._SELF.message.intent.provider.items[*].xinput.head.descriptor.code must be present in the payload

**REQUIRED_FIELD_JWELLERY**
`group: SEARCH_ITEMS > REQUIRED_ITEM_FIELDS > REQUIRED_XINPUT_FIELDS > GOLD_LOAN_FIELDS | type: leaf`

- $._EXTERNAL._SELF.message.intent.provider.items[*].xinput.head.descriptor.code must be present in the payload

**REQUIRED_FIELD_PURITY**
`group: SEARCH_ITEMS > REQUIRED_ITEM_FIELDS > REQUIRED_XINPUT_FIELDS > GOLD_LOAN_FIELDS | type: leaf`

- $._EXTERNAL._SELF.message.intent.provider.items[*].xinput.head.descriptor.code must be present in the payload

**REQUIRED_FIELD_BUREAU_CONSENT**
`group: SEARCH_ITEMS > REQUIRED_ITEM_FIELDS > REQUIRED_XINPUT_FIELDS > GOLD_LOAN_FIELDS | type: leaf`

- $._EXTERNAL._SELF.message.intent.provider.items[*].xinput.head.descriptor.code must be present in the payload

##### WORKING_CAPITAL_LOAN_FIELDS

This is a group of **8** sub-validation(s) that all must pass: REQUIRED_FIELD_GSTIN_PROFILE_1, REQUIRED_FIELD_GSTR_B2B_INVOICE_1, REQUIRED_FIELD_GSTR_B2B_CDNR_1, REQUIRED_FIELD_GSTR_B2B_INVOICES_1, REQUIRED_FIELD_GSTR_3B_SUMMARY_1, REQUIRED_FIELD_BANK_STATEMENT_FILES, REQUIRED_FIELD_BANK_NAME, and REQUIRED_FIELD_MIME_TYPE.

> **Skip if:**
> - Not all elements of $.message.intent.provider.items[*].xinput.head.descriptor.code may be in ["BANK_STATEMENT_AND_GST_RETURNS"]

---

**REQUIRED_FIELD_GSTIN_PROFILE_1**
`group: SEARCH_ITEMS > REQUIRED_ITEM_FIELDS > REQUIRED_XINPUT_FIELDS > WORKING_CAPITAL_LOAN_FIELDS | type: leaf`

- $._EXTERNAL._SELF.message.intent.provider.items[*].xinput.head.descriptor.code must be present in the payload

**REQUIRED_FIELD_GSTR_B2B_INVOICE_1**
`group: SEARCH_ITEMS > REQUIRED_ITEM_FIELDS > REQUIRED_XINPUT_FIELDS > WORKING_CAPITAL_LOAN_FIELDS | type: leaf`

- $._EXTERNAL._SELF.message.intent.provider.items[*].xinput.head.descriptor.code must be present in the payload

**REQUIRED_FIELD_GSTR_B2B_CDNR_1**
`group: SEARCH_ITEMS > REQUIRED_ITEM_FIELDS > REQUIRED_XINPUT_FIELDS > WORKING_CAPITAL_LOAN_FIELDS | type: leaf`

- $._EXTERNAL._SELF.message.intent.provider.items[*].xinput.head.descriptor.code must be present in the payload

**REQUIRED_FIELD_GSTR_B2B_INVOICES_1**
`group: SEARCH_ITEMS > REQUIRED_ITEM_FIELDS > REQUIRED_XINPUT_FIELDS > WORKING_CAPITAL_LOAN_FIELDS | type: leaf`

- $._EXTERNAL._SELF.message.intent.provider.items[*].xinput.head.descriptor.code must be present in the payload

**REQUIRED_FIELD_GSTR_3B_SUMMARY_1**
`group: SEARCH_ITEMS > REQUIRED_ITEM_FIELDS > REQUIRED_XINPUT_FIELDS > WORKING_CAPITAL_LOAN_FIELDS | type: leaf`

- $._EXTERNAL._SELF.message.intent.provider.items[*].xinput.head.descriptor.code must be present in the payload

**REQUIRED_FIELD_BANK_STATEMENT_FILES**
`group: SEARCH_ITEMS > REQUIRED_ITEM_FIELDS > REQUIRED_XINPUT_FIELDS > WORKING_CAPITAL_LOAN_FIELDS | type: leaf`

- $._EXTERNAL._SELF.message.intent.provider.items[*].xinput.head.descriptor.code must be present in the payload

**REQUIRED_FIELD_BANK_NAME**
`group: SEARCH_ITEMS > REQUIRED_ITEM_FIELDS > REQUIRED_XINPUT_FIELDS > WORKING_CAPITAL_LOAN_FIELDS | type: leaf`

- $._EXTERNAL._SELF.message.intent.provider.items[*].xinput.head.descriptor.code must be present in the payload

**REQUIRED_FIELD_MIME_TYPE**
`group: SEARCH_ITEMS > REQUIRED_ITEM_FIELDS > REQUIRED_XINPUT_FIELDS > WORKING_CAPITAL_LOAN_FIELDS | type: leaf`

- $._EXTERNAL._SELF.message.intent.provider.items[*].xinput.head.descriptor.code must be present in the payload

##### BUSINESS_AND_FINANCIAL_DOCUMENTS_FIELDS

This is a group of **3** sub-validation(s) that all must pass: REQUIRED_FIELD_FINANCIAL_STATEMENTS, REQUIRED_FIELD_SHAREHOLDING_PATTERN, and REQUIRED_FIELD_ITR.

> **Skip if:**
> - Not all elements of $.message.intent.provider.items[*].xinput.head.descriptor.code may be in ["BUSINESS_AND_FINANCIAL_DOCUMENTS"]

---

**REQUIRED_FIELD_FINANCIAL_STATEMENTS**
`group: SEARCH_ITEMS > REQUIRED_ITEM_FIELDS > REQUIRED_XINPUT_FIELDS > BUSINESS_AND_FINANCIAL_DOCUMENTS_FIELDS | type: leaf`

- $.message.intent.provider.items[*].xinput.form.data.financialStatements.value must be present in the payload

**REQUIRED_FIELD_SHAREHOLDING_PATTERN**
`group: SEARCH_ITEMS > REQUIRED_ITEM_FIELDS > REQUIRED_XINPUT_FIELDS > BUSINESS_AND_FINANCIAL_DOCUMENTS_FIELDS | type: leaf`

- $.message.intent.provider.items[*].xinput.form.data.shareholdingPattern.value must be present in the payload

**REQUIRED_FIELD_ITR**
`group: SEARCH_ITEMS > REQUIRED_ITEM_FIELDS > REQUIRED_XINPUT_FIELDS > BUSINESS_AND_FINANCIAL_DOCUMENTS_FIELDS | type: leaf`

- $.message.intent.provider.items[*].xinput.form.data.itr.value must be present in the payload

##### TERM_LOAN_FIELDS

This is a group of **9** sub-validation(s) that all must pass: REQUIRED_FIELD_PAN, REQUIRED_FULL_NAME, REQUIRED_DOB, REQUIRED_CONSTITUTION, REQUIRED_BUSINESS_PAN, REQUIRED_DOI, REQUIRED_NATURE_OF_BUSINESS, REQUIRED_ANNUAL_TURNOVER, and REQUIRED_BUSINESS_PINCODE.

> **Skip if:**
> - Not all elements of $.message.intent.provider.items[*].xinput.head.descriptor.code may be in ["PERSONAL_INFORMATION_TERM"]

---

**REQUIRED_FIELD_PAN**
`group: SEARCH_ITEMS > REQUIRED_ITEM_FIELDS > REQUIRED_XINPUT_FIELDS > TERM_LOAN_FIELDS | type: leaf`

- $.message.intent.provider.items[*].xinput.form.data.pan.value must be present in the payload

**REQUIRED_FULL_NAME**
`group: SEARCH_ITEMS > REQUIRED_ITEM_FIELDS > REQUIRED_XINPUT_FIELDS > TERM_LOAN_FIELDS | type: leaf`

- $.message.intent.provider.items[*].xinput.form.data.fullName.value must be present in the payload

**REQUIRED_DOB**
`group: SEARCH_ITEMS > REQUIRED_ITEM_FIELDS > REQUIRED_XINPUT_FIELDS > TERM_LOAN_FIELDS | type: leaf`

- $.message.intent.provider.items[*].xinput.form.data.dob.value must be present in the payload

**REQUIRED_CONSTITUTION**
`group: SEARCH_ITEMS > REQUIRED_ITEM_FIELDS > REQUIRED_XINPUT_FIELDS > TERM_LOAN_FIELDS | type: leaf`

- $.message.intent.provider.items[*].xinput.form.data.constitution.value must be present in the payload

**REQUIRED_BUSINESS_PAN**
`group: SEARCH_ITEMS > REQUIRED_ITEM_FIELDS > REQUIRED_XINPUT_FIELDS > TERM_LOAN_FIELDS | type: leaf`

- $.message.intent.provider.items[*].xinput.form.data.businessPan.value must be present in the payload

**REQUIRED_DOI**
`group: SEARCH_ITEMS > REQUIRED_ITEM_FIELDS > REQUIRED_XINPUT_FIELDS > TERM_LOAN_FIELDS | type: leaf`

- $.message.intent.provider.items[*].xinput.form.data.doi.value must be present in the payload

**REQUIRED_NATURE_OF_BUSINESS**
`group: SEARCH_ITEMS > REQUIRED_ITEM_FIELDS > REQUIRED_XINPUT_FIELDS > TERM_LOAN_FIELDS | type: leaf`

- $.message.intent.provider.items[*].xinput.form.data.natureOfBusiness.value must be present in the payload

**REQUIRED_ANNUAL_TURNOVER**
`group: SEARCH_ITEMS > REQUIRED_ITEM_FIELDS > REQUIRED_XINPUT_FIELDS > TERM_LOAN_FIELDS | type: leaf`

- $.message.intent.provider.items[*].xinput.form.data.annualTurnover.value must be present in the payload

**REQUIRED_BUSINESS_PINCODE**
`group: SEARCH_ITEMS > REQUIRED_ITEM_FIELDS > REQUIRED_XINPUT_FIELDS > TERM_LOAN_FIELDS | type: leaf`

- $.message.intent.provider.items[*].xinput.form.data.businessPincode.value must be present in the payload

##### LAMF_FIELDS

This is a group of **9** sub-validation(s) that all must pass: REQUIRED_FIELD_PAN, REQUIRED_FIELD_FULL_NAME, REQUIRED_FIELD_CONSTITUION, REQUIRED_FIELD_GENDER, REQUIRED_FIELD_EMPLOYMENT_TYPE, REQUIRED_FIELD_DOB, REQUIRED_FIELD_ANNUAL_INCOME, REQUIRED_FIELD_MOBILE_NUMBER, and REQUIRED_FIELD_EMAIL_ID.

> **Skip if:**
> - Not all elements of $.message.intent.provider.items[*].xinput.head.descriptor.code may be in ["PERSONAL_INFORMATION_LAMF"]

---

**REQUIRED_FIELD_PAN**
`group: SEARCH_ITEMS > REQUIRED_ITEM_FIELDS > REQUIRED_XINPUT_FIELDS > LAMF_FIELDS | type: leaf`

- $.message.intent.provider.items[*].xinput.form.data.pan.value must be present in the payload

**REQUIRED_FIELD_FULL_NAME**
`group: SEARCH_ITEMS > REQUIRED_ITEM_FIELDS > REQUIRED_XINPUT_FIELDS > LAMF_FIELDS | type: leaf`

- $.message.intent.provider.items[*].xinput.form.data.fullName.value must be present in the payload

**REQUIRED_FIELD_CONSTITUION**
`group: SEARCH_ITEMS > REQUIRED_ITEM_FIELDS > REQUIRED_XINPUT_FIELDS > LAMF_FIELDS | type: leaf`

- $.message.intent.provider.items[*].xinput.form.data.constitution.value must be present in the payload

**REQUIRED_FIELD_GENDER**
`group: SEARCH_ITEMS > REQUIRED_ITEM_FIELDS > REQUIRED_XINPUT_FIELDS > LAMF_FIELDS | type: leaf`

- $.message.intent.provider.items[*].xinput.form.data.gender.value must be present in the payload

**REQUIRED_FIELD_EMPLOYMENT_TYPE**
`group: SEARCH_ITEMS > REQUIRED_ITEM_FIELDS > REQUIRED_XINPUT_FIELDS > LAMF_FIELDS | type: leaf`

- $.message.intent.provider.items[*].xinput.form.data.employmentType.value must be present in the payload

**REQUIRED_FIELD_DOB**
`group: SEARCH_ITEMS > REQUIRED_ITEM_FIELDS > REQUIRED_XINPUT_FIELDS > LAMF_FIELDS | type: leaf`

- $.message.intent.provider.items[*].xinput.form.data.dob.value must be present in the payload

**REQUIRED_FIELD_ANNUAL_INCOME**
`group: SEARCH_ITEMS > REQUIRED_ITEM_FIELDS > REQUIRED_XINPUT_FIELDS > LAMF_FIELDS | type: leaf`

- $.message.intent.provider.items[*].xinput.form.data.annualIncome.value must be present in the payload

**REQUIRED_FIELD_MOBILE_NUMBER**
`group: SEARCH_ITEMS > REQUIRED_ITEM_FIELDS > REQUIRED_XINPUT_FIELDS > LAMF_FIELDS | type: leaf`

- $.message.intent.provider.items[*].xinput.form.data.mobileNumber.value must be present in the payload

**REQUIRED_FIELD_EMAIL_ID**
`group: SEARCH_ITEMS > REQUIRED_ITEM_FIELDS > REQUIRED_XINPUT_FIELDS > LAMF_FIELDS | type: leaf`

- $.message.intent.provider.items[*].xinput.form.data.emailId.value must be present in the payload

##### INVOICE_LOAN_FIELDS

This is a group of **1** sub-validation(s) that all must pass: REQUIRED_FIELD_BUREAU_CONSENT_INVOICE.

> **Skip if:**
> - Not all elements of $.message.intent.provider.items[*].xinput.head.descriptor.code may be in ["ORGANIZATION_INFORMATION"]

---

**REQUIRED_FIELD_BUREAU_CONSENT_INVOICE**
`group: SEARCH_ITEMS > REQUIRED_ITEM_FIELDS > REQUIRED_XINPUT_FIELDS > INVOICE_LOAN_FIELDS | type: leaf`

- $.message.intent.provider.items[*].xinput.form.data.bureauConsent.value must be present in the payload

#### VALID_XINPUT_ENUMS

This is a group of **1** sub-validation(s) that all must pass: REQUIRED_HEAD_CODE.

---

**REQUIRED_HEAD_CODE**
`group: SEARCH_ITEMS > REQUIRED_ITEM_FIELDS > VALID_XINPUT_ENUMS | type: leaf`

- All elements of $.message.intent.provider.items[*].xinput.head.descriptor.code must be in ["PERSONAL_INFORMATION", "CONSENT_APPROVAL", "ORGANIZATION_INFORMATION", "MERCHANT_AND_PRDOUCT_DETAILS", "BANK_STATEMENT_AND_GST_RETURNS", "BUSINESS_AND_FINANCIAL_DOCUMENTS", "ORGANIZATION_INFORMATION", "PERSONAL_INFORMATION_TERM", "PERSONAL_INFORMATION_GOLD", "PERSONAL_INFORMATION_TERM_GST", "PERSONAL_INFORMATION_BUSINESS_TERM", "PERSONAL_INFORMATION_LAMF", "PERSONAL_INFORMATION_BUSINESS_TERM_GST"]

> **Skip if:**
>
>     - $.message.intent.provider.items[*].xinput.head.descriptor.code is not in the payload

---

## SEARCH_FULFILLMENTS

This group contains **1** sub-group(s)/validation(s): REQUIRED_FULFILLMENT_ITEMS.

> **Skip if:**
> - $.message.intent.provider.fulfillments[*].customer.person.name must **not** be present in the payload

---

### REQUIRED_FULFILLMENT_ITEMS

This is a group of **7** sub-validation(s) that all must pass: REQUIRED_PERSON_NAME, REQUIRED_PERSON_DOB, REQUIRED_PERSON_GENDER, REQUIRED_CREDS_ID, REQUIRED_CREDS_TYPE, REQUIRED_CONTACT_EMAIL, and REQUIRED_CONTACT_PHONE.

---

**REQUIRED_PERSON_NAME**
`group: SEARCH_FULFILLMENTS > REQUIRED_FULFILLMENT_ITEMS | type: leaf`

- $._EXTERNAL._SELF.message.intent.provider.fulfillments[*].customer.person.name must be present in the payload

**REQUIRED_PERSON_DOB**
`group: SEARCH_FULFILLMENTS > REQUIRED_FULFILLMENT_ITEMS | type: leaf`

- $._EXTERNAL._SELF.message.intent.provider.fulfillments[*].customer.person.name must be present in the payload

**REQUIRED_PERSON_GENDER**
`group: SEARCH_FULFILLMENTS > REQUIRED_FULFILLMENT_ITEMS | type: leaf`

- $._EXTERNAL._SELF.message.intent.provider.fulfillments[*].customer.person.name must be present in the payload

**REQUIRED_CREDS_ID**
`group: SEARCH_FULFILLMENTS > REQUIRED_FULFILLMENT_ITEMS | type: leaf`

- $._EXTERNAL._SELF.message.intent.provider.fulfillments[*].customer.person.name must be present in the payload

**REQUIRED_CREDS_TYPE**
`group: SEARCH_FULFILLMENTS > REQUIRED_FULFILLMENT_ITEMS | type: leaf`

- $._EXTERNAL._SELF.message.intent.provider.fulfillments[*].customer.person.name must be present in the payload

**REQUIRED_CONTACT_EMAIL**
`group: SEARCH_FULFILLMENTS > REQUIRED_FULFILLMENT_ITEMS | type: leaf`

- $._EXTERNAL._SELF.message.intent.provider.fulfillments[*].customer.person.name must be present in the payload

**REQUIRED_CONTACT_PHONE**
`group: SEARCH_FULFILLMENTS > REQUIRED_FULFILLMENT_ITEMS | type: leaf`

- $._EXTERNAL._SELF.message.intent.provider.fulfillments[*].customer.person.name must be present in the payload

---

## SEARCH_PAYMENT

This group contains **1** sub-group(s)/validation(s): REQUIRED_PAYMENT_ITEMS.

---

### REQUIRED_PAYMENT_ITEMS

This is a group of **1** sub-validation(s) that all must pass: REQUIRED_PAYMENT_COLLECTED_BY.

---

**REQUIRED_PAYMENT_COLLECTED_BY**
`group: SEARCH_PAYMENT > REQUIRED_PAYMENT_ITEMS | type: leaf`

- $.message.intent.payment.collected_by must be present in the payload

---

## SEARCH_TAGS

This is a group of **2** sub-validation(s) that all must pass: REQUIRED_PAYMENT_TAGS and REQUIRED_BAP_TERMS.

---

**REQUIRED_PAYMENT_TAGS**
`group: SEARCH_TAGS | type: leaf`

- All elements of $.message.intent.tags[*].descriptor.code must be in ["BAP_TERMS", "BPP_TERMS"]

> **Skip if:**
>
>     - $.message.intent.tags[*].descriptor.code is not in the payload

**REQUIRED_BAP_TERMS**
`group: SEARCH_TAGS | type: leaf | scope: $.message.intent.tags[?(@.descriptor.code == 'BAP_TERMS')]`

- All elements of $.message.intent.tags[?(@.descriptor.code == 'BAP_TERMS')].list[*].descriptor.code must be in ["STATIC_TERMS", "OFFLINE_CONTRACT"]
