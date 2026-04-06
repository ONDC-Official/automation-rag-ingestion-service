---
action: on_status
domain: ONDC:FIS12
version: 2.0.2
numTests: 6
generated: 2026-03-18
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
        "_NAME_": "ON_STATUS_ORDER",
        "_RETURN_": [
          {
            "_NAME_": "REQUIRED_ORDER_PROVIDER_ID",
            "attr": "$.message.order.provider.id",
            "_RETURN_": "attr are present"
          },
          {
            "_NAME_": "REQUIRED_ORDER_ITEMS",
            "attr": "$.message.order.items[*].id",
            "_RETURN_": "attr are present"
          }
        ]
      },
      {
        "_NAME_": "ON_STATUS_FULFILLMENTS",
        "_RETURN_": [
          {
            "_NAME_": "REQUIRED_FULFILLMENT_TYPE",
            "attr": "$.message.order.fulfillments[*].type",
            "enumList": [
              "LOAN"
            ],
            "_CONTINUE_": "!(attr are present)",
            "_RETURN_": "attr all in enumList"
          }
        ]
      },
      {
        "_NAME_": "ON_STATUS_FULFILLMENT_STATE",
        "statepath": "$.message.order.fulfillments[*].state.descriptor.code",
        "_CONTINUE_": "!(statepath are present)",
        "_RETURN_": [
          {
            "_NAME_": "VALID_FULFILLMENT_STATE_CODE",
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
      },
      {
        "_NAME_": "ON_STATUS_PAYMENTS",
        "paymentspath": "$.message.order.payments[*].type",
        "_CONTINUE_": "!(paymentspath are present)",
        "_RETURN_": [
          {
            "_NAME_": "REQUIRED_PAYMENT_TYPE",
            "attr": "$.message.order.payments[*].type",
            "_RETURN_": "attr are present"
          },
          {
            "_NAME_": "REQUIRED_PAYMENT_STATUS",
            "attr": "$.message.order.payments[*].status",
            "enumList": [
              "PAID",
              "NOT-PAID",
              "FAILED",
              "DELAYED",
              "DEFERRED"
            ],
            "_RETURN_": "attr all in enumList"
          }
        ]
      },
      {
        "_NAME_": "ON_STATUS_QUOTE",
        "attr": "$.message.order.quote.breakup[*].title",
        "enumList": [
          "PRINCIPAL",
          "INTEREST",
          "PROCESSING_FEE",
          "OTHER_UPFRONT_CHARGES",
          "INSURANCE_CHARGES",
          "NET_DISBURSED_AMOUNT",
          "OTHER_CHARGES",
          "LATE_FEE_AMOUNT",
          "OUTSTANDING_PRINCIPAL",
          "FORCLOSUER_CHARGES",
          "OUTSTANDING_INTEREST",
          "PRE_PAYMENT_CHARGE",
          "INSURANCE_TOTAL_FEE",
          "INSURANCE_PRODUCT_FEE",
          "TAX"
        ],
        "_RETURN_": "attr any in enumList"
      }
    ]
  }
}
```