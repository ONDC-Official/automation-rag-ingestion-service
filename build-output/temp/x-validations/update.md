---
action: update
domain: ONDC:FIS12
version: 2.0.2
numTests: 5
generated: 2026-03-18
---

```json
{
  "_TESTS_": {
    "update": [
      {
        "_NAME_": "UPDATE_CONTEXT",
        "action": [
          "update"
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
        "_NAME_": "UPDATE_ORDER_ID",
        "attr": "$.message.order.id",
        "_RETURN_": "attr are present"
      },
      {
        "_NAME_": "UPDATE_PAYMENT_TARGET",
        "update_target": "$.message.update_target",
        "target_match_fulfillment": [
          "fulfillment"
        ],
        "payment_types": "$.message.order.payments[*].type",
        "_CONTINUE_": "(update_target any in target_match_fulfillment) || !(payment_types are present)",
        "_RETURN_": [
          {
            "_NAME_": "REQUIRED_PAYMENT_TYPE",
            "attr": "$.message.order.payments[*].type",
            "enumList": [
              "POST_FULFILLMENT",
              "ON_ORDER"
            ],
            "_RETURN_": "attr all in enumList"
          },
          {
            "_NAME_": "REQUIRED_PAYMENT_TIME_LABEL",
            "attr": "$.message.order.payments[*].time.label",
            "_RETURN_": "attr are present"
          },
          {
            "_NAME_": "VALID_PAYMENT_TIME_LABEL_ENUM",
            "attr": "$.message.order.payments[*].time.label",
            "enumList": [
              "PRE_PART_PAYMENT",
              "INSTALLMENT",
              "FORECLOSURE",
              "MISSED_EMI_PAYMENT"
            ],
            "_RETURN_": "attr all in enumList"
          },
          {
            "_NAME_": "REQUIRED_PAYMENT_PARAMS_AMOUNT",
            "attr": "$.message.order.payments[*].params.amount",
            "_RETURN_": "attr are present"
          }
        ]
      },
      {
        "_NAME_": "UPDATE_PAYMENT_REF_ID_GOLD",
        "item_code": "$.message.order.items[*].descriptor.code",
        "loan_type_match": [
          "LOAN"
        ],
        "update_target": "$.message.update_target",
        "target_match_fulfillment": [
          "fulfillment"
        ],
        "payment_types": "$.message.order.payments[*].type",
        "_CONTINUE_": "!(item_code any in loan_type_match) || (update_target any in target_match_fulfillment) || !(payment_types are present)",
        "_RETURN_": [
          {
            "_NAME_": "REQUIRED_PAYMENT_REF_ID",
            "attr": "$.message.order.payments[*].tags[?(@.descriptor.code=='LOAN_REPAYMENT')].list[?(@.descriptor.code=='ref_id')].value",
            "_RETURN_": "attr are present"
          }
        ]
      },
      {
        "_NAME_": "UPDATE_FULFILLMENT_TARGET",
        "update_target": "$.message.update_target",
        "target_match": [
          "fulfillment"
        ],
        "_CONTINUE_": "!(update_target any in target_match)",
        "_RETURN_": [
          {
            "_NAME_": "REQUIRED_FULFILLMENT_STATE_CODE",
            "attr": "$.message.order.fulfillments[*].state.descriptor.code",
            "_RETURN_": "attr are present"
          },
          {
            "_NAME_": "VALID_FULFILLMENT_STATE_ENUM",
            "attr": "$.message.order.fulfillments[*].state.descriptor.code",
            "enumList": [
              "INITIATED",
              "SANCTIONED",
              "DISBURSED",
              "PENDING",
              "REJECTED",
              "COMPLETED",
              "CONSENT_REQUIRED",
              "APPROVED"
            ],
            "_RETURN_": "attr all in enumList"
          }
        ]
      }
    ]
  }
}
```