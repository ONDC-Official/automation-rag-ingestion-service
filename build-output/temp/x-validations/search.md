---
action: search
domain: ONDC:FIS12
version: 2.0.2
numTests: 3
generated: 2026-03-18
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
        "_NAME_": "SEARCH_CATEGORY_CODE",
        "action": [
          "search"
        ],
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
              "GOLD_LOAN",
              "PERSONAL_LOAN"
            ],
            "_CONTINUE_": "!(attr are present)",
            "_RETURN_": "attr all in enumList"
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
            "_NAME_": "REQUIRED_PAYMENT_COLLECTED_BY",
            "attr": "$.message.intent.payment.collected_by",
            "_RETURN_": "attr are present"
          },
          {
            "_NAME_": "VALID_PAYMENT_COLLECTED_BY_ENUM",
            "attr": "$.message.intent.payment.collected_by",
            "enumList": [
              "BPP",
              "BAP"
            ],
            "_CONTINUE_": "!(attr are present)",
            "_RETURN_": "attr any in enumList"
          },
          {
            "_NAME_": "REQUIRED_PAYMENT_TAGS_GROUPS",
            "_RETURN_": [
              {
                "_NAME_": "REQUIRED_BUYER_FINDER_FEES_TAG",
                "validTags": [
                  "BUYER_FINDER_FEES"
                ],
                "tagPath": "$.message.intent.payment.tags[*].descriptor.code",
                "_RETURN_": "tagPath any in validTags"
              },
              {
                "_NAME_": "REQUIRED_BUYER_FINDER_FEES_LIST",
                "_SCOPE_": "$.message.intent.payment.tags[?(@.descriptor.code=='BUYER_FINDER_FEES')]",
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
                "_SCOPE_": "$.message.intent.payment.tags[?(@.descriptor.code=='BUYER_FINDER_FEES')].list[?(@.descriptor.code=='BUYER_FINDER_FEES_TYPE')]",
                "attr": "$.value",
                "enumList": [
                  "percent-annualized",
                  "percent",
                  "amount"
                ],
                "_RETURN_": "attr all in enumList"
              },
              {
                "_NAME_": "REQUIRED_SETTLEMENT_TERMS_TAG",
                "validTags": [
                  "SETTLEMENT_TERMS"
                ],
                "tagPath": "$.message.intent.payment.tags[*].descriptor.code",
                "_RETURN_": "tagPath any in validTags"
              },
              {
                "_NAME_": "REQUIRED_SETTLEMENT_TERMS_LIST",
                "_SCOPE_": "$.message.intent.payment.tags[?(@.descriptor.code=='SETTLEMENT_TERMS')]",
                "subTags": "$.list[*].descriptor.code",
                "validValues": [
                  "DELAY_INTEREST",
                  "STATIC_TERMS",
                  "OFFLINE_CONTRACT"
                ],
                "_CONTINUE_": "!(subTags are present)",
                "_RETURN_": "subTags all in validValues"
              }
            ]
          }
        ]
      }
    ]
  }
}
```