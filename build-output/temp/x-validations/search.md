---
action: search
domain: ONDC:FIS12
version: 2.3.0
numTests: 6
generated: 2026-04-14
---

```json
{
  "_TESTS_": {
    "search": [
      {
        "_NAME_": "SEARCH_CONTEXT",
        "action": [
          "search"
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
                "usecasepath": "$.message.intent.provider.id",
                "_CONTINUE_": "!(usecasepath are present)",
                "_RETURN_": "attr are present"
              },
              {
                "_NAME_": "REQUIRED_CONTEXT_BPP_URI",
                "attr": "$.context.bpp_uri",
                "usecasepath": "$.message.intent.provider.id",
                "_CONTINUE_": "!(usecasepath are present)",
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
                "usecasepath": "$.message.intent.provider.id",
                "_CONTINUE_": "!(attr are present && usecasepath are present)",
                "_RETURN_": "attr follow regex reg"
              },
              {
                "_NAME_": "REGEX_CONTEXT_BPP_URI",
                "attr": "$.context.bpp_uri",
                "reg": [
                  "^https:\\/\\/(www\\.)?[a-zA-Z0-9-]+(\\.[a-zA-Z0-9-]+)+(/)?$"
                ],
                "usecasepath": "$.message.intent.provider.id",
                "_CONTINUE_": "!(attr are present && usecasepath are present)",
                "_RETURN_": "attr follow regex reg"
              }
            ]
          }
        ]
      },
      {
        "_NAME_": "SEARCH_CATEGORY_CODE",
        "action": [
          "search"
        ],
        "useCasePath": "$.message.intent.provider.id",
        "_CONTINUE_": "(useCasePath are present)",
        "_RETURN_": [
          {
            "_NAME_": "REQUIRED_CATEGORY_CODE",
            "attr": "$.message.intent.category.descriptor.code",
            "_RETURN_": "attr are present"
          },
          {
            "_NAME_": "VALID_ENUM_CATEGORY_CODE",
            "attr": "$.message.intent.category.descriptor.code",
            "enumList": [
              "LOAN",
              "UNSECURED_PERSONAL",
              "SECURED_PERSONAL",
              "OFFERS",
              "ADDITIONAL_DATA",
              "PERSONAL_FINANCING",
              "CONSUMER_INVOICE_FINANCING",
              "AGRI_PURCHASE_FINANCE",
              "ELECTRONICS_PURCHASE_FINANCE",
              "BUSINESS",
              "SOLE_PROPRIETORSHIP",
              "OTHER",
              "PARTNERSHIP_FIRM",
              "PRIVATE_LTD",
              "INVOICE_FINANCING",
              "GOLD_LOAN",
              "LAMF",
              "TERM_LOAN",
              "CREDIT_LINE",
              "DOCUMENT_BASED_DRAWDOWN",
              "NON_DOCUMENT_BASED_DRAWDOWN",
              "BANKING",
              "STATEMENT_UPLOAD",
              "AA_BANKING",
              "GST",
              "AA_GST",
              "GSP",
              "RETURN_UPLOAD",
              "MUTUAL_FUND",
              "AA_LOAN",
              "MFC",
              "ITR",
              "UPLOAD",
              "BUREAU_LOAN",
              "DERIVED_DATA",
              "ADDITIONAL_UPLOAD",
              "RTA"
            ],
            "_CONTINUE_": "!(attr are present)",
            "_RETURN_": "attr all in enumList"
          }
        ]
      },
      {
        "_NAME_": "SEARCH_ITEMS",
        "action": [
          "search"
        ],
        "useCasePath": "$.message.intent.provider.id",
        "_CONTINUE_": "!(useCasePath are present)",
        "_RETURN_": [
          {
            "_NAME_": "REQUIRED_ITEM_FIELDS",
            "_RETURN_": [
              {
                "_NAME_": "REQUIRED_PROVIDER_ID",
                "attr": "$.message.intent.provider.id",
                "_RETURN_": "attr are present"
              },
              {
                "_NAME_": "REQUIRED_PROVIDER_ITEM_ID",
                "attr": "$.message.intent.provider.items[*].id",
                "_RETURN_": "attr are present"
              },
              {
                "_NAME_": "REQUIRED_XINPUT_FIELDS",
                "_RETURN_": [
                  {
                    "_NAME_": "REQUIRED_HEAD_CODE",
                    "attr": "$.message.intent.provider.items[*].xinput.head.descriptor.code",
                    "_RETURN_": "attr are present"
                  },
                  {
                    "_NAME_": "REQUIRED_FORM_ID",
                    "attr": "$.message.intent.provider.items[*].xinput.form.id",
                    "_RETURN_": "attr are present"
                  },
                  {
                    "_NAME_": "REQUIRED_SUBMISSION_ID",
                    "attr": "$.message.intent.provider.items[*].xinput.form_response.submission_id",
                    "useCasePath": "$.message.intent.provider.items[*].xinput.head.descriptor.code",
                    "formHeading": "CONSENT_APPROVAL",
                    "_CONTINUE_": "!(useCasePath equal to formHeading)",
                    "_RETURN_": "attr are present"
                  },
                  {
                    "_NAME_": "PERSONAL_LOAN_FIELDS",
                    "usecasepath": "$.message.intent.provider.items[*].xinput.head.descriptor.code",
                    "formHeading": [
                      "PERSONAL_INFORMATION"
                    ],
                    "_CONTINUE_": "!(usecasepath all in formHeading)",
                    "_RETURN_": [
                      {
                        "_NAME_": "REQUIRED_FIELD_PAN_NAME_1",
                        "attr": "$.message.intent.provider.items[*].xinput.form.data.panName.value",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_FIELD_DOB",
                        "attr": "$.message.intent.provider.items[*].xinput.form.data.dob.value",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_FIELD_GENDER",
                        "attr": "$.message.intent.provider.items[*].xinput.form.data.gender.value",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_FIELD_PAN",
                        "attr": "$.message.intent.provider.items[*].xinput.form.data.pan.value",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_FIELD_CONTACT_NUMBER",
                        "attr": "$.message.intent.provider.items[*].xinput.form.data.contactNumber.value",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_FIELD_INCOME",
                        "attr": "$.message.intent.provider.items[*].xinput.form.data.income.value",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_FIELD_COMPANY_NAME",
                        "attr": "$.message.intent.provider.items[*].xinput.form.data.companyName.value",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_FIELD_BUREAU_CONSENT",
                        "attr": "$.message.intent.provider.items[*].xinput.form.data.bureauConsent.value",
                        "_RETURN_": "attr are present"
                      }
                    ]
                  },
                  {
                    "_NAME_": "REQUIRED_CONSENT_FIELDS",
                    "usecasepath": "$.message.intent.provider.items[*].xinput.head.descriptor.code",
                    "formHeading": [
                      "CONSENT_APPROVAL"
                    ],
                    "_CONTINUE_": "!(usecasepath any in formHeading)",
                    "_RETURN_": [
                      {
                        "_NAME_": "REQUIRED_FIELD_CONSENT_HANDLER",
                        "attr": "$.message.intent.provider.items[*].xinput.form_response.submission_id",
                        "_RETURN_": "attr are present"
                      }
                    ]
                  },
                  {
                    "_NAME_": "GOLD_LOAN_FIELDS",
                    "attr": "$.message.intent.provider.items[*].xinput.head.descriptor.code",
                    "formHeading": [
                      "PERSONAL_INFORMATION_GOLD"
                    ],
                    "_CONTINUE_": "!(attr all in  formHeading)",
                    "_RETURN_": [
                      {
                        "_NAME_": "REQUIRED_FIELD_PAN",
                        "attr": "$.message.catalog.providers[*].items[*].xinput.form.data.pan.value",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_FULL_NAME",
                        "attr": "$.message.catalog.providers[*].items[*].xinput.form.data.fullName.value",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_FIELD_GENDER",
                        "attr": "$.message.catalog.providers[*].items[*].xinput.form.data.gender.value",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_FIELD_DOB",
                        "attr": "$.message.catalog.providers[*].items[*].xinput.form.data.dob.value",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_FIELD_CONTACT_NUMBER",
                        "attr": "$.message.catalog.providers[*].items[*].xinput.form.data.contactNumber.value",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_FIELD_PINCODE",
                        "attr": "$.message.catalog.providers[*].items[*].xinput.form.data.pincode.value",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_FIELD_JWELLERY",
                        "attr": "$.message.catalog.providers[*].items[*].xinput.form.data.jewellery.value",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_FIELD_PURITY",
                        "attr": "$.message.catalog.providers[*].items[*].xinput.form.data.purity.value",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_FIELD_BUREAU_CONSENT",
                        "attr": "$.message.catalog.providers[*].items[*].xinput.form.data.bureauConsent.value",
                        "_RETURN_": "attr are present"
                      }
                    ]
                  },
                  {
                    "_NAME_": "WORKING_CAPITAL_LOAN_FIELDS",
                    "attr": "$.message.intent.provider.items[*].xinput.head.descriptor.code",
                    "formHeading": [
                      "BANK_STATEMENT_AND_GST_RETURNS"
                    ],
                    "_CONTINUE_": "!(attr all in  formHeading)",
                    "_RETURN_": [
                      {
                        "_NAME_": "REQUIRED_FIELD_GSTIN_PROFILE_1",
                        "attr": "$.message.intent.provider.items[*].xinput.form.data.gstinProfile_1.value",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_FIELD_GSTR_B2B_INVOICE_1",
                        "attr": "$.message.intent.provider.items[*].xinput.form.data.gstr1B2bInvoice_1.value",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_FIELD_GSTR_B2B_CDNR_1",
                        "attr": "$.message.intent.provider.items[*].xinput.form.data.gstr1B2bCdnr_1.value",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_FIELD_GSTR_B2B_INVOICES_1",
                        "attr": "$.message.intent.provider.items[*].xinput.form.data.gstr2aB2bInvoices_1.value",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_FIELD_GSTR_3B_SUMMARY_1",
                        "attr": "$.message.intent.provider.items[*].xinput.form.data.gstr3bSummary_1.value",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_FIELD_BANK_STATEMENT_FILES",
                        "attr": "$.message.intent.provider.items[*].xinput.form.data.bankStatementFiles_1.value",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_FIELD_BANK_NAME",
                        "attr": "$.message.intent.provider.items[*].xinput.form.data.bankName_1.value",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_FIELD_MIME_TYPE",
                        "attr": "$.message.intent.provider.items[*].xinput.form.data.mimeType_1.value",
                        "_RETURN_": "attr are present"
                      }
                    ]
                  },
                  {
                    "_NAME_": "BUSINESS_AND_FINANCIAL_DOCUMENTS_FIELDS",
                    "usecasepath": "$.message.intent.provider.items[*].xinput.head.descriptor.code",
                    "formHeading": [
                      "BUSINESS_AND_FINANCIAL_DOCUMENTS"
                    ],
                    "_CONTINUE_": "!(usecasepath all in  formHeading)",
                    "_RETURN_": [
                      {
                        "_NAME_": "REQUIRED_FIELD_FINANCIAL_STATEMENTS",
                        "attr": "$.message.intent.provider.items[*].xinput.form.data.financialStatements.value",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_FIELD_SHAREHOLDING_PATTERN",
                        "attr": "$.message.intent.provider.items[*].xinput.form.data.shareholdingPattern.value",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_FIELD_ITR",
                        "attr": "$.message.intent.provider.items[*].xinput.form.data.itr.value",
                        "_RETURN_": "attr are present"
                      }
                    ]
                  },
                  {
                    "_NAME_": "TERM_LOAN_FIELDS",
                    "usecasepath": "$.message.intent.provider.items[*].xinput.head.descriptor.code",
                    "formHeading": [
                      "PERSONAL_INFORMATION_TERM"
                    ],
                    "_CONTINUE_": "!(usecasepath all in formHeading)",
                    "_RETURN_": [
                      {
                        "_NAME_": "REQUIRED_FIELD_PAN",
                        "attr": "$.message.intent.provider.items[*].xinput.form.data.pan.value",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_FULL_NAME",
                        "attr": "$.message.intent.provider.items[*].xinput.form.data.fullName.value",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_DOB",
                        "attr": "$.message.intent.provider.items[*].xinput.form.data.dob.value",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_CONSTITUTION",
                        "attr": "$.message.intent.provider.items[*].xinput.form.data.constitution.value",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_BUSINESS_PAN",
                        "attr": "$.message.intent.provider.items[*].xinput.form.data.businessPan.value",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_DOI",
                        "attr": "$.message.intent.provider.items[*].xinput.form.data.doi.value",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_NATURE_OF_BUSINESS",
                        "attr": "$.message.intent.provider.items[*].xinput.form.data.natureOfBusiness.value",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_ANNUAL_TURNOVER",
                        "attr": "$.message.intent.provider.items[*].xinput.form.data.annualTurnover.value",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_BUSINESS_PINCODE",
                        "attr": "$.message.intent.provider.items[*].xinput.form.data.businessPincode.value",
                        "_RETURN_": "attr are present"
                      }
                    ]
                  },
                  {
                    "_NAME_": "LAMF_FIELDS",
                    "usecasepath": "$.message.intent.provider.items[*].xinput.head.descriptor.code",
                    "formHeading": [
                      "PERSONAL_INFORMATION_LAMF"
                    ],
                    "_CONTINUE_": "!(usecasepath all in  formHeading)",
                    "_RETURN_": [
                      {
                        "_NAME_": "REQUIRED_FIELD_PAN",
                        "attr": "$.message.intent.provider.items[*].xinput.form.data.pan.value",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_FIELD_FULL_NAME",
                        "attr": "$.message.intent.provider.items[*].xinput.form.data.fullName.value",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_FIELD_CONSTITUION",
                        "attr": "$.message.intent.provider.items[*].xinput.form.data.constitution.value",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_FIELD_GENDER",
                        "attr": "$.message.intent.provider.items[*].xinput.form.data.gender.value",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_FIELD_EMPLOYMENT_TYPE",
                        "attr": "$.message.intent.provider.items[*].xinput.form.data.employmentType.value",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_FIELD_DOB",
                        "attr": "$.message.intent.provider.items[*].xinput.form.data.dob.value",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_FIELD_ANNUAL_INCOME",
                        "attr": "$.message.intent.provider.items[*].xinput.form.data.annualIncome.value",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_FIELD_MOBILE_NUMBER",
                        "attr": "$.message.intent.provider.items[*].xinput.form.data.mobileNumber.value",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_FIELD_EMAIL_ID",
                        "attr": "$.message.intent.provider.items[*].xinput.form.data.emailId.value",
                        "_RETURN_": "attr are present"
                      }
                    ]
                  },
                  {
                    "_NAME_": "INVOICE_LOAN_FIELDS",
                    "usecasepath": "$.message.intent.provider.items[*].xinput.head.descriptor.code",
                    "formHeading": [
                      "ORGANIZATION_INFORMATION"
                    ],
                    "_CONTINUE_": "!(usecasepath all in formHeading)",
                    "_RETURN_": [
                      {
                        "_NAME_": "REQUIRED_FIELD_BUREAU_CONSENT_INVOICE",
                        "attr": "$.message.intent.provider.items[*].xinput.form.data.bureauConsent.value",
                        "_RETURN_": "attr are present"
                      }
                    ]
                  }
                ]
              },
              {
                "_NAME_": "VALID_XINPUT_ENUMS",
                "_RETURN_": [
                  {
                    "_NAME_": "REQUIRED_HEAD_CODE",
                    "attr": "$.message.intent.provider.items[*].xinput.head.descriptor.code",
                    "_CONTINUE_": "!(attr are present)",
                    "enumList": [
                      "PERSONAL_INFORMATION",
                      "CONSENT_APPROVAL",
                      "ORGANIZATION_INFORMATION",
                      "MERCHANT_AND_PRDOUCT_DETAILS",
                      "BANK_STATEMENT_AND_GST_RETURNS",
                      "BUSINESS_AND_FINANCIAL_DOCUMENTS",
                      "ORGANIZATION_INFORMATION",
                      "PERSONAL_INFORMATION_TERM",
                      "PERSONAL_INFORMATION_GOLD",
                      "PERSONAL_INFORMATION_TERM_GST",
                      "PERSONAL_INFORMATION_BUSINESS_TERM",
                      "PERSONAL_INFORMATION_LAMF",
                      "PERSONAL_INFORMATION_BUSINESS_TERM_GST"
                    ],
                    "_RETURN_": "attr all in enumList"
                  }
                ]
              }
            ]
          }
        ]
      },
      {
        "_NAME_": "SEARCH_FULFILLMENTS",
        "attr": "$.message.intent.provider.fulfillments[*].customer.person.name",
        "_CONTINUE_": "!(attr are present)",
        "_RETURN_": [
          {
            "_NAME_": "REQUIRED_FULFILLMENT_ITEMS",
            "_RETURN_": [
              {
                "_NAME_": "REQUIRED_PERSON_NAME",
                "attr": "$.message.intent.provider.fulfillments[*].customer.person.name",
                "_RETURN_": "attr are present"
              },
              {
                "_NAME_": "REQUIRED_PERSON_DOB",
                "attr": "$.message.intent.provider.fulfillments[*].customer.person.dob",
                "_RETURN_": "attr are present"
              },
              {
                "_NAME_": "REQUIRED_PERSON_GENDER",
                "attr": "$.message.intent.provider.fulfillments[*].customer.person.gender",
                "_RETURN_": "attr are present"
              },
              {
                "_NAME_": "REQUIRED_CREDS_ID",
                "attr": "$.message.intent.provider.fulfillments[*].customer.person.creds[*].id",
                "_RETURN_": "attr are present"
              },
              {
                "_NAME_": "REQUIRED_CREDS_TYPE",
                "attr": "$.message.intent.provider.fulfillments[*].customer.person.creds[*].type",
                "_RETURN_": "attr are present"
              },
              {
                "_NAME_": "REQUIRED_CONTACT_EMAIL",
                "attr": "$.message.intent.provider.fulfillments[*].customer.contact.email",
                "_RETURN_": "attr are present"
              },
              {
                "_NAME_": "REQUIRED_CONTACT_PHONE",
                "attr": "$.message.intent.provider.fulfillments[*].customer.contact.phone",
                "_RETURN_": "attr are present"
              }
            ]
          }
        ]
      },
      {
        "_NAME_": "SEARCH_PAYMENT",
        "action": [
          "search"
        ],
        "_RETURN_": [
          {
            "_NAME_": "REQUIRED_PAYMENT_ITEMS",
            "_RETURN_": [
              {
                "_NAME_": "REQUIRED_PAYMENT_COLLECTED_BY",
                "attr": "$.message.intent.payment.collected_by",
                "_RETURN_": "attr are present"
              }
            ]
          }
        ]
      },
      {
        "_NAME_": "SEARCH_TAGS",
        "action": [
          "search"
        ],
        "_RETURN_": [
          {
            "_NAME_": "REQUIRED_PAYMENT_TAGS",
            "validTags": [
              "BAP_TERMS",
              "BPP_TERMS"
            ],
            "tagPath": "$.message.intent.tags[*].descriptor.code",
            "_CONTINUE_": "!(tagPath are present)",
            "_RETURN_": "tagPath all in validTags"
          },
          {
            "_NAME_": "REQUIRED_BAP_TERMS",
            "_SCOPE_": "$.message.intent.tags[?(@.descriptor.code == 'BAP_TERMS')]",
            "subTags": "$.list[*].descriptor.code",
            "validValues": [
              "STATIC_TERMS",
              "OFFLINE_CONTRACT"
            ],
            "_RETURN_": "subTags all in validValues"
          }
        ]
      }
    ]
  }
}
```