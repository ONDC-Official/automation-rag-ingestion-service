---
action: select
domain: ONDC:FIS12
version: 2.3.0
numTests: 4
generated: 2026-04-15
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
        "_NAME_": "SELECT_PROVIDER_ID",
        "attr": "$.message.order.provider.id",
        "_RETURN_": "attr are present"
      },
      {
        "_NAME_": "SELECT_ITEMS",
        "_RETURN_": [
          {
            "_NAME_": "REQUIRED_ITEM_ID",
            "attr": "$.message.order.items[*].id",
            "_RETURN_": "attr are present"
          }
        ]
      },
      {
        "_NAME_": "SELECT_XINPUT_PERSONAL_LOAN",
        "item_code": "$.message.order.items[*].descriptor.code",
        "loan_type_match": [
          "PERSONAL_LOAN"
        ],
        "_CONTINUE_": "!(item_code any in loan_type_match)",
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
          }
        ]
      }
    ]
  }
}
```