---
action: on_select
domain: ONDC:FIS12
version: 2.3.0
numTests: 15
generated: 2026-04-15
---

```json
{
  "_TESTS_": {
    "on_select": [
      {
        "_NAME_": "ON_SELECT_CONTEXT",
        "action": [
          "on_select"
        ],
        "domain": [
          "ONDC:FIS12"
        ],
        "version": [
          "2.0.3"
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
        "_NAME_": "ON_SELECT_PROVIDER",
        "_RETURN_": [
          {
            "_NAME_": "REQUIRED_PROVIDER_ID",
            "attr": "$.message.order.provider.id",
            "_RETURN_": "attr are present"
          },
          {
            "_NAME_": "REQUIRED_PROVIDER_NAME",
            "attr": "$.message.order.provider.descriptor.name",
            "_RETURN_": "attr are present"
          }
        ]
      },
      {
        "_NAME_": "ON_SELECT_PROVIDER_LOCATIONS_GOLD",
        "item_code": "$.message.order.items[*].descriptor.code",
        "loan_type_match": [
          "LOAN"
        ],
        "locationspath": "$.message.order.provider.locations[*].id",
        "_CONTINUE_": "!(item_code any in loan_type_match) || !(locationspath are present)",
        "_RETURN_": [
          {
            "_NAME_": "REQUIRED_PROVIDER_LOCATIONS",
            "attr": "$.message.order.provider.locations[*].id",
            "_RETURN_": "attr are present"
          },
          {
            "_NAME_": "REQUIRED_PROVIDER_LOCATION_GPS",
            "attr": "$.message.order.provider.locations[*].gps",
            "_RETURN_": "attr are present"
          },
          {
            "_NAME_": "REQUIRED_PROVIDER_LOCATION_ADDRESS",
            "attr": "$.message.order.provider.locations[*].address",
            "_RETURN_": "attr are present"
          }
        ]
      },
      {
        "_NAME_": "ON_SELECT_PROVIDER_TAGS",
        "_RETURN_": [
          {
            "_NAME_": "REQUIRED_CONTACT_INFO_TAG_GROUP",
            "validTags": [
              "CONTACT_INFO"
            ],
            "tagPath": "$.message.order.provider.tags[*].descriptor.code",
            "_RETURN_": "tagPath any in validTags"
          },
          {
            "_NAME_": "REQUIRED_CONTACT_INFO_LIST",
            "_SCOPE_": "$.message.order.provider.tags[?(@.descriptor.code=='CONTACT_INFO')]",
            "subTags": "$.list[*].descriptor.code",
            "validValues": [
              "GRO_NAME",
              "GRO_EMAIL",
              "GRO_CONTACT_NUMBER",
              "GRO_DESIGNATION",
              "GRO_ADDRESS",
              "CUSTOMER_SUPPORT_LINK",
              "CUSTOMER_SUPPORT_CONTACT_NUMBER",
              "CUSTOMER_SUPPORT_EMAIL"
            ],
            "_CONTINUE_": "!(subTags are present)",
            "_RETURN_": "subTags all in validValues"
          },
          {
            "_NAME_": "REQUIRED_LSP_INFO_TAG_GROUP",
            "validTags": [
              "LSP_INFO"
            ],
            "tagPath": "$.message.order.provider.tags[*].descriptor.code",
            "_RETURN_": "tagPath any in validTags"
          },
          {
            "_NAME_": "REQUIRED_LSP_INFO_LIST",
            "_SCOPE_": "$.message.order.provider.tags[?(@.descriptor.code=='LSP_INFO')]",
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
        "_NAME_": "ON_SELECT_ITEMS_BASIC",
        "_RETURN_": [
          {
            "_NAME_": "REQUIRED_ITEM_ID",
            "attr": "$.message.order.items[*].id",
            "_RETURN_": "attr are present"
          },
          {
            "_NAME_": "REQUIRED_ITEM_DESCRIPTOR_CODE",
            "attr": "$.message.order.items[*].descriptor.code",
            "_RETURN_": "attr are present"
          },
          {
            "_NAME_": "VALID_ITEM_DESCRIPTOR_CODE_ENUM",
            "attr": "$.message.order.items[*].descriptor.code",
            "enumList": [
              "LOAN",
              "PERSONAL_LOAN",
              "CREDIT_CARD"
            ],
            "_RETURN_": "attr all in enumList"
          },
          {
            "_NAME_": "REQUIRED_ITEM_DESCRIPTOR_NAME",
            "attr": "$.message.order.items[*].descriptor.name",
            "_RETURN_": "attr are present"
          }
        ]
      },
      {
        "_NAME_": "ON_SELECT_1_AA_CONSENT_ITEMS",
        "_SCOPE_": "$.message.order.items[*].tags[?(@.descriptor.code=='PERSONAL_LOAN')]",
        "_RETURN_": [
          {
            "_NAME_": "REQUIRED_CONSENT_INFO_TAG",
            "validTags": [
              "CONSENT_INFO"
            ],
            "tagPath": "$.message.order.items[*].tags[*].descriptor.code",
            "_RETURN_": "tagPath any in validTags"
          },
          {
            "_NAME_": "REQUIRED_CONSENT_HANDLER",
            "_SCOPE_": "$.message.order.items[*].tags[?(@.descriptor.code=='CONSENT_INFO')]",
            "subTags": "$.list[*].descriptor.code",
            "validValues": [
              "CONSENT_HANDLER"
            ],
            "_RETURN_": "subTags any in validValues"
          }
        ]
      },
      {
        "_NAME_": "ON_SELECT_1_AA_CONSENT_XINPUT",
        "_SCOPE_": "$.message.order.items[*].tags[?(@.descriptor.code=='PERSONAL_LOAN')]",
        "_RETURN_": [
          {
            "_NAME_": "REQUIRED_XINPUT_FORM",
            "attr": "$.message.order.items[*].xinput.form.id",
            "_RETURN_": "attr are present"
          },
          {
            "_NAME_": "REQUIRED_XINPUT_FORM_RESPONSE",
            "attr": "$.message.order.items[*].xinput.form_response.status",
            "_RETURN_": "attr are present"
          },
          {
            "_NAME_": "VALID_XINPUT_FORM_RESPONSE_STATUS",
            "attr": "$.message.order.items[*].xinput.form_response.status",
            "enumList": [
              "PENDING",
              "SUCCESS"
            ],
            "_RETURN_": "attr all in enumList"
          },
          {
            "_NAME_": "REQUIRED_XINPUT_FORM_RESPONSE_SUBMISSION_ID",
            "attr": "$.message.order.items[*].xinput.form_response.submission_id",
            "_RETURN_": "attr are present"
          }
        ]
      },
      {
        "_NAME_": "ON_SELECT_CONSENT_XINPUT_CC",
        "_SCOPE_": "$.message.order.items[*].tags[?(@.descriptor.code=='PERSONAL_LOAN')]",
        "_RETURN_": [
          {
            "_NAME_": "REQUIRED_XINPUT_FORM",
            "attr": "$.message.order.items[*].xinput.form.id",
            "_RETURN_": "attr are present"
          }
        ]
      },
      {
        "_NAME_": "ON_SELECT_2_OFFER_ITEMS_PRICE",
        "usecasepath": "$.message.order.items[*].price.value",
        "_CONTINUE_": "!(usecasepath are present)",
        "_RETURN_": [
          {
            "_NAME_": "REQUIRED_ITEM_PRICE",
            "attr": "$.message.order.items[*].price.value",
            "_RETURN_": "attr are present"
          },
          {
            "_NAME_": "REQUIRED_ITEM_PRICE_CURRENCY",
            "attr": "$.message.order.items[*].price.currency",
            "enumList": [
              "INR"
            ],
            "_RETURN_": "attr all in enumList"
          }
        ]
      },
      {
        "_NAME_": "ON_SELECT_2_OFFER_LOAN_INFO",
        "usecasepath": "$.message.order.items[*].price.value",
        "_CONTINUE_": "!(usecasepath are present)",
        "_RETURN_": [
          {
            "_NAME_": "REQUIRED_LOAN_INFO_TAG_GROUP",
            "validTags": [
              "LOAN_INFO",
              "CONTACT_INFO",
              "LSP_INFO",
              "GENERAL_INFO"
            ],
            "tagPath": "$.message.order.items[*].tags[*].descriptor.code",
            "_RETURN_": "tagPath any in validTags"
          },
          {
            "_NAME_": "REQUIRED_LOAN_INFO_LIST_COMMON",
            "_SCOPE_": "$.message.order.items[*].tags[?(@.descriptor.code=='LOAN_INFO')]",
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
              "NUMBER_OF_INSTALLMENTS_OF_REPAYMENT",
              "TNC_LINK",
              "COOL_OFF_PERIOD",
              "INSTALLMENT_AMOUNT"
            ],
            "_CONTINUE_": "!(subTags are present)",
            "_RETURN_": "subTags any in validValues"
          },
          {
            "_NAME_": "REQUIRED_LOAN_INFO_LTV_RATIO_GOLD",
            "_SCOPE_": "$.message.order.items[?(@.descriptor.code=='LOAN')].tags[?(@.descriptor.code=='LOAN_INFO')]",
            "subTags": "$.list[*].descriptor.code",
            "validValues": [
              "LTV_RATIO"
            ],
            "_RETURN_": "subTags any in validValues"
          }
        ]
      },
      {
        "_NAME_": "ON_SELECT_2_OFFER_QUOTE",
        "usecasepath": "$.message.order.items[*].price.value",
        "_CONTINUE_": "!(usecasepath are present)",
        "_RETURN_": [
          {
            "_NAME_": "REQUIRED_QUOTE_ID",
            "attr": "$.message.order.quote.id",
            "_RETURN_": "attr are present"
          },
          {
            "_NAME_": "REQUIRED_QUOTE_PRICE",
            "_RETURN_": [
              {
                "_NAME_": "REQUIRED_QUOTE_PRICE_VALUE",
                "attr": "$.message.order.quote.price.value",
                "_RETURN_": "attr are present"
              },
              {
                "_NAME_": "REQUIRED_QUOTE_PRICE_CURRENCY",
                "attr": "$.message.order.quote.price.currency",
                "enumList": [
                  "INR"
                ],
                "_RETURN_": "attr all in enumList"
              }
            ]
          },
          {
            "_NAME_": "REQUIRED_QUOTE_BREAKUP",
            "_RETURN_": [
              {
                "_NAME_": "REQUIRED_QUOTE_BREAKUP_TITLE",
                "attr": "$.message.order.quote.breakup[*].title",
                "_RETURN_": "attr are present"
              },
              {
                "_NAME_": "VALID_QUOTE_BREAKUP_TITLE_ENUM",
                "attr": "$.message.order.quote.breakup[*].title",
                "enumList": [
                  "PRINCIPAL",
                  "INTEREST",
                  "PROCESSING_FEE",
                  "OTHER_UPFRONT_CHARGES",
                  "INSURANCE_CHARGES",
                  "NET_DISBURSED_AMOUNT",
                  "OTHER_CHARGES"
                ],
                "_RETURN_": "attr any in enumList"
              },
              {
                "_NAME_": "REQUIRED_QUOTE_BREAKUP_PRICE",
                "attr": "$.message.order.quote.breakup[*].price.value",
                "_RETURN_": "attr are present"
              },
              {
                "_NAME_": "REQUIRED_QUOTE_BREAKUP_PRICE_CURRENCY",
                "attr": "$.message.order.quote.breakup[*].price.currency",
                "enumList": [
                  "INR"
                ],
                "_RETURN_": "attr all in enumList"
              }
            ]
          },
          {
            "_NAME_": "REQUIRED_QUOTE_TTL",
            "attr": "$.message.order.quote.ttl",
            "_RETURN_": "attr are present"
          }
        ]
      },
      {
        "_NAME_": "ON_SELECT_2_OFFER_FULFILLMENT_GOLD",
        "item_code": "$.message.order.items[*].descriptor.code",
        "loan_type_match": [
          "LOAN"
        ],
        "usecasepath": "$.message.order.items[*].price.value",
        "_CONTINUE_": "!(item_code any in loan_type_match) || !(usecasepath are present)",
        "_RETURN_": [
          {
            "_NAME_": "REQUIRED_FULFILLMENT_TYPE",
            "attr": "$.message.order.fulfillments[*].type",
            "enumList": [
              "LOAN"
            ],
            "_CONTINUE_": "!(attr are present)",
            "_RETURN_": "attr all in enumList"
          },
          {
            "_NAME_": "REQUIRED_FULFILLMENT_AGENT_NAME",
            "attr": "$.message.order.fulfillments[*].agent.person.name",
            "_CONTINUE_": "!(attr are present)",
            "_RETURN_": "attr are present"
          },
          {
            "_NAME_": "REQUIRED_FULFILLMENT_AGENT_CONTACT",
            "attr": "$.message.order.fulfillments[*].agent.contact.phone",
            "_CONTINUE_": "!(attr are present)",
            "_RETURN_": "attr are present"
          }
        ]
      },
      {
        "_NAME_": "ON_SELECT_2_OFFER_XINPUT_COMMON",
        "usecasepath": "$.message.order.items[*].price.value",
        "_CONTINUE_": "!(usecasepath are present)",
        "_RETURN_": [
          {
            "_NAME_": "REQUIRED_XINPUT_REQUIRED",
            "attr": "$.message.order.items[*].xinput.required",
            "_RETURN_": "attr are present"
          },
          {
            "_NAME_": "REQUIRED_XINPUT_FORM_ID",
            "attr": "$.message.order.items[*].xinput.form.id",
            "_RETURN_": "attr are present"
          },
          {
            "_NAME_": "REQUIRED_XINPUT_FORM_URL",
            "attr": "$.message.order.items[*].xinput.form.url",
            "_RETURN_": "attr are present"
          }
        ]
      },
      {
        "_NAME_": "ON_SELECT_2_OFFER_XINPUT_PERSONAL_LOAN",
        "item_code": "$.message.order.items[*].descriptor.code",
        "loan_type_match": [
          "PERSONAL_LOAN"
        ],
        "usecasepath": "$.message.order.items[*].price.value",
        "_CONTINUE_": "!(item_code any in loan_type_match) || !(usecasepath are present)",
        "_RETURN_": [
          {
            "_NAME_": "REQUIRED_XINPUT_HEAD_INDEX",
            "_RETURN_": [
              {
                "_NAME_": "REQUIRED_XINPUT_HEAD_INDEX_MIN",
                "attr": "$.message.order.items[*].xinput.head.index.min",
                "_RETURN_": "attr are present"
              },
              {
                "_NAME_": "REQUIRED_XINPUT_HEAD_INDEX_CUR",
                "attr": "$.message.order.items[*].xinput.head.index.cur",
                "_RETURN_": "attr are present"
              },
              {
                "_NAME_": "REQUIRED_XINPUT_HEAD_INDEX_MAX",
                "attr": "$.message.order.items[*].xinput.head.index.max",
                "_RETURN_": "attr are present"
              }
            ]
          },
          {
            "_NAME_": "REQUIRED_XINPUT_HEAD_DESCRIPTOR_NAME",
            "attr": "$.message.order.items[*].xinput.head.descriptor.name",
            "_RETURN_": "attr are present"
          },
          {
            "_NAME_": "REQUIRED_XINPUT_HEAD_HEADINGS",
            "attr": "$.message.order.items[*].xinput.head.headings[*]",
            "_RETURN_": "attr are present"
          }
        ]
      },
      {
        "_NAME_": "ON_SELECT_2_OFFER_XINPUT_GOLD",
        "item_code": "$.message.order.items[*].descriptor.code",
        "loan_type_match": [
          "LOAN"
        ],
        "usecasepath": "$.message.order.items[*].price.value",
        "_CONTINUE_": "!(item_code any in loan_type_match) || !(usecasepath are present)",
        "_RETURN_": [
          {
            "_NAME_": "REQUIRED_XINPUT_HEAD_INDEX",
            "_RETURN_": [
              {
                "_NAME_": "REQUIRED_XINPUT_HEAD_INDEX_MIN",
                "attr": "$.message.order.items[*].xinput.head.index.min",
                "_RETURN_": "attr are present"
              },
              {
                "_NAME_": "REQUIRED_XINPUT_HEAD_INDEX_CUR",
                "attr": "$.message.order.items[*].xinput.head.index.cur",
                "_RETURN_": "attr are present"
              },
              {
                "_NAME_": "REQUIRED_XINPUT_HEAD_INDEX_MAX",
                "attr": "$.message.order.items[*].xinput.head.index.max",
                "_RETURN_": "attr are present"
              }
            ]
          },
          {
            "_NAME_": "REQUIRED_XINPUT_HEAD_DESCRIPTOR_NAME",
            "attr": "$.message.order.items[*].xinput.head.descriptor.name",
            "_RETURN_": "attr are present"
          },
          {
            "_NAME_": "REQUIRED_XINPUT_HEAD_HEADINGS",
            "attr": "$.message.order.items[*].xinput.head.headings[*]",
            "_RETURN_": "attr are present"
          }
        ]
      }
    ]
  }
}
```