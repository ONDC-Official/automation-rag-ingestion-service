---
action: on_search
domain: ONDC:FIS12
version: 2.3.0
numTests: 10
generated: 2026-04-14
---

```json
{
  "_TESTS_": {
    "on_search": [
      {
        "_NAME_": "ON_SEARCH_CONTEXT",
        "action": [
          "on_search"
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
        "_NAME_": "ON_SEARCH_CATALOG_NAME",
        "attr": "$.message.catalog.descriptor.name",
        "_RETURN_": "attr are present"
      },
      {
        "_NAME_": "ON_SEARCH_PROVIDER",
        "action": [
          "on_search"
        ],
        "_RETURN_": [
          {
            "_NAME_": "ON_SEARCH_PROVIDER_ID",
            "attr": "$.message.catalog.providers[*].id",
            "_RETURN_": "attr are present"
          },
          {
            "_NAME_": "ON_SEARCH_PROVIDER_NAME",
            "attr": "$.message.catalog.providers[*].descriptor.name",
            "_RETURN_": "attr are present"
          },
          {
            "_NAME_": "ON_SEARCH_PROVIDER_IMAGES_URL",
            "attr": "$.message.catalog.providers[*].descriptor.images[*].url",
            "_RETURN_": "attr are present"
          },
          {
            "_NAME_": "ON_SEARCH_PROVIDER_IMAGES_SIZE_TYPE",
            "attr": "$.message.catalog.providers[*].descriptor.images[*].size_type",
            "_RETURN_": "attr are present"
          }
        ]
      },
      {
        "_NAME_": "ON_SEARCH_CATEGORIES",
        "action": [
          "on_search"
        ],
        "usecasepath": "$.message.catalog.providers[*].categories[*].id",
        "_CONTINUE_": "!(usecasepath are present)",
        "_RETURN_": [
          {
            "_NAME_": "ON_SEARCH_CATEGORIES_NAME",
            "attr": "$.message.catalog.providers[*].categories[*].descriptor.name",
            "_RETURN_": "attr are present"
          },
          {
            "_NAME_": "ON_SEARCH_CATEGORIES_CODE",
            "attr": "$.message.catalog.providers[*].categories[*].descriptor.code",
            "_RETURN_": "attr are present"
          },
          {
            "_NAME_": "ON_SEARCH_CATEGORIES_ID",
            "attr": "$.message.catalog.providers[*].categories[*].id",
            "_RETURN_": "attr are present"
          },
          {
            "_NAME_": "ON_SEARCH_CATEGORIES_PARENT_ID",
            "attr": "$.message.catalog.providers[*].categories[*].parent_category_id",
            "category_code_path": "$.message.catalog.providers[*].categories[*].descriptor.code",
            "var_category_code": [
              "LOAN"
            ],
            "_CONTINUE_": "(category_code_path any in var_category_code)",
            "_RETURN_": "attr are present"
          },
          {
            "_NAME_": "VALID_ENUM_CATEGORY_CODE",
            "attr": "$.message.catalog.providers[*].categories[*].descriptor.code",
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
        "_NAME_": "ON_SEARCH_ITEMS",
        "_RETURN_": [
          {
            "_NAME_": "REQUIRED_ITEMS",
            "_RETURN_": [
              {
                "_NAME_": "REQUIRED_ITEM_ID",
                "attr": "$.message.catalog.providers[*].items[*].id",
                "_RETURN_": "attr are present"
              },
              {
                "_NAME_": "REQUIRED_ITEM_CODE",
                "attr": "$.message.catalog.providers[*].items[*].descriptor.code",
                "_RETURN_": "attr are present"
              },
              {
                "_NAME_": "REQUIRED_ITEM_CATEGORY_ID",
                "attr": "$.message.catalog.providers[*].items[*].category_ids[*]",
                "_RETURN_": "attr are present"
              },
              {
                "_NAME_": "CHECK_CATEGORY_ID",
                "attr": "$.message.catalog.providers[*].items[*].category_ids[*]",
                "useCasePath": "$.message.catalog.providers[*].categories[*].id",
                "_CONTINUE_": "!(useCasePath are present)",
                "_RETURN_": "(attr any in useCasePath)"
              },
              {
                "_NAME_": "REQUIRED_ITEM_FULFILLMENT_ID",
                "attr": "$.message.catalog.providers[*].items[*].fulfillment_ids[*]",
                "_RETURN_": "attr are present"
              },
              {
                "_NAME_": "REQUIRED_XINPUT_FIELDS",
                "usecasepath": "$.message.catalog.providers[*].items[*].tags[*].descriptor.code",
                "validTags": [
                  "LOAN_INFO"
                ],
                "_CONTINUE_": "!(usecasepath are present && usecasepath all in validTags)",
                "_RETURN_": [
                  {
                    "_NAME_": "REQUIRED_HEAD_CODE",
                    "attr": "$.message.catalog.providers[*].items[*].xinput.head.descriptor.code",
                    "_RETURN_": "attr are present"
                  },
                  {
                    "_NAME_": "REQUIRED_HEAD_NAME",
                    "attr": "$.message.catalog.providers[*].items[*].xinput.head.descriptor.name",
                    "_RETURN_": "attr are present"
                  },
                  {
                    "_NAME_": "REQUIRED_FORM_HEADINGS",
                    "attr": "$.message.catalog.providers[*].items[*].xinput.head.headings[*]",
                    "_RETURN_": "attr are present"
                  },
                  {
                    "_NAME_": "REQUIRED_FORM_ID",
                    "attr": "$.message.catalog.providers[*].items[*].xinput.form.id",
                    "_RETURN_": "attr are present"
                  },
                  {
                    "_NAME_": "REQUIRED_FORM_MIME_TYPE",
                    "attr": "$.message.catalog.providers[*].items[*].xinput.form.mime_type",
                    "_RETURN_": "attr are present"
                  },
                  {
                    "_NAME_": "PERSONAL_LOAN_FIELDS",
                    "usecasepath": "$.message.catalog.providers[*].items[*].xinput.head.descriptor.code",
                    "formHeading": [
                      "PERSONAL_INFORMATION"
                    ],
                    "_CONTINUE_": "!(usecasepath all in  formHeading)",
                    "_RETURN_": [
                      {
                        "_NAME_": "REQUIRED_FIELD_PAN_NAME",
                        "attr": "$.message.catalog.providers[*].items[*].xinput.form.data.panName.type",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_FIELD_DOB",
                        "attr": "$.message.catalog.providers[*].items[*].xinput.form.data.dob.type",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_FIELD_GENDER",
                        "attr": "$.message.catalog.providers[*].items[*].xinput.form.data.gender.type",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_FIELD_PAN",
                        "attr": "$.message.catalog.providers[*].items[*].xinput.form.data.pan.type",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_FIELD_CONTACT_NUMBER",
                        "attr": "$.message.catalog.providers[*].items[*].xinput.form.data.contactNumber.type",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_FIELD_EMPLOYMENT_TYPE",
                        "attr": "$.message.catalog.providers[*].items[*].xinput.form.data.employmentType.type",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_FIELD_INCOME",
                        "attr": "$.message.catalog.providers[*].items[*].xinput.form.data.income.type",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_FIELD_COMPANY_NAME",
                        "attr": "$.message.catalog.providers[*].items[*].xinput.form.data.companyName.type",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_FIELD_BUREAU_CONSENT",
                        "attr": "$.message.catalog.providers[*].items[*].xinput.form.data.bureauConsent.type",
                        "_RETURN_": "attr are present"
                      }
                    ]
                  },
                  {
                    "_NAME_": "REQUIRED_CONSENT_FIELDS",
                    "usecasepath": "$.message.catalog.providers[*].items[*].xinput.head.descriptor.code",
                    "formHeading": [
                      "CONSENT_APPROVAL"
                    ],
                    "_CONTINUE_": "!(usecasepath any in formHeading)",
                    "_RETURN_": [
                      {
                        "_NAME_": "REQUIRED_FIELD_CONSENT_HANDLER",
                        "attr": "$.message.catalog.providers[*].items[*].xinput.form.data.consent_handler",
                        "_RETURN_": "attr are present"
                      }
                    ]
                  },
                  {
                    "_NAME_": "INVOICE_LOAN_FIELDS",
                    "usecasepath": "$.message.catalog.providers[*].items[*].xinput.head.descriptor.code",
                    "formHeading": [
                      "ORGANIZATION_INFORMATION"
                    ],
                    "_CONTINUE_": "!(usecasepath all in formHeading)",
                    "_RETURN_": [
                      {
                        "_NAME_": "REQUIRED_FIELD_BUREAU_CONSENT",
                        "attr": "$.message.catalog.providers[*].items[*].xinput.form.data.bureauConsent.type",
                        "_RETURN_": "attr are present"
                      }
                    ]
                  },
                  {
                    "_NAME_": "GOLD_LOAN_FIELDS",
                    "usecasepath": "$.message.catalog.providers[*].items[*].xinput.head.descriptor.code",
                    "formHeading": [
                      "PERSONAL_INFORMATION_GOLD"
                    ],
                    "_CONTINUE_": "!(usecasepath all in formHeading)",
                    "_RETURN_": [
                      {
                        "_NAME_": "REQUIRED_FIELD_PAN",
                        "attr": "$.message.catalog.providers[*].items[*].xinput.form.data.pan.type",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_FULL_NAME",
                        "attr": "$.message.catalog.providers[*].items[*].xinput.form.data.fullName.type",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_FIELD_GENDER",
                        "attr": "$.message.catalog.providers[*].items[*].xinput.form.data.gender.type",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_FIELD_DOB",
                        "attr": "$.message.catalog.providers[*].items[*].xinput.form.data.dob.type",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_FIELD_CONTACT_NUMBER",
                        "attr": "$.message.catalog.providers[*].items[*].xinput.form.data.contactNumber.type",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_FIELD_PINCODE",
                        "attr": "$.message.catalog.providers[*].items[*].xinput.form.data.pincode.type",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_FIELD_JWELLERY",
                        "attr": "$.message.catalog.providers[*].items[*].xinput.form.data.jewellery.type",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_FIELD_PURITY",
                        "attr": "$.message.catalog.providers[*].items[*].xinput.form.data.purity.type",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_FIELD_BUREAU_CONSENT",
                        "attr": "$.message.catalog.providers[*].items[*].xinput.form.data.bureauConsent.type",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_CONSENT_FIELDS",
                        "attr": "$.message.catalog.providers[*].items[*].xinput.form.data.bureauConsent.type",
                        "usecasepath": "$.message.order.items[*].xinput.head.descriptor.code",
                        "formHeading": [
                          "CONSENT_APPROVAL"
                        ],
                        "_CONTINUE_": "!(usecasepath any in formHeading)",
                        "_RETURN_": [
                          {
                            "_NAME_": "REQUIRED_FIELD_AA_ID",
                            "attr": "$.message.catalog.providers[*].items[*].xinput.form.data.aa_id.type",
                            "_RETURN_": "attr are present"
                          }
                        ]
                      }
                    ]
                  },
                  {
                    "_NAME_": "WORKING_CAPITAL_LOAN_FIELDS",
                    "usecasepath": "$.message.catalog.providers[*].items[*].xinput.head.descriptor.code",
                    "formHeading": [
                      "BANK_STATEMENT_AND_GST_RETURNS"
                    ],
                    "_CONTINUE_": "!(usecasepath all in  formHeading)",
                    "_RETURN_": [
                      {
                        "_NAME_": "REQUIRED_FIELD_GSTIN_PROFILE_1",
                        "attr": "$.message.catalog.providers[*].items[*].xinput.form.data.gstinProfile_1.type",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_FIELD_GSTR_B2B_INVOICE_1",
                        "attr": "$.message.catalog.providers[*].items[*].xinput.form.data.gstr1B2bInvoice_1.type",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_FIELD_GSTR_B2B_CDNR_1",
                        "attr": "$.message.catalog.providers[*].items[*].xinput.form.data.gstr1B2bCdnr_1.type",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_FIELD_GSTR_B2B_INVOICES_1",
                        "attr": "$.message.catalog.providers[*].items[*].xinput.form.data.gstr2aB2bInvoices_1.type",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_FIELD_GSTR_3B_SUMMARY_1",
                        "attr": "$.message.catalog.providers[*].items[*].xinput.form.data.gstr3bSummary_1.type",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_FIELD_BANK_STATEMENT_FILES",
                        "attr": "$.message.catalog.providers[*].items[*].xinput.form.data.bankStatementFiles_1.type",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_FIELD_BANK_NAME",
                        "attr": "$.message.catalog.providers[*].items[*].xinput.form.data.bankName_1.type",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_FIELD_MIME_TYPE",
                        "attr": "$.message.catalog.providers[*].items[*].xinput.form.data.mimeType_1.type",
                        "_RETURN_": "attr are present"
                      }
                    ]
                  },
                  {
                    "_NAME_": "BUSINESS_AND_FINANCIAL_DOCUMENTS_FIELDS",
                    "usecasepath": "$.message.catalog.providers[*].items[*].xinput.head.descriptor.code",
                    "formHeading": [
                      "BUSINESS_AND_FINANCIAL_DOCUMENTS"
                    ],
                    "_CONTINUE_": "!(usecasepath all in  formHeading)",
                    "_RETURN_": [
                      {
                        "_NAME_": "REQUIRED_FIELD_FINANCIAL_STATEMENTS",
                        "attr": "$.message.catalog.providers[*].items[*].xinput.form.data.financialStatements.type",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_FIELD_SHAREHOLDING_PATTERN",
                        "attr": "$.message.catalog.providers[*].items[*].xinput.form.data.shareholdingPattern.type",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_FIELD_ITR",
                        "attr": "$.message.catalog.providers[*].items[*].xinput.form.data.itr.type",
                        "_RETURN_": "attr are present"
                      }
                    ]
                  },
                  {
                    "_NAME_": "TERM_LOAN_FIELDS",
                    "usecasepath": "$.message.catalog.providers[*].items[*].xinput.head.descriptor.code",
                    "formHeading": [
                      "PERSONAL_INFORMATION_TERM"
                    ],
                    "_CONTINUE_": "!(usecasepath all in formHeading)",
                    "_RETURN_": [
                      {
                        "_NAME_": "REQUIRED_FIELD_PAN",
                        "attr": "$.message.catalog.providers[*].items[*].xinput.form.data.pan.type",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_FULL_NAME",
                        "attr": "$.message.catalog.providers[*].items[*].xinput.form.data.fullName.type",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_DOB",
                        "attr": "$.message.catalog.providers[*].items[*].xinput.form.data.dob.type",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_CONSTITUTION",
                        "attr": "$.message.catalog.providers[*].items[*].xinput.form.data.constitution.type",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_BUSINESS_PAN",
                        "attr": "$.message.catalog.providers[*].items[*].xinput.form.data.businessPan.type",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_DOI",
                        "attr": "$.message.catalog.providers[*].items[*].xinput.form.data.doi.type",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_NATURE_OF_BUSINESS",
                        "attr": "$.message.catalog.providers[*].items[*].xinput.form.data.natureOfBusiness.type",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_ANNUAL_TURNOVER",
                        "attr": "$.message.catalog.providers[*].items[*].xinput.form.data.annualTurnover.type",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_BUSINESS_PINCODE",
                        "attr": "$.message.catalog.providers[*].items[*].xinput.form.data.businessPincode.type",
                        "_RETURN_": "attr are present"
                      }
                    ]
                  },
                  {
                    "_NAME_": "TERM_LOAN_FIELDS_GST",
                    "usecasepath": "$.message.catalog.providers[*].items[*].xinput.head.descriptor.code",
                    "formHeading": [
                      "PERSONAL_INFORMATION_TERM_GST"
                    ],
                    "_CONTINUE_": "!(usecasepath all in formHeading)",
                    "_RETURN_": [
                      {
                        "_NAME_": "REQUIRED_FIELD_BUREAU_CONSENT",
                        "attr": "$.message.catalog.providers[*].items[*].xinput.form.data.bureauConsent.type",
                        "_RETURN_": "attr are present"
                      }
                    ]
                  },
                  {
                    "_NAME_": "LAMF_FIELDS",
                    "usecasepath": "$.message.catalog.providers[*].items[*].xinput.head.descriptor.code",
                    "formHeading": [
                      "PERSONAL_INFORMATION_LAMF"
                    ],
                    "_CONTINUE_": "!(usecasepath all in  formHeading)",
                    "_RETURN_": [
                      {
                        "_NAME_": "REQUIRED_FIELD_PAN",
                        "attr": "$.message.catalog.providers[*].items[*].xinput.form.data.pan.type",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_FIELD_FULL_NAME",
                        "attr": "$.message.catalog.providers[*].items[*].xinput.form.data.fullName.type",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_FIELD_CONSTITUION",
                        "attr": "$.message.catalog.providers[*].items[*].xinput.form.data.constitution.type",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_FIELD_GENDER",
                        "attr": "$.message.catalog.providers[*].items[*].xinput.form.data.gender.type",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_FIELD_EMPLOYMENT_TYPE",
                        "attr": "$.message.catalog.providers[*].items[*].xinput.form.data.employmentType.type",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_FIELD_DOB",
                        "attr": "$.message.catalog.providers[*].items[*].xinput.form.data.dob.type",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_FIELD_ANNUAL_INCOME",
                        "attr": "$.message.catalog.providers[*].items[*].xinput.form.data.annualIncome.type",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_FIELD_MOBILE_NUMBER",
                        "attr": "$.message.catalog.providers[*].items[*].xinput.form.data.mobileNumber.type",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_FIELD_EMAIL_ID",
                        "attr": "$.message.catalog.providers[*].items[*].xinput.form.data.emailId.type",
                        "_RETURN_": "attr are present"
                      }
                    ]
                  }
                ]
              }
            ]
          },
          {
            "_NAME_": "VALID_ENUM_ITEMS",
            "_RETURN_": [
              {
                "_NAME_": "VALID_ITEM_CODE",
                "attr": "$.message.catalog.providers[*].items[*].descriptor.code",
                "enumList": [
                  "LOAN"
                ],
                "_CONTINUE_": "!(attr are present)",
                "_RETURN_": "attr all in enumList"
              },
              {
                "_NAME_": "VALID_HEAD_CODE",
                "attr": "$.message.catalog.providers[*].items[*].xinput.head.descriptor.code",
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
      },
      {
        "_NAME_": "ON_SEARCH_FULFILLMENTS",
        "_RETURN_": [
          {
            "_NAME_": "REQUIRED_FULFILLMENT_ITEMS",
            "_RETURN_": [
              {
                "_NAME_": "REQUIRED_FULFILLMENT_ID",
                "attr": "$.message.catalog.providers[*].fulfillments[*].id",
                "_RETURN_": "attr are present"
              },
              {
                "_NAME_": "REQUIRED_FULFILLMENT_TYPE",
                "attr": "$.message.catalog.providers[*].fulfillments[*].type",
                "_RETURN_": "attr are present"
              }
            ]
          },
          {
            "_NAME_": "VALID_FULFILLMENT_ITEMS",
            "_RETURN_": [
              {
                "_NAME_": "VALID_FULFILLMENT_TYPE",
                "attr": "$.message.catalog.providers[*].fulfillments[*].type",
                "enumList": [
                  "ONLINE",
                  "SEMI_ONLINE",
                  "BASE_ORDER"
                ],
                "_CONTINUE_": "!(attr are present)",
                "_RETURN_": "(attr all in enumList)"
              }
            ]
          },
          {
            "_NAME_": "VALID_FULFILLMENT_TAGS",
            "_SCOPE_": "$.message.catalog.providers[*].fulfillments[*][?(@.type != 'BASE_ORDER')]",
            "_RETURN_": [
              {
                "_NAME_": "REQUIRED_FULFILLMENT_TAGS",
                "validTags": [
                  "CHECKLISTS"
                ],
                "tagPath": "$.message.catalog.providers[*].fulfillments[*].tags[*].descriptor.code",
                "_CONTINUE_": "!(tagPath are present)",
                "_RETURN_": "tagPath all in validTags"
              },
              {
                "_NAME_": "REQUIRED_CHECKLISTS_ITEM",
                "_SCOPE_": "$.message.catalog.providers[*].fulfillments[*].tags[?(@.descriptor.code == 'CHECKLISTS')]",
                "subTags": "$.list[*].descriptor.code",
                "validValues": [
                  "PERSONAL_INFORMATION",
                  "CONSENT_APPROVAL",
                  "SET_LOAN_AMOUNT",
                  "KYC",
                  "KYC_OFFLINE",
                  "EMANDATE",
                  "LOAN_AGREEMENT",
                  "ACCOUNT_MONITORING",
                  "ORGANIZATION_INFORMATION",
                  "INDIVIDUAL_KYC",
                  "ENTITY_KYC",
                  "MERCHANT_AND_PRDOUCT_DETAILS",
                  "SET_DOWN_PAYMENT",
                  "ESIGN",
                  "BANK_STATEMENT_AND_GST_RETURNS",
                  "BUSINESS_AND_FINANCIAL_DOCUMENTS",
                  "BUSINESS_KYC",
                  "PERSONAL_DISCUSSION",
                  "PHYSICAL_VERIFICATION",
                  "ENACH",
                  "PROCESSING_FEE",
                  "MANUAL_VERIFICATION",
                  "LIEN_MARKING",
                  "PERSONAL_INFORMATION_TERM",
                  "PERSONAL_INFORMATION_LAMF",
                  "PERSONAL_INFORMATION_TERM_GST",
                  "KYC_OFFLINE",
                  "JOURNEY_OFFLINE",
                  "PERSONAL_INFORMATION_BUSINESS_TERM_GST",
                  "PERSONAL_INFORMATION_BUSINESS_TERM",
                  "INVOICE_UPLOAD"
                ],
                "_RETURN_": "subTags all in validValues"
              }
            ]
          }
        ]
      },
      {
        "_NAME_": "ON_SEARCH_PAYMENTS",
        "_RETURN_": [
          {
            "_NAME_": "REQUIRED_PAYMENT_ITEMS",
            "_RETURN_": [
              {
                "_NAME_": "REQUIRED_PAYMENT_TYPE",
                "attr": "$.message.catalog.providers[*].payments[*].type",
                "_RETURN_": "attr are present"
              },
              {
                "_NAME_": "REQUIRED_PAYMENT_ID",
                "attr": "$.message.catalog.providers[*].payments[*].id",
                "_RETURN_": "attr are present"
              },
              {
                "_NAME_": "REQUIRED_PAYMENT_STATUS",
                "attr": "$.message.catalog.providers[*].payments[*].status",
                "_RETURN_": "attr are present"
              },
              {
                "_NAME_": "REQUIRED_PAYMENT_COLLECTED_BY",
                "attr": "$.message.catalog.providers[*].payments[*].collected_by",
                "_RETURN_": "attr are present"
              },
              {
                "_NAME_": "REQUIRED_PAYMENT_TIME_LABEL",
                "attr": "$.message.catalog.providers[*].payments[*].time.label",
                "_RETURN_": "attr are present"
              }
            ]
          },
          {
            "_NAME_": "VALID_PAYMENT_ITEMS",
            "_RETURN_": [
              {
                "_NAME_": "VALID_PAYMENT_TYPE",
                "attr": "$.message.catalog.providers[*].payments[*].type",
                "_CONTINUE_": "!(attr are present)",
                "enumList": [
                  "ON_ORDER",
                  "ON_FULFILLMENT",
                  "POST_FULFILLMENT",
                  "PRE_ORDER"
                ],
                "_RETURN_": "attr all in enumList"
              },
              {
                "_NAME_": "VALID_PAYMENT_STATUS",
                "attr": "$.message.catalog.providers[*].payments[*].status",
                "_CONTINUE_": "!(attr are present)",
                "enumList": [
                  "NOT-PAID",
                  "PAID",
                  "DEFERRED",
                  "DELAYED"
                ],
                "_RETURN_": "attr all in enumList"
              },
              {
                "_NAME_": "VALID_PAYMENT_COLLECTOR",
                "attr": "$.message.catalog.providers[*].payments[*].collected_by",
                "_CONTINUE_": "!(attr are present)",
                "enumList": [
                  "BPP",
                  "CONSUMER",
                  "BAP"
                ],
                "_RETURN_": "attr all in enumList"
              },
              {
                "_NAME_": "VALID_PAYMENT_LABEL",
                "attr": "$.message.catalog.providers[*].payments[*].time.label",
                "_CONTINUE_": "!(attr are present)",
                "enumList": [
                  "INSTALLMENT",
                  "LOAN_DISBURSMENT"
                ],
                "_RETURN_": "enumList all in attr"
              }
            ]
          }
        ]
      },
      {
        "_NAME_": "ON_SEARCH_TAGS",
        "action": [
          "on_search"
        ],
        "_RETURN_": [
          {
            "_NAME_": "REQUIRED_PAYMENT_TAGS",
            "validTags": [
              "BAP_TERMS",
              "BPP_TERMS"
            ],
            "tagPath": "$.message.catalog.tags[*].descriptor.code",
            "_CONTINUE_": "!(tagPath are present)",
            "_RETURN_": "tagPath all in validTags"
          },
          {
            "_NAME_": "REQUIRED_BPP_TERMS",
            "_SCOPE_": "$.message.catalog.tags[?(@.descriptor.code == 'BPP_TERMS')]",
            "subTags": "$.list[*].descriptor.code",
            "validValues": [
              "STATIC_TERMS",
              "OFFLINE_CONTRACT"
            ],
            "_RETURN_": "subTags all in validValues"
          }
        ]
      },
      {
        "_NAME_": "ON_SEARCH_PROVIDER_TAGS",
        "action": [
          "on_search"
        ],
        "_RETURN_": [
          {
            "_NAME_": "VALID_PROVODER_TAGS",
            "validTags": [
              "CONTACT_INFO",
              "LSP_INFO"
            ],
            "tagPath": "$.message.catalog.providers[*].tags[*].descriptor.code",
            "_CONTINUE_": "!(tagPath are present)",
            "_RETURN_": "tagPath all in validTags"
          },
          {
            "_NAME_": "REQUIRED_CONTACT_INFO",
            "_SCOPE_": "$.message.catalog.providers[*].tags[?(@.descriptor.code == 'CONTACT_INFO')]",
            "subTags": "$.list[*].descriptor.code",
            "validValues": [
              "GRO_NAME",
              "GRO_EMAIL",
              "GRO_CONTACT_NUMBER",
              "CUSTOMER_SUPPORT_LINK",
              "CUSTOMER_SUPPORT_CONTACT_NUMBER",
              "CUSTOMER_SUPPORT_EMAIL",
              "GRO_DESIGNATION",
              "GRO_ADDRESS"
            ],
            "_RETURN_": "subTags all in validValues"
          },
          {
            "_NAME_": "REQUIRED_LSP_INFO",
            "_SCOPE_": "$.message.catalog.providers[*].tags[?(@.descriptor.code == 'LSP_INFO')]",
            "subTags": "$.list[*].descriptor.code",
            "validValues": [
              "LSP_NAME",
              "LSP_EMAIL",
              "LSP_CONTACT_NUMBER",
              "LSP_ADDRESS"
            ],
            "_RETURN_": "subTags all in validValues"
          }
        ]
      },
      {
        "_NAME_": "ON_SEARCH_ITEM_TAGS",
        "action": [
          "on_search"
        ],
        "validTags": [
          "LOAN_INFO",
          "LOAN_OFFER"
        ],
        "usecasepath": "$.message.catalog.providers[*].items[*].tags[*].descriptor.code",
        "_CONTINUE_": "!(usecasepath are present && usecasepath all in validTags)",
        "_RETURN_": [
          {
            "_NAME_": "REQUIRED_LOAN_INFO_TAG_GROUP",
            "_SCOPE_": "$.message.catalog.providers[*].items[*].tags[?(@.descriptor.code == 'LOAN_INFO')]",
            "subTags": "$.list[*].descriptor.code",
            "validValues": [
              "INTEREST_RATE",
              "TERM",
              "INTEREST_RATE_TYPE",
              "APPLICATION_FEE",
              "FORECLOSURE_FEE",
              "INTEREST_RATE_CONVERSION_CHARGE",
              "DELAY_PENALTY_FEE",
              "OTHER_PENALTY_FEE",
              "ANNUAL_PERCENTAGE_RATE",
              "REPAYMENT_FREQUENCY",
              "NUMBER_OF_INSTALLMENTS",
              "TNC_LINK",
              "COOL_OFF_PERIOD",
              "INSTALLMENT_AMOUNT",
              "KFS_LINK",
              "INVOICE_NUMBER",
              "WORKING_CAPITAL_LIMIT",
              "INSURANCE_CHARGES",
              "RATE_ANNUALISED_PENAL_CHARGES",
              "KYC_MODE",
              "CO_APPLICANT",
              "MINIMUM_DOWNPAYMENT",
              "SUBVENTION_RATE",
              "SELLER_SUBVENTION_RATE"
            ],
            "_RETURN_": "subTags all in validValues"
          },
          {
            "_NAME_": "REQUIRED_LOAN_OFFER_TAGS",
            "_SCOPE_": "$.message.catalog.providers[*].items[*].tags[?(@.descriptor.code == 'LOAN_OFFER')]",
            "subTags": "$.list[*].descriptor.code",
            "validValues": [
              "PRINCIPAL_AMOUNT",
              "INTEREST_AMOUNT",
              "PROCESSING_FEE",
              "OTHER_UPFRONT_CHARGES",
              "INSURANCE_CHARGES",
              "NET_DISBURSED_AMOUNT",
              "OTHER_CHARGES",
              "OFFER_VALIDITY",
              "WORKING_CAPITAL_LIMIT",
              "CURRENT_UTLIZATION",
              "MINIMUM_DOWNPAYMENT",
              "SUBVENTION_RATE",
              "SELLER_SUBVENTION_RATE",
              "WORKING_CAPITAL_LIMIT",
              "CURRENT_UTILIZATION"
            ],
            "_RETURN_": "subTags all in validValues"
          }
        ]
      }
    ]
  }
}
```