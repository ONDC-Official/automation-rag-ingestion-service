---
action: confirm
domain: ONDC:FIS12
version: 2.3.0
numTests: 6
generated: 2026-04-14
---

```json
{
  "_TESTS_": {
    "confirm": [
      {
        "_NAME_": "CONFIRM_CONTEXT",
        "action": [
          "confirm"
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
          }
        ]
      },
      {
        "_NAME_": "CONFIRM_PAYMENTS",
        "usecaseRef": "$.message.order.ref_order_ids[*]",
        "_CONTINUE_": "(usecaseRef are present)",
        "_RETURN_": [
          {
            "_NAME_": "REQUIRED_PAYMENT_ITEMS",
            "_RETURN_": [
              {
                "_NAME_": "REQUIRED_PAYMENT_ITEMS",
                "attr": "$.message.order.payments[*].type",
                "_RETURN_": "attr are present"
              },
              {
                "_NAME_": "REQUIRED_PAYMENT_ID",
                "attr": "$.message.order.payments[*].id",
                "_RETURN_": "attr are present"
              },
              {
                "_NAME_": "REQUIRED_PAYMENT_STATUS",
                "attr": "$.message.order.payments[*].status",
                "_RETURN_": "attr are present"
              },
              {
                "_NAME_": "REQUIRED_PAYMENT_COLLECTED_BY",
                "attr": "$.message.order.payments[*].collected_by",
                "usecasepath": "$.message.order.payments[*].time.label",
                "label": [
                  "LOAN_DISBURSMENT"
                ],
                "_CONTINUE_": "!(usecasepath all in label)",
                "_RETURN_": "attr are present"
              },
              {
                "_NAME_": "REQUIRED_PAYMENT_BANK_ACCOUNT_NUMBER",
                "_SCOPE_": "$.message.order.payments[*][?(@.time.label=='LOAN_DISBURSMENT')]",
                "_RETURN_": [
                  {
                    "_NAME_": "REQUIRED_PAYMENT_BANK_ACCOUNT_NUMBER",
                    "attr": "$.message.order.payments[*].params.bank_account_number",
                    "_RETURN_": "attr are present"
                  }
                ]
              },
              {
                "_NAME_": "REQUIRED_PAYMENT_BANK_CODE",
                "_SCOPE_": "$.message.order.payments[*][?(@.time.label=='LOAN_DISBURSMENT')]",
                "_RETURN_": [
                  {
                    "_NAME_": "REQUIRED_PAYMENT_BANK_CODE",
                    "attr": "$.message.order.payments[*].params.bank_code",
                    "_RETURN_": "attr are present"
                  }
                ]
              },
              {
                "_NAME_": "REQUIRED_PAYMENT_LABEL",
                "attr": "$.message.order.payments[*].time.label",
                "_RETURN_": "attr are present"
              }
            ]
          }
        ]
      },
      {
        "_NAME_": "CONFIRM_PAYMENT_TAGS",
        "action": [
          "confirm"
        ],
        "_RETURN_": [
          {
            "_NAME_": "VALID_PAYMENT_TAGS",
            "validTags": [
              "ACCOUNT_DETAILS",
              "BREAKUP"
            ],
            "tagPath": "$.message.order.payments[*].tags[*].descriptor.code",
            "_CONTINUE_": "!(tagPath are present)",
            "_RETURN_": "tagPath all in validTags"
          },
          {
            "_NAME_": "REQUIRED_ACCOUNT_DETAILS",
            "_SCOPE_": "$.message.order.payments[*].tags[?(@.descriptor.code == 'ACCOUNT_DETAILS')]",
            "subTags": "$.list[*].descriptor.code",
            "validValues": [
              "ACCOUNT_TYPE",
              "ACCOUNT_HOLDER_NAME",
              "BANK_NAME"
            ],
            "_RETURN_": "subTags all in validValues"
          }
        ]
      },
      {
        "_NAME_": "CONFIRM_TAGS",
        "_RETURN_": [
          {
            "_NAME_": "REQUIRED_PAYMENT_TAGS",
            "validTags": [
              "BAP_TERMS",
              "BPP_TERMS"
            ],
            "tagPath": "$.message.order.tags[*].descriptor.code",
            "_CONTINUE_": "!(tagPath are present)",
            "_RETURN_": "tagPath all in validTags"
          },
          {
            "_NAME_": "REQUIRED_BAP_TERMS",
            "_SCOPE_": "$.message.order.tags[?(@.descriptor.code == 'BAP_TERMS')]",
            "subTags": "$.list[*].descriptor.code",
            "validValues": [
              "STATIC_TERMS",
              "OFFLINE_CONTRACT"
            ],
            "_RETURN_": "subTags all in validValues"
          },
          {
            "_NAME_": "REQUIRED_BPP_TERMS",
            "_SCOPE_": "$.message.order.tags[?(@.descriptor.code == 'BPP_TERMS')]",
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