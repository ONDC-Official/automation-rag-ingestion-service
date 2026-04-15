---
action: update
codeName: L1validations
numTests: 27
generated: 2026-04-15
domain: ONDC:FIS12
version: 2.3.0
---

# L1validations — `update` Validations

These are the validation rules applied when processing the `update` API call in the L1validations flow.
There are **27** validation rules organized into **5** top-level group(s).

---
## UPDATE_CONTEXT

This group contains **3** sub-group(s)/validation(s): CONTEXT_REQUIRED, CONTEXT_ENUM, and CONTEXT_REGEX.

---

### CONTEXT_REQUIRED

This is a group of **12** sub-validation(s) that all must pass: REQUIRED_CONTEXT_LOCATION_COUNTRY_CODE, REQUIRED_CONTEXT_LOCATION_CITY_CODE, REQUIRED_CONTEXT_DOMAIN, REQUIRED_CONTEXT_TIMESTAMP, REQUIRED_CONTEXT_BAP_ID, REQUIRED_CONTEXT_BAP_URI, REQUIRED_CONTEXT_BPP_ID, REQUIRED_CONTEXT_BPP_URI, REQUIRED_CONTEXT_TRANSACTION_ID, REQUIRED_CONTEXT_MESSAGE_ID, REQUIRED_CONTEXT_VERSION, and REQUIRED_CONTEXT_TTL.

---

**REQUIRED_CONTEXT_LOCATION_COUNTRY_CODE**
`group: UPDATE_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.location.country.code must be present in the payload

**REQUIRED_CONTEXT_LOCATION_CITY_CODE**
`group: UPDATE_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.location.city.code must be present in the payload

**REQUIRED_CONTEXT_DOMAIN**
`group: UPDATE_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.domain must be present in the payload

**REQUIRED_CONTEXT_TIMESTAMP**
`group: UPDATE_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.timestamp must be present in the payload

**REQUIRED_CONTEXT_BAP_ID**
`group: UPDATE_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.bap_id must be present in the payload

**REQUIRED_CONTEXT_BAP_URI**
`group: UPDATE_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.bap_uri must be present in the payload

**REQUIRED_CONTEXT_BPP_ID**
`group: UPDATE_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.bpp_id must be present in the payload

> **Skip if:**
>
>     - all elements of ["update"] are in ["search"]

**REQUIRED_CONTEXT_BPP_URI**
`group: UPDATE_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.bpp_uri must be present in the payload

> **Skip if:**
>
>     - all elements of ["update"] are in ["search"]

**REQUIRED_CONTEXT_TRANSACTION_ID**
`group: UPDATE_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.transaction_id must be present in the payload

**REQUIRED_CONTEXT_MESSAGE_ID**
`group: UPDATE_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.message_id must be present in the payload

**REQUIRED_CONTEXT_VERSION**
`group: UPDATE_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.version must be present in the payload

**REQUIRED_CONTEXT_TTL**
`group: UPDATE_CONTEXT > CONTEXT_REQUIRED | type: leaf`

- $.context.ttl must be present in the payload

### CONTEXT_ENUM

This is a group of **2** sub-validation(s) that all must pass: VALID_CONTEXT_LOCATION_COUNTRY_CODE and VALID_CONTEXT_DOMAIN.

---

**VALID_CONTEXT_LOCATION_COUNTRY_CODE**
`group: UPDATE_CONTEXT > CONTEXT_ENUM | type: leaf`

- At least one of $.context.location.country.code must be in ["IND"]

> **Skip if:**
>
>     - $.context.location.country.code is not in the payload

**VALID_CONTEXT_DOMAIN**
`group: UPDATE_CONTEXT > CONTEXT_ENUM | type: leaf`

- All elements of $.context.domain must be in ["ONDC:FIS12"]

> **Skip if:**
>
>     - $.context.domain is not in the payload

### CONTEXT_REGEX

This is a group of **5** sub-validation(s) that all must pass: REGEX_CONTEXT_LOCATION_CITY_CODE, REGEX_CONTEXT_TIMESTAMP, REGEX_CONTEXT_BAP_ID, REGEX_CONTEXT_BAP_URI, and REGEX_CONTEXT_TTL.

---

**REGEX_CONTEXT_LOCATION_CITY_CODE**
`group: UPDATE_CONTEXT > CONTEXT_REGEX | type: leaf`

- All elements of $.context.location.city.code must follow every regex in ["^\*$"]

> **Skip if:**
>
>     - $.context.location.city.code is not in the payload

**REGEX_CONTEXT_TIMESTAMP**
`group: UPDATE_CONTEXT > CONTEXT_REGEX | type: leaf`

- All elements of $.context.timestamp must follow every regex in ["^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[+-]\\d{2}:\\d{2})$"]

> **Skip if:**
>
>     - $.context.timestamp is not in the payload

**REGEX_CONTEXT_BAP_ID**
`group: UPDATE_CONTEXT > CONTEXT_REGEX | type: leaf`

- All elements of $.context.bap_id must follow every regex in ["^(?!.*\b(?:http|https|www)\b)[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)+$"]

> **Skip if:**
>
>     - $.context.bap_id is not in the payload

**REGEX_CONTEXT_BAP_URI**
`group: UPDATE_CONTEXT > CONTEXT_REGEX | type: leaf`

- All elements of $.context.bap_uri must follow every regex in ["^https?://([a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*|localhost)(:\d+)?(/.*)?$"]

> **Skip if:**
>
>     - $.context.bap_uri is not in the payload

**REGEX_CONTEXT_TTL**
`group: UPDATE_CONTEXT > CONTEXT_REGEX | type: leaf`

- All elements of $.context.ttl must follow every regex in ["^P(?=\\d|T\\d)(\\d+Y)?(\\d+M)?(\\d+D)?(T(\\d+H)?(\\d+M)?(\\d+S)?)?$"]

> **Skip if:**
>
>     - $.context.ttl is not in the payload

---

## UPDATE_ORDER_ID

`group: top-level | type: leaf`

- $.message.order.id must be present in the payload

---

## UPDATE_PAYMENT_TARGET

This is a group of **4** sub-validation(s) that all must pass: REQUIRED_PAYMENT_TYPE, REQUIRED_PAYMENT_TIME_LABEL, VALID_PAYMENT_TIME_LABEL_ENUM, and REQUIRED_PAYMENT_PARAMS_AMOUNT.

> **Skip if:**
> **Any of these must be true:**
>   - At least one of $.message.update_target must be in ["fulfillment"]
>   - $.message.order.payments[*].type must **not** be present in the payload

---

**REQUIRED_PAYMENT_TYPE**
`group: UPDATE_PAYMENT_TARGET | type: leaf`

- All elements of $.message.order.payments[*].type must be in ["POST_FULFILLMENT", "ON_ORDER"]

**REQUIRED_PAYMENT_TIME_LABEL**
`group: UPDATE_PAYMENT_TARGET | type: leaf`

- $.message.order.payments[*].time.label must be present in the payload

**VALID_PAYMENT_TIME_LABEL_ENUM**
`group: UPDATE_PAYMENT_TARGET | type: leaf`

- All elements of $.message.order.payments[*].time.label must be in ["PRE_PART_PAYMENT", "INSTALLMENT", "FORECLOSURE", "MISSED_EMI_PAYMENT"]

**REQUIRED_PAYMENT_PARAMS_AMOUNT**
`group: UPDATE_PAYMENT_TARGET | type: leaf`

- $.message.order.payments[*].params.amount must be present in the payload

---

## UPDATE_PAYMENT_REF_ID_GOLD

This is a group of **1** sub-validation(s) that all must pass: REQUIRED_PAYMENT_REF_ID.

> **Skip if:**
> **Any of these must be true:**
>   - **Any of these must be true:**
>     - None of $.message.order.items[*].descriptor.code may be in ["LOAN"]
>     - At least one of $.message.update_target must be in ["fulfillment"]
>   - $.message.order.payments[*].type must **not** be present in the payload

---

**REQUIRED_PAYMENT_REF_ID**
`group: UPDATE_PAYMENT_REF_ID_GOLD | type: leaf`

- $.message.order.payments[*].tags[?(@.descriptor.code=='LOAN_REPAYMENT')].list[?(@.descriptor.code=='ref_id')].value must be present in the payload

---

## UPDATE_FULFILLMENT_TARGET

This is a group of **2** sub-validation(s) that all must pass: REQUIRED_FULFILLMENT_STATE_CODE and VALID_FULFILLMENT_STATE_ENUM.

> **Skip if:**
> - None of $.message.update_target may be in ["fulfillment"]

---

**REQUIRED_FULFILLMENT_STATE_CODE**
`group: UPDATE_FULFILLMENT_TARGET | type: leaf`

- $.message.order.fulfillments[*].state.descriptor.code must be present in the payload

**VALID_FULFILLMENT_STATE_ENUM**
`group: UPDATE_FULFILLMENT_TARGET | type: leaf`

- All elements of $.message.order.fulfillments[*].state.descriptor.code must be in ["INITIATED", "SANCTIONED", "DISBURSED", "PENDING", "REJECTED", "COMPLETED", "CONSENT_REQUIRED", "APPROVED", "DISPATCHED"]
