---
action: on_search
domain: ONDC:FIS12
version: 2.0.2
numTests: 8
generated: 2026-03-18
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
          "2.0.2"
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
                "_NAME_": "REQUIRED_CONTEXT_BPP_ID",
                "attr": "$.context.bpp_id",
                "var_search": [
                  "search"
                ],
                "_CONTINUE_": "(action all in var_search)",
                "_RETURN_": "attr are present"
              },
              {
                "_NAME_": "REQUIRED_CONTEXT_BPP_URI",
                "attr": "$.context.bpp_uri",
                "var_search": [
                  "search"
                ],
                "_CONTINUE_": "(action all in var_search)",
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
                "_RETURN_": "attr any in enumList"
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
                  "^\\*$"
                ],
                "_CONTINUE_": "!(attr are present)",
                "_RETURN_": "attr follow regex reg"
              },
              {
                "_NAME_": "REGEX_CONTEXT_TIMESTAMP",
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
                  "^https?://([a-zA-Z0-9-]+(\\.[a-zA-Z0-9-]+)*|localhost)(:\\d+)?(/.*)?$"
                ],
                "_CONTINUE_": "!(attr are present)",
                "_RETURN_": "attr follow regex reg"
              },
              {
                "_NAME_": "REGEX_CONTEXT_TTL",
                "attr": "$.context.ttl",
                "reg": [
                  "^P(?=\\\\d|T\\\\d)(\\\\d+Y)?(\\\\d+M)?(\\\\d+D)?(T(\\\\d+H)?(\\\\d+M)?(\\\\d+S)?)?$"
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
        "_NAME_": "ON_SEARCH_CATEGORIES",
        "_RETURN_": [
          {
            "_NAME_": "REQUIRED_CATEGORIES_NAME",
            "attr": "$.message.catalog.providers[*].categories[*].descriptor.name",
            "_RETURN_": "attr are present"
          },
          {
            "_NAME_": "REQUIRED_CATEGORIES_CODE",
            "attr": "$.message.catalog.providers[*].categories[*].descriptor.code",
            "_RETURN_": "attr are present"
          },
          {
            "_NAME_": "VALID_ENUM_CATEGORIES_CODE",
            "attr": "$.message.catalog.providers[*].categories[*].descriptor.code",
            "enumList": [
              "PERSONAL_LOAN",
              "BUREAU_LOAN",
              "AA_PERSONAL_LOAN",
              "GOLD_LOAN",
              "AA_LOAN",
              "LOAN",
              "PERSONAL_INFORMATION"
            ],
            "_RETURN_": "attr all in enumList"
          },
          {
            "_NAME_": "REQUIRED_CATEGORIES_ID",
            "attr": "$.message.catalog.providers[*].categories[*].id",
            "_RETURN_": "attr are present"
          },
          {
            "_NAME_": "REQUIRED_CATEGORIES_PARENT_ID",
            "attr": "$.message.catalog.providers[*].categories[*].parent_category_id",
            "category_code_path": "$.message.catalog.providers[*].categories[*].descriptor.code",
            "var_category_code": [
              "BUREAU_LOAN",
              "AA_LOAN",
              "PERSONAL_LOAN",
              "AA_PERSONAL_LOAN",
              "GOLD_LOAN"
            ],
            "_CONTINUE_": "(var_category_code any in category_code_path)",
            "_RETURN_": "attr are present"
          }
        ]
      },
      {
        "_NAME_": "ON_SEARCH_PROVIDER",
        "_RETURN_": [
          {
            "_NAME_": "REQUIRED_PROVIDER_ID",
            "attr": "$.message.catalog.providers[*].id",
            "_RETURN_": "attr are present"
          },
          {
            "_NAME_": "REQUIRED_PROVIDER_NAME",
            "attr": "$.message.catalog.providers[*].descriptor.name",
            "_RETURN_": "attr are present"
          },
          {
            "_NAME_": "REQUIRED_PROVIDER_IMAGES_URL",
            "attr": "$.message.catalog.providers[*].descriptor.images[*].url",
            "_RETURN_": "attr are present"
          },
          {
            "_NAME_": "REQUIRED_PROVIDER_IMAGES_SIZE_TYPE",
            "attr": "$.message.catalog.providers[*].descriptor.images[*].size_type",
            "_RETURN_": "attr are present"
          }
        ]
      },
      {
        "_NAME_": "ON_SEARCH_PROVIDER_CONTACT_INFO",
        "_RETURN_": [
          {
            "_NAME_": "REQUIRED_CONTACT_INFO_TAG_GROUP",
            "validTags": [
              "CONTACT_INFO"
            ],
            "tagPath": "$.message.catalog.providers[*].tags[*].descriptor.code",
            "_RETURN_": "tagPath any in validTags"
          },
          {
            "_NAME_": "REQUIRED_CONTACT_INFO_LIST",
            "_SCOPE_": "$.message.catalog.providers[*].tags[?(@.descriptor.code=='CONTACT_INFO')]",
            "subTags": "$.list[*].descriptor.code",
            "validValues": [
              "GRO_NAME",
              "GRO_EMAIL",
              "GRO_CONTACT_NUMBER",
              "CUSTOMER_SUPPORT_LINK",
              "CUSTOMER_SUPPORT_CONTACT_NUMBER",
              "CUSTOMER_SUPPORT_EMAIL"
            ],
            "_CONTINUE_": "!(subTags are present)",
            "_RETURN_": "subTags all in validValues"
          }
        ]
      },
      {
        "_NAME_": "ON_SEARCH_PROVIDER_LSP_INFO",
        "_RETURN_": [
          {
            "_NAME_": "REQUIRED_LSP_INFO_TAG_GROUP",
            "validTags": [
              "LSP_INFO"
            ],
            "tagPath": "$.message.catalog.providers[*].tags[*].descriptor.code",
            "_RETURN_": "tagPath any in validTags"
          },
          {
            "_NAME_": "REQUIRED_LSP_INFO_LIST",
            "_SCOPE_": "$.message.catalog.providers[*].tags[?(@.descriptor.code=='LSP_INFO')]",
            "subTags": "$.list[*].descriptor.code",
            "validValues": [
              "LSP_NAME",
              "LSP_EMAIL",
              "LSP_CONTACT_NUMBER",
              "LSP_ADDRESS"
            ],
            "_CONTINUE_": "!(subTags are present)",
            "_RETURN_": "subTags all in validValues"
          }
        ]
      },
      {
        "_NAME_": "ON_SEARCH_PAYMENT",
        "_RETURN_": [
          {
            "_NAME_": "REQUIRED_PAYMENT_COLLECTED_BY",
            "attr": "$.message.catalog.providers[*].payments[*].collected_by",
            "_RETURN_": "attr are present"
          },
          {
            "_NAME_": "VALID_PAYMENT_COLLECTED_BY_ENUM",
            "attr": "$.message.catalog.providers[*].payments[*].collected_by",
            "enumList": [
              "BPP",
              "BAP"
            ],
            "_RETURN_": "attr all in enumList"
          },
          {
            "_NAME_": "REQUIRED_BUYER_FINDER_FEES_TAG",
            "validTags": [
              "BUYER_FINDER_FEES"
            ],
            "tagPath": "$.message.catalog.providers[*].payments[*].tags[*].descriptor.code",
            "_RETURN_": "tagPath any in validTags"
          },
          {
            "_NAME_": "REQUIRED_BUYER_FINDER_FEES_LIST",
            "_SCOPE_": "$.message.catalog.providers[*].payments[*].tags[?(@.descriptor.code=='BUYER_FINDER_FEES')]",
            "subTags": "$.list[*].descriptor.code",
            "validValues": [
              "BUYER_FINDER_FEES_TYPE",
              "BUYER_FINDER_FEES_PERCENTAGE"
            ],
            "_CONTINUE_": "!(subTags are present)",
            "_RETURN_": "subTags all in validValues"
          },
          {
            "_NAME_": "VALID_BUYER_FINDER_FEES_TYPE_VALUE",
            "_SCOPE_": "$.message.catalog.providers[*].payments[*].tags[?(@.descriptor.code=='BUYER_FINDER_FEES')].list[?(@.descriptor.code=='BUYER_FINDER_FEES_TYPE')]",
            "attr": "$.value",
            "enumList": [
              "PERCENT_ANNUALIZED"
            ],
            "_RETURN_": "attr all in enumList"
          },
          {
            "_NAME_": "REQUIRED_SETTLEMENT_TERMS_TAG",
            "validTags": [
              "SETTLEMENT_TERMS"
            ],
            "tagPath": "$.message.catalog.providers[*].payments[*].tags[*].descriptor.code",
            "_RETURN_": "tagPath any in validTags"
          },
          {
            "_NAME_": "REQUIRED_SETTLEMENT_TERMS_LIST",
            "_SCOPE_": "$.message.catalog.providers[*].payments[*].tags[?(@.descriptor.code=='SETTLEMENT_TERMS')]",
            "subTags": "$.list[*].descriptor.code",
            "validValues": [
              "SETTLEMENT_WINDOW",
              "SETTLEMENT_BASIS",
              "MANDATORY_ARBITRATION",
              "COURT_JURISDICTION",
              "STATIC_TERMS",
              "OFFLINE_CONTRACT"
            ],
            "_CONTINUE_": "!(subTags are present)",
            "_RETURN_": "subTags all in validValues"
          }
        ]
      },
      {
        "_NAME_": "ON_SEARCH_ITEMS",
        "usecasepath": "$.message.catalog.providers[*].items[*].id",
        "_CONTINUE_": "!(usecasepath are present)",
        "_RETURN_": [
          {
            "_NAME_": "REQUIRED_ITEM_ID",
            "attr": "$.message.catalog.providers[*].items[*].id",
            "_RETURN_": "attr are present"
          },
          {
            "_NAME_": "REQUIRED_ITEM_CATEGORY_IDS",
            "attr": "$.message.catalog.providers[*].items[*].category_ids[*]",
            "_RETURN_": "attr are present"
          },
          {
            "_NAME_": "REQUIRED_ITEM_DESCRIPTOR_NAME",
            "attr": "$.message.catalog.providers[*].items[*].descriptor.name",
            "_RETURN_": "attr are present"
          },
          {
            "_NAME_": "REQUIRED_GENERAL_INFO_TAG_GROUP",
            "validTags": [
              "GENERAL_INFO"
            ],
            "tagPath": "$.message.catalog.providers[*].items[*].tags[*].descriptor.code",
            "_RETURN_": "tagPath any in validTags"
          },
          {
            "_NAME_": "REQUIRED_GENERAL_INFO_LIST",
            "_SCOPE_": "$.message.catalog.providers[*].items[*].tags[?(@.descriptor.code=='GENERAL_INFO')]",
            "subTags": "$.list[*].descriptor.code",
            "validValues": [
              "MIN_INTEREST_RATE",
              "MAX_INTEREST_RATE",
              "MIN_TENURE",
              "MAX_TENURE",
              "MIN_LOAN_AMOUNT",
              "MAX_LOAN_AMOUNT"
            ],
            "_CONTINUE_": "!(subTags are present)",
            "_RETURN_": "subTags all in validValues"
          },
          {
            "_NAME_": "REQUIRED_XINPUT",
            "attr": "$.message.catalog.providers[*].items[*].xinput.required",
            "_RETURN_": "attr are present"
          },
          {
            "_NAME_": "REQUIRED_XINPUT_FORM_URL",
            "attr": "$.message.catalog.providers[*].items[*].xinput.form.url",
            "_RETURN_": "attr are present"
          },
          {
            "_NAME_": "VALID_XINPUT_HEADINGS_ENUM",
            "attr": "$.message.catalog.providers[*].items[*].xinput.head.headings[*]",
            "enumList": [
              "KYC",
              "BUREAU_CONSENT",
              "AA_CONSENT",
              "Personal Information",
              "Set Loan Amount",
              "Know your Customer",
              "Account Information",
              "Emandate",
              "Loan Agreement",
              "PERSONAL_INFORMATION",
              "Loan Details"
            ],
            "_RETURN_": "attr all in enumList"
          }
        ]
      }
    ]
  }
}
```