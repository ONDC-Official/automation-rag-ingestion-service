---
action: on_confirm
domain: ONDC:FIS12
version: 2.3.0
numTests: 9
generated: 2026-04-15
---

```json
{
  "_TESTS_": {
    "on_confirm": [
      {
        "_NAME_": "ON_CONFIRM_CONTEXT",
        "action": [
          "on_confirm"
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
        "_NAME_": "ON_CONFIRM_PROVIDER",
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
          },
          {
            "_NAME_": "REQUIRED_PROVIDER_TAGS",
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
                "_NAME_": "REQUIRED_LSP_INFO_TAG_GROUP",
                "validTags": [
                  "LSP_INFO"
                ],
                "tagPath": "$.message.order.provider.tags[*].descriptor.code",
                "_RETURN_": "tagPath any in validTags"
              }
            ]
          }
        ]
      },
      {
        "_NAME_": "ON_CONFIRM_ITEMS",
        "_SCOPE_": "$.message.order.items[?(@.descriptor.code=='PERSONAL_LOAN')]",
        "_RETURN_": [
          {
            "_NAME_": "REQUIRED_ITEM_ID",
            "attr": "$.message.order.items[*].id",
            "_RETURN_": "attr are present"
          },
          {
            "_NAME_": "REQUIRED_ITEM_DESCRIPTOR_CODE",
            "attr": "$.message.order.items[*].descriptor.code",
            "enumList": [
              "LOAN",
              "PERSONAL_LOAN",
              "CREDIT_CARD"
            ],
            "_RETURN_": "attr all in enumList"
          },
          {
            "_NAME_": "REQUIRED_ITEM_PRICE",
            "attr": "$.message.order.items[*].price.value",
            "_RETURN_": "attr are present"
          },
          {
            "_NAME_": "REQUIRED_LOAN_INFO_TAG",
            "validTags": [
              "LOAN_INFO",
              "CONTACT_INFO",
              "LSP_INFO",
              "GENERAL_INFO"
            ],
            "tagPath": "$.message.order.items[*].tags[*].descriptor.code",
            "_RETURN_": "tagPath any in validTags"
          }
        ]
      },
      {
        "_NAME_": "ON_CONFIRM_QUOTE",
        "_SCOPE_": "$.message.order.items[?(@.descriptor.code=='PERSONAL_LOAN')]",
        "_RETURN_": [
          {
            "_NAME_": "REQUIRED_QUOTE_ID",
            "attr": "$.message.order.quote.id",
            "_RETURN_": "attr are present"
          },
          {
            "_NAME_": "REQUIRED_QUOTE_PRICE",
            "attr": "$.message.order.quote.price.value",
            "_RETURN_": "attr are present"
          },
          {
            "_NAME_": "REQUIRED_QUOTE_BREAKUP",
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
          }
        ]
      },
      {
        "_NAME_": "ON_CONFIRM_FULFILLMENTS",
        "_RETURN_": [
          {
            "_NAME_": "REQUIRED_FULFILLMENT_TYPE",
            "attr": "$.message.order.fulfillments[*].type",
            "_CONTINUE_": "!(attr are present)",
            "enumList": [
              "LOAN"
            ],
            "_RETURN_": "attr all in enumList"
          },
          {
            "_NAME_": "REQUIRED_FULFILLMENT_STATE_DESCRIPTOR_CODE",
            "attr": "$.message.order.fulfillments[*].state.descriptor.code",
            "_RETURN_": "attr are present"
          },
          {
            "_NAME_": "VALID_FULFILLMENT_STATE_ENUM",
            "attr": "$.message.order.fulfillments[*].state.descriptor.code",
            "enumList": [
              "DISBURSED",
              "SANCTIONED",
              "DISPATCHED"
            ],
            "_RETURN_": "attr any in enumList"
          },
          {
            "_NAME_": "REQUIRED_FULFILLMENT_CUSTOMER",
            "attr": "$.message.order.fulfillments[*].customer.person.name",
            "_CONTINUE_": "!(attr are present)",
            "_RETURN_": "attr are present"
          }
        ]
      },
      {
        "_NAME_": "ON_CONFIRM_PAYMENTS",
        "_SCOPE_": "$.message.order.items[?(@.descriptor.code=='PERSONAL_LOAN')]",
        "_RETURN_": [
          {
            "_NAME_": "REQUIRED_PAYMENT_TYPE",
            "attr": "$.message.order.payments[*].type",
            "enumList": [
              "ON_ORDER",
              "ON_FULFILLMENT",
              "POST_FULFILLMENT"
            ],
            "_RETURN_": "attr all in enumList"
          },
          {
            "_NAME_": "REQUIRED_PAYMENT_STATUS",
            "attr": "$.message.order.payments[*].status",
            "_RETURN_": "attr are present"
          },
          {
            "_NAME_": "VALID_PAYMENT_STATUS_ENUM",
            "attr": "$.message.order.payments[*].status",
            "enumList": [
              "PAID",
              "NOT-PAID"
            ],
            "_RETURN_": "attr all in enumList"
          }
        ]
      },
      {
        "_NAME_": "ON_CONFIRM_PAYMENTS_COLLECTED_BY",
        "_SCOPE_": "$.message.order.payments[?(@.type=='ON_ORDER')]",
        "_RETURN_": [
          {
            "_NAME_": "REQUIRED_PAYMENT_COLLECTED_BY",
            "attr": "$.message.order.payments[?(@.type=='ON_ORDER')].collected_by",
            "enumList": [
              "BPP",
              "BAP"
            ],
            "_RETURN_": "attr all in enumList"
          }
        ]
      },
      {
        "_NAME_": "ON_CONFIRM_DOCUMENTS",
        "_SCOPE_": "$.message.order.items[?(@.descriptor.code=='PERSONAL_LOAN')]",
        "_RETURN_": [
          {
            "_NAME_": "REQUIRED_DOCUMENT_DESCRIPTOR_CODE",
            "attr": "$.message.order.documents[*].descriptor.code",
            "_RETURN_": "attr are present"
          },
          {
            "_NAME_": "REQUIRED_DOCUMENT_URL",
            "attr": "$.message.order.documents[*].url",
            "_RETURN_": "attr are present"
          },
          {
            "_NAME_": "REQUIRED_DOCUMENT_MIME_TYPE",
            "attr": "$.message.order.documents[*].mime_type",
            "enumList": [
              "application/pdf",
              "text/html"
            ],
            "_RETURN_": "attr all in enumList"
          }
        ]
      },
      {
        "_NAME_": "ON_CONFIRM_CANCELLATION_TERMS",
        "attr": "$.message.order.cancellation_terms[*].fulfillment_state.descriptor.code",
        "enumList": [
          "SANCTIONED",
          "DISBURSED"
        ],
        "_CONTINUE_": "!(attr are present)",
        "_RETURN_": "attr all in enumList"
      }
    ]
  }
}
```