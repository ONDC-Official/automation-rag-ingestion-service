---
action: on_status
domain: ONDC:FIS12
version: 2.3.0
numTests: 9
generated: 2026-04-14
---

```json
{
  "_TESTS_": {
    "on_status": [
      {
        "_NAME_": "ON_STATUS_CONTEXT",
        "action": [
          "on_status"
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
        "_NAME_": "REQUIRED_ORDER_ITEMS",
        "usecasepath": "$.message.order.id",
        "_CONTINUE_": "!(usecasepath are present)",
        "_RETURN_": [
          {
            "_NAME_": "REQUIRED_ORDER_ID",
            "attr": "$.message.order.id",
            "_RETURN_": "attr are present"
          },
          {
            "_NAME_": "REQUIRED_ORDER_STATUS",
            "attr": "$.message.order.status",
            "_RETURN_": "attr are present"
          },
          {
            "_NAME_": "REQUIRED_ORDER_CREATED_AT",
            "attr": "$.message.order.created_at",
            "_RETURN_": "attr are present"
          },
          {
            "_NAME_": "REQUIRED_ORDER_UPDATED_AT",
            "attr": "$.message.order.updated_at",
            "_RETURN_": "attr are present"
          },
          {
            "_NAME_": "CREATED_AT_UPDATED_AT_EQUALITY",
            "created_at": "$.message.order.created_at",
            "updated_at": "$.message.order.updated_at",
            "_RETURN_": "created_at equal to updated_at"
          }
        ]
      },
      {
        "_NAME_": "ON_SELECT_PROVIDER",
        "usecasepath": "$.message.order.provider.id",
        "_CONTINUE_": "!(usecasepath are present)",
        "_RETURN_": [
          {
            "_NAME_": "ON_SELECT_PROVIDER_ID",
            "attr": "$.message.order.provider.id",
            "_RETURN_": "attr are present"
          },
          {
            "_NAME_": "ON_SELECT_PROVIDER_NAME",
            "attr": "$.message.order.provider.descriptor.name",
            "_RETURN_": "attr are present"
          },
          {
            "_NAME_": "ON_SELECT_PROVIDER_IMAGES_URL",
            "attr": "$.message.order.provider.descriptor.images[*].url",
            "_RETURN_": "attr are present"
          },
          {
            "_NAME_": "ON_SELECT_PROVIDER_IMAGES_SIZE_TYPE",
            "attr": "$.message.order.provider.descriptor.images[*].size_type",
            "_RETURN_": "attr are present"
          }
        ]
      },
      {
        "_NAME_": "ON_SELECT_PROVIDER_TAGS",
        "action": [
          "on_select"
        ],
        "_RETURN_": [
          {
            "_NAME_": "VALID_PROVODER_TAGS",
            "validTags": [
              "CONTACT_INFO",
              "LSP_INFO"
            ],
            "tagPath": "$.message.order.provider.tags[*].descriptor.code",
            "_CONTINUE_": "!(tagPath are present)",
            "_RETURN_": "tagPath all in validTags"
          },
          {
            "_NAME_": "REQUIRED_CONTACT_INFO",
            "_SCOPE_": "$.message.order.provider.tags[?(@.descriptor.code == 'CONTACT_INFO')]",
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
            "_SCOPE_": "$.message.order.provider.tags[?(@.descriptor.code == 'LSP_INFO')]",
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
        "_NAME_": "ON_STATUS_ITEMS",
        "_RETURN_": [
          {
            "_NAME_": "REQUIRED_ITEMS",
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
                "_NAME_": "REQUIRED_ITEM_DESCRIPTOR_CODE",
                "attr": "$.message.order.items[*].descriptor.code",
                "_RETURN_": "attr are present"
              },
              {
                "_NAME_": "REQUIRED_ITEM_CATEGORY_ID",
                "attr": "$.message.order.items[*].category_ids[*]",
                "_RETURN_": "attr are present"
              },
              {
                "_NAME_": "ON_SEARCH_ITEM_PRICE_CURRENCY",
                "attr": "$.message.order.items[*].price.currency",
                "_RETURN_": "attr are present"
              },
              {
                "_NAME_": "ON_SEARCH_ITEM_PRICE_VALUE",
                "attr": "$.message.order.items[*].price.value",
                "_RETURN_": "attr are present"
              },
              {
                "_NAME_": "ON_SELECT_ITEM_FULFILLMENT_IDS",
                "attr": "$.message.order.items[*].fulfillment_ids[*]",
                "_RETURN_": "attr are present"
              },
              {
                "_NAME_": "REQUIRED_XINPUT_FIELDS",
                "usecasepath": "$.message.order.items[*].xinput.form_response.submission_id",
                "_CONTINUE_": "!(usecasepath are present)",
                "_RETURN_": [
                  {
                    "_NAME_": "REQUIRED_XINPUT_ITEMS",
                    "_RETURN_": [
                      {
                        "_NAME_": "REQUIRED_FORM_ID",
                        "attr": "$.message.order.items[*].xinput.form.id",
                        "_RETURN_": "attr are present"
                      },
                      {
                        "_NAME_": "REQUIRED_FORM_RESPONSE",
                        "useCasePath1": "$.message.order.items[*].xinput.form_response.status",
                        "_CONTINUE_": "!(useCasePath1 are present)",
                        "_RETURN_": [
                          {
                            "_NAME_": "REQUIRED_FORM_STATUS",
                            "attr": "$.message.order.items[*].xinput.form_response.status",
                            "_RETURN_": "attr are present"
                          },
                          {
                            "_NAME_": "REQUIRED_FORM_SUBMISSION_ID",
                            "attr": "$.message.order.items[*].xinput.form_response.status",
                            "_RETURN_": "attr are present"
                          }
                        ]
                      },
                      {
                        "_NAME_": "REQUIRED_SUBMISSION_ID",
                        "attr": "$.message.order.items[*].xinput.form_response.submission_id",
                        "_CONTINUE_": "!(attr are present)",
                        "_RETURN_": "attr are present"
                      }
                    ]
                  }
                ]
              }
            ]
          }
        ]
      },
      {
        "_NAME_": "ON_SELECT_ITEM_TAGS",
        "action": [
          "on_select"
        ],
        "validTags": [
          "LOAN_INFO",
          "LOAN_OFFER"
        ],
        "usecasepath": "$.message.order.items[*].tags[*].descriptor.code",
        "_CONTINUE_": "!(usecasepath are present && usecasepath all in validTags)",
        "_RETURN_": [
          {
            "_NAME_": "REQUIRED_LOAN_INFO",
            "_SCOPE_": "$.message.order.items[*].tags[?(@.descriptor.code == 'LOAN_INFO')]",
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
            "_NAME_": "REQUIRED_LOAN_OFFER",
            "_SCOPE_": "$.message.order.items[*].tags[?(@.descriptor.code == 'LOAN_OFFER')]",
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
      },
      {
        "_NAME_": "ON_STATUS_FULFILLMENTS",
        "_RETURN_": [
          {
            "_NAME_": "REQUIRED_FULFILLMENT_ITEMS",
            "_RETURN_": [
              {
                "_NAME_": "REQUIRED_FULFILLMENT_ID",
                "attr": "$.message.order.fulfillments[*].id",
                "_RETURN_": "attr are present"
              },
              {
                "_NAME_": "REQUIRED_FULFILLMENT_TYPE",
                "attr": "$.message.order.fulfillments[*].type",
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
                "_NAME_": "REQUIRED_CUSTOMER_NAME",
                "attr": "$.message.order.fulfillments[*].customer.person.name",
                "_CONTINUE_": "!(attr are present)",
                "_RETURN_": "attr are present"
              },
              {
                "_NAME_": "REQUIRED_CUSTOMER_CONTACT_DETAILS",
                "attr": "$.message.order.fulfillments[*].customer.contact.phone",
                "_CONTINUE_": "!(attr are present)",
                "_RETURN_": [
                  {
                    "_NAME_": "REQUIRED_CUSTOMER_CONTACT_NUMBER",
                    "attr": "$.message.order.fulfillments[*].customer.contact.phone",
                    "_RETURN_": "attr are present"
                  },
                  {
                    "_NAME_": "REQUIRED_CUSTOMER_CONTACT_EMAIL",
                    "attr": "$.message.order.fulfillments[*].customer.contact.email",
                    "_RETURN_": "attr are present"
                  }
                ]
              },
              {
                "_NAME_": "REQUIRED_CUSTOMER_ORG_DETAILS",
                "attr": "$.message.order.fulfillments[*].customer.organization.address",
                "_CONTINUE_": "!(attr are present)",
                "_RETURN_": [
                  {
                    "_NAME_": "REQUIRED_ORG_ADDRESS",
                    "attr": "$.message.order.fulfillments[*].customer.organization.address",
                    "_RETURN_": "attr are present"
                  },
                  {
                    "_NAME_": "REQUIRED_ORG_STATE",
                    "attr": "$.message.order.fulfillments[*].customer.organization.state.name",
                    "_RETURN_": "attr are present"
                  },
                  {
                    "_NAME_": "REQUIRED_ORG_CITY",
                    "attr": "$.message.order.fulfillments[*].customer.organization.city.name",
                    "_RETURN_": "attr are present"
                  },
                  {
                    "_NAME_": "REQUIRED_ORG_CODE",
                    "attr": "$.message.order.fulfillments[*].customer.organization.city.code",
                    "_RETURN_": "attr are present"
                  },
                  {
                    "_NAME_": "REQUIRED_ORG_CONTACT_PHONE",
                    "attr": "$.message.order.fulfillments[*].customer.organization.contact.phone",
                    "_RETURN_": "attr are present"
                  },
                  {
                    "_NAME_": "REQUIRED_ORG_CONTACT_EMAIL",
                    "attr": "$.message.order.fulfillments[*].customer.organization.contact.email",
                    "_RETURN_": "attr are present"
                  }
                ]
              }
            ]
          },
          {
            "_NAME_": "VALID_FULFILLMENT_ITEMS",
            "_RETURN_": [
              {
                "_NAME_": "VALID_FULFILLMENT_TYPE",
                "attr": "$.message.order.fulfillments[*].type",
                "enumList": [
                  "ONLINE",
                  "SEMI_ONLINE",
                  "BASE_ORDER"
                ],
                "_CONTINUE_": "!(attr are present)",
                "_RETURN_": "(attr all in enumList)"
              },
              {
                "_NAME_": "VALID_FULFILLMENT_STATE_CODE",
                "attr": "$.message.order.fulfillments[*].state.descriptor.code",
                "enumList": [
                  "INITIATED",
                  "SANCTIONED",
                  "DISBURSED",
                  "CONSENT_REQUIRED",
                  "DELIVERED"
                ],
                "_CONTINUE_": "!(attr are present)",
                "_RETURN_": "attr all in enumList"
              }
            ]
          },
          {
            "_NAME_": "VALID_FULFILLMENT_TAGS",
            "_SCOPE_": "$.message.order.providers[*].fulfillments[*][?(@.type != 'BASE_ORDER')]",
            "_RETURN_": [
              {
                "_NAME_": "REQUIRED_FULFILLMENT_TAGS",
                "validTags": [
                  "CHECKLISTS"
                ],
                "tagPath": "$.message.order.fulfillments[*].tags[*].descriptor.code",
                "_CONTINUE_": "!(tagPath are present)",
                "_RETURN_": "tagPath all in validTags"
              },
              {
                "_NAME_": "REQUIRED_CHECKLISTS_ITEM",
                "_SCOPE_": "$.message.order.fulfillments[*].tags[?(@.descriptor.code == 'CHECKLISTS')]",
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
        "_NAME_": "ON_SELECT_QUOTE",
        "usecasepath": "$.message.order.quote.id",
        "_CONTINUE_": "!(usecasepath are present)",
        "_RETURN_": [
          {
            "_NAME_": "REQUIRED_COMMON_QUOTE_ITEMS",
            "_RETURN_": [
              {
                "_NAME_": "REQUIRED_QUOTE_ID",
                "attr": "$.message.order.quote.id",
                "_RETURN_": "attr are present"
              },
              {
                "_NAME_": "REQUIRED_QUOTE_PRICE_VALUE",
                "attr": "$.message.order.quote.price.value",
                "_RETURN_": "attr are present"
              },
              {
                "_NAME_": "REQUIRED_QUOTE_PRICE_CURRENCY",
                "attr": "$.message.order.quote.price.currency",
                "_RETURN_": "attr are present"
              },
              {
                "_NAME_": "REQUIRED_BREAKUP_TITLE",
                "attr": "$.message.order.quote.breakup[*].title",
                "_RETURN_": "attr are present"
              },
              {
                "_NAME_": "REQUIRED_BREAKUP_PRICE_VALUE",
                "attr": "$.message.order.quote.breakup[*].price.value",
                "_RETURN_": "attr are present"
              },
              {
                "_NAME_": "REQUIRED_BREAKUP_PRICE_CURRENCY",
                "attr": "$.message.order.quote.breakup[*].price.currency",
                "_RETURN_": "attr are present"
              },
              {
                "_NAME_": "REQUIRED_QUOTE_TTL",
                "attr": "$.message.order.quote.ttl",
                "_RETURN_": "attr are present"
              }
            ]
          },
          {
            "_NAME_": "VALID_COMMON_QUOTE_ITEMS",
            "_RETURN_": [
              {
                "_NAME_": "VALID_ENUM_BREAKUP_PRICE_CURRENCY",
                "attr": "$.message.order.quote.breakup[*].price.currency",
                "enumList": [
                  "INR"
                ],
                "_RETURN_": "attr any in enumList"
              },
              {
                "_NAME_": "VALID_ENUM_BREAKUP_TITLE",
                "attr": "$.message.order.quote.breakup[*].title",
                "enumList": [
                  "PRINCIPAL_AMOUNT",
                  "INTEREST_AMOUNT",
                  "PROCESSING_FEE",
                  "OTHER_UPFRONT_CHARGES",
                  "INSURANCE_CHARGES",
                  "NET_DISBURSED_AMOUNT",
                  "OTHER_CHARGES",
                  "WORKING_CAPITAL_LIMIT",
                  "CURRENT_UTLIZATION"
                ],
                "_RETURN_": "attr any in enumList"
              }
            ]
          }
        ]
      },
      {
        "_NAME_": "REQUIRED_ORDER_DOCUMENTS",
        "usecasepath": "$.message.order.documents[*].descriptor.code",
        "_CONTINUE_": "!(usecasepath are present)",
        "_RETURN_": [
          {
            "_NAME_": "REQUIRED_DOCUMENT_CODE",
            "attr": "$.message.order.documents[*].descriptor.code",
            "_RETURN_": "attr are present"
          },
          {
            "_NAME_": "REQUIRED_DOCUMENT_NAME",
            "attr": "$.message.order.documents[*].descriptor.name",
            "_RETURN_": "attr are present"
          },
          {
            "_NAME_": "REQUIRED_DOCUMENT_TYPE",
            "attr": "$.message.order.documents[*].mime_type",
            "_RETURN_": "attr are present"
          },
          {
            "_NAME_": "REQUIRED_DOCUMENT_URL",
            "attr": "$.message.order.documents[*].url",
            "_RETURN_": "attr are present"
          },
          {
            "_NAME_": "VALID_DESCRIPTOR_CODE",
            "attr": "$.message.order.documents[*].descriptor.code",
            "enumList": [
              "LOAN_AGREEMENT",
              "LOAN_CANCELLATION"
            ],
            "_RETURN_": "attr all in enumList"
          }
        ]
      }
    ]
  }
}
```