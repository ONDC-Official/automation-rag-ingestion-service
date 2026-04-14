---
action: select
domain: ONDC:FIS12
version: 2.3.0
numTests: 4
generated: 2026-04-14
---

```json
{
  "_TESTS_": {
    "select": [
      {
        "_NAME_": "SELECT_CONTEXT",
        "action": [
          "select"
        ],
        "domain": [
          "ONDC:FIS12"
        ],
        "version": [
          "2.3.0"
        ],
        "_RETURN_": [
          {
            "_NAME_": "CONTEXT_REQUIRED",
            "_RETURN_": [
              {
                "_NAME_": "REQUIRED_CONTEXT_LOCATION_COUNTRY_CODE",
                "attr": "$.context.location.country.code",
                "_RETURN_": "attr are present"
              },
              {
                "_NAME_": "REQUIRED_CONTEXT_LOCATION_CITY_CODE",
                "attr": "$.context.location.city.code",
                "_RETURN_": "attr are present"
              },
              {
                "_NAME_": "REQUIRED_CONTEXT_DOMAIN",
                "attr": "$.context.domain",
                "_RETURN_": "attr are present"
              },
              {
                "_NAME_": "REQUIRED_CONTEXT_TIMESTAMP",
                "attr": "$.context.timestamp",
                "_RETURN_": "attr are present"
              },
              {
                "_NAME_": "REQUIRED_CONTEXT_BAP_ID",
                "attr": "$.context.bap_id",
                "_RETURN_": "attr are present"
              },
              {
                "_NAME_": "REQUIRED_CONTEXT_BAP_URI",
                "attr": "$.context.bap_uri",
                "_RETURN_": "attr are present"
              },
              {
                "_NAME_": "REQUIRED_CONTEXT_TRANSACTION_ID",
                "attr": "$.context.transaction_id",
                "_RETURN_": "attr are present"
              },
              {
                "_NAME_": "REQUIRED_CONTEXT_MESSAGE_ID",
                "attr": "$.context.message_id",
                "_RETURN_": "attr are present"
              },
              {
                "_NAME_": "REQUIRED_CONTEXT_VERSION",
                "attr": "$.context.version",
                "_RETURN_": "attr are present"
              },
              {
                "_NAME_": "REQUIRED_CONTEXT_TTL",
                "attr": "$.context.ttl",
                "_RETURN_": "attr are present"
              },
              {
                "_NAME_": "REQUIRED_CONTEXT_BPP_ID",
                "attr": "$.context.bpp_id",
                "_RETURN_": "attr are present"
              },
              {
                "_NAME_": "REQUIRED_CONTEXT_BPP_URI",
                "attr": "$.context.bpp_uri",
                "_RETURN_": "attr are present"
              }
            ]
          },
          {
            "_NAME_": "CONTEXT_ENUM",
            "_RETURN_": [
              {
                "_NAME_": "VALID_CONTEXT_LOCATION_COUNTRY_CODE",
                "attr": "$.context.location.country.code",
                "_CONTINUE_": "!(attr are present)",
                "enumList": [
                  "IND"
                ],
                "_RETURN_": "attr all in enumList"
              },
              {
                "_NAME_": "VALID_CONTEXT_DOMAIN",
                "attr": "$.context.domain",
                "enumList": [
                  "ONDC:FIS12"
                ],
                "_CONTINUE_": "!(attr are present)",
                "_RETURN_": "attr all in enumList"
              }
            ]
          },
          {
            "_NAME_": "CONTEXT_REGEX",
            "_RETURN_": [
              {
                "_NAME_": "REGEX_CONTEXT_LOCATION_CITY_CODE",
                "attr": "$.context.location.city.code",
                "reg": [
                  "(\\\\*)|(^std\\\\:[0-9]{2,4}$)"
                ],
                "_CONTINUE_": "!(attr are present)",
                "_RETURN_": "attr follow regex reg"
              },
              {
                "_NAME_": "REGEX_CONTEXT_TIMESTAMP_1",
                "attr": "$.context.timestamp",
                "reg": [
                  "^\\\\d{4}-\\\\d{2}-\\\\d{2}T\\\\d{2}:\\\\d{2}:\\\\d{2}(\\\\.\\\\d+)?(Z|[+-]\\\\d{2}:\\\\d{2})$"
                ],
                "_CONTINUE_": "!(attr are present)",
                "_RETURN_": "attr follow regex reg"
              },
              {
                "_NAME_": "REGEX_CONTEXT_BAP_ID",
                "attr": "$.context.bap_id",
                "reg": [
                  "^(?!.*\\b(?:http|https|www)\\b)[a-zA-Z0-9-]+(\\.[a-zA-Z0-9-]+)+$"
                ],
                "_CONTINUE_": "!(attr are present)",
                "_RETURN_": "attr follow regex reg"
              },
              {
                "_NAME_": "REGEX_CONTEXT_BAP_URI",
                "attr": "$.context.bap_uri",
                "reg": [
                  "^https:\\/\\/(www\\.)?[a-zA-Z0-9-]+(\\.[a-zA-Z0-9-]+)+(/)?$"
                ],
                "_CONTINUE_": "!(attr are present)",
                "_RETURN_": "attr follow regex reg"
              },
              {
                "_NAME_": "REQUIRED_CONTEXT_TTL",
                "attr": "$.context.ttl",
                "reg": [
                  "^P(?=\\\\d|T\\\\d)(\\\\d+Y)?(\\\\d+M)?(\\\\d+D)?(T(\\\\d+H)?(\\\\d+M)?(\\\\d+S)?)?$"
                ],
                "_CONTINUE_": "!(attr are present)",
                "_RETURN_": "attr follow regex reg"
              },
              {
                "_NAME_": "REGEX_CONTEXT_BPP_ID",
                "attr": "$.context.bpp_id",
                "reg": [
                  "^(?!.*\\b(?:http|https|www)\\b)[a-zA-Z0-9-]+(\\.[a-zA-Z0-9-]+)+$"
                ],
                "_CONTINUE_": "!(attr are present)",
                "_RETURN_": "attr follow regex reg"
              },
              {
                "_NAME_": "REGEX_CONTEXT_BPP_URI",
                "attr": "$.context.bpp_uri",
                "reg": [
                  "^https:\\/\\/(www\\.)?[a-zA-Z0-9-]+(\\.[a-zA-Z0-9-]+)+(/)?$"
                ],
                "_CONTINUE_": "!(attr are present)",
                "_RETURN_": "attr follow regex reg"
              }
            ]
          }
        ]
      },
      {
        "_NAME_": "REQUIRED_PROVIDER_ID",
        "attr": "$.message.order.provider.id",
        "_RETURN_": "attr are present"
      },
      {
        "_NAME_": "REQUIRED_ITEM_FIELDS",
        "_RETURN_": [
          {
            "_NAME_": "REQUIRED_ITEM_ID",
            "attr": "$.message.order.items[*].id",
            "_RETURN_": "attr are present"
          },
          {
            "_NAME_": "REQUIRED_PARENT_ITEM_ID",
            "attr": "$.message.order.items[*].parent_item_id",
            "_RETURN_": "attr are present"
          },
          {
            "_NAME_": "REQUIRED_XINPUT_ITEMS",
            "usecasepath": "$.message.order.items[*].xinput.form.id",
            "_CONTINUE_": "!(usecasepath are present)",
            "_RETURN_": [
              {
                "_NAME_": "SET_LOAN_AMOUNT_FORM",
                "attrForm": "$.message.order.items[*].xinput.head.descriptor.code",
                "formHeading": [
                  "SET_LOAN_AMOUNT"
                ],
                "_CONTINUE_": "!(attrForm equal to formHeading)",
                "_RETURN_": [
                  {
                    "_NAME_": "REQUIRED_REQUEST_AMOUNT",
                    "attr": "$.message.order.items[*].xinput.form.data.requestAmount.value",
                    "_RETURN_": "attr are present"
                  }
                ]
              },
              {
                "_NAME_": "REQUIRED_FORM_SUBMISSION_ID",
                "attr": "$.message.order.items[*].xinput.form_response.submission_id",
                "useCasePath": "$.message.order.items[*].xinput.head.descriptor.code",
                "formHeading": [
                  "INDIVIDUAL_KYC",
                  "MANUAL_VERIFICATION"
                ],
                "_CONTINUE_": "!(useCasePath all in formHeading)",
                "_RETURN_": "attr are present"
              },
              {
                "_NAME_": "BUSINESS_KYC_FORM",
                "attrForm": "$.message.order.items[*].xinput.head.descriptor.code",
                "formHeading": [
                  "BUSINESS_KYC"
                ],
                "_CONTINUE_": "!(attrForm equal to formHeading)",
                "_RETURN_": [
                  {
                    "_NAME_": "REQUIRED_COMPANY_PAN",
                    "attr": "$.message.order.items[*].xinput.form.data.companyPan.value",
                    "_RETURN_": "attr are present"
                  },
                  {
                    "_NAME_": "REQUIRED_GST_CERTIFICATE",
                    "attr": "$.message.order.items[*].xinput.form.data.gstCertificate.value",
                    "_RETURN_": "attr are present"
                  },
                  {
                    "_NAME_": "REQUIRED_BUSINESS_PROOF",
                    "attr": "$.message.order.items[*].xinput.form.data.businessProof.value",
                    "_RETURN_": "attr are present"
                  },
                  {
                    "_NAME_": "REQUIRED_APPLICATION_FORM",
                    "attr": "$.message.order.items[*].xinput.form.data.applicationForm.value",
                    "_RETURN_": "attr are present"
                  }
                ]
              }
            ]
          },
          {
            "_NAME_": "VALID_TAGS",
            "tagPath1": "$.message.order.items[*].tags[*].descriptor.code",
            "_CONTINUE_": "!(tagPath1 are present)",
            "_RETURN_": [
              {
                "_NAME_": "VALID_ITEM_TAGS",
                "tagPath": "$.message.order.items[*].tags[*].descriptor.code",
                "validTags": [
                  "PLEDGE_REQUIREMENTS"
                ],
                "_CONTINUE_": "!(tagPath are present)",
                "_RETURN_": "tagPath all in validTags"
              },
              {
                "_NAME_": "VALID_PLEDGE_TAGS",
                "_SCOPE_": "$.message.order.items[*].tags[?(@.descriptor.code == 'PLEDGE_REQUIREMENTS')]",
                "subTags": "$.list[*].descriptor.code",
                "validValues": [
                  "SCHEME_CODE",
                  "UNITS_PLEDGED"
                ],
                "_RETURN_": "subTags all in validValues"
              }
            ]
          }
        ]
      },
      {
        "_NAME_": "REQUIRED_FULFILMENT_ITEMS",
        "_RETURN_": [
          {
            "_NAME_": "REQUIRED_FULFILLMENT_ID",
            "attr": "$.message.order.fulfillments[*].id",
            "_RETURN_": "attr are present"
          },
          {
            "_NAME_": "REQUIRED_CUSTOMER_ITEMS",
            "attr": "$.message.order.fulfillments[*].customer.person.name",
            "_CONTINUE_": "!(attr are present)",
            "_RETURN_": [
              {
                "_NAME_": "REQUIRED_CUSTOMER_DOB",
                "attr": "$.message.order.fulfillments[*].customer.person.dob",
                "_RETURN_": "attr are present"
              },
              {
                "_NAME_": "REQUIRED_CUSTOMER_GENDER",
                "attr": "$.message.order.fulfillments[*].customer.person.gender",
                "_RETURN_": "attr are present"
              },
              {
                "_NAME_": "REQUIRED_CREDS",
                "attr": "$.message.order.fulfillments[*].customer.person.creds[*].id",
                "_CONTINUE_": "!(attr are present)",
                "_RETURN_": [
                  {
                    "_NAME_": "REQUIRED_CUSTOMER_CREDS_ID",
                    "attr": "$.message.order.fulfillments[*].customer.person.creds[*].id",
                    "_RETURN_": "attr are present"
                  },
                  {
                    "_NAME_": "REQUIRED_CUSTOMER_CREDS_TYPE",
                    "attr": "$.message.order.fulfillments[*].customer.person.creds[*].type",
                    "_RETURN_": "attr are present"
                  }
                ]
              },
              {
                "_NAME_": "REQUIRED_CUSTOMER_CONTACT_EMAIL",
                "attr": "$.message.order.fulfillments[*].customer.contact.email",
                "_RETURN_": "attr are present"
              },
              {
                "_NAME_": "REQUIRED_CUSTOMER_CONTACT_PHONE",
                "attr": "$.message.order.fulfillments[*].customer.contact.phone",
                "_RETURN_": "attr are present"
              }
            ]
          }
        ]
      }
    ]
  }
}
```