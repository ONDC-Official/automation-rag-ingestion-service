---
action: on_init
domain: ONDC:FIS12
version: 2.0.2
numTests: 8
generated: 2026-03-18
---

```json
{
  "_TESTS_": {
    "on_init": [
      {
        "_NAME_": "ON_INIT_CONTEXT",
        "action": [
          "on_init"
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
        "_NAME_": "ON_INIT_PROVIDER",
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
        "_NAME_": "ON_INIT_ITEMS",
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
              "PERSONAL_LOAN"
            ],
            "_RETURN_": "attr all in enumList"
          },
          {
            "_NAME_": "REQUIRED_ITEM_PRICE_VALUE",
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
          },
          {
            "_NAME_": "REQUIRED_LOAN_INFO_TAG_GROUP",
            "validTags": [
              "LOAN_INFO"
            ],
            "tagPath": "$.message.order.items[*].tags[*].descriptor.code",
            "_RETURN_": "tagPath any in validTags"
          }
        ]
      },
      {
        "_NAME_": "ON_INIT_QUOTE",
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
            "_NAME_": "REQUIRED_QUOTE_PRICE_CURRENCY",
            "attr": "$.message.order.quote.price.currency",
            "enumList": [
              "INR"
            ],
            "_RETURN_": "attr all in enumList"
          },
          {
            "_NAME_": "REQUIRED_QUOTE_TTL",
            "attr": "$.message.order.quote.ttl",
            "_RETURN_": "attr are present"
          },
          {
            "_NAME_": "VALID_QUOTE_TTL_REGEX",
            "attr": "$.message.order.quote.ttl",
            "reg": [
              "^P(?:(\\\\d+Y)?(\\\\d+M)?(\\\\d+D)?(T(\\\\d+H)?(\\\\d+M)?(\\\\d+S)?)?|T\\\\d+D)$"
            ],
            "_RETURN_": "attr follow regex reg"
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
        "_NAME_": "ON_INIT_PAYMENTS",
        "_RETURN_": [
          {
            "_NAME_": "REQUIRED_PAYMENT_TYPE",
            "attr": "$.message.order.payments[*].type",
            "_RETURN_": "attr are present"
          },
          {
            "_NAME_": "VALID_PAYMENT_TYPE_ENUM",
            "attr": "$.message.order.payments[*].type",
            "enumList": [
              "ON_ORDER",
              "ON_FULFILLMENT",
              "POST_FULFILLMENT"
            ],
            "_RETURN_": "attr all in enumList"
          }
        ]
      },
      {
        "_NAME_": "ON_INIT_PAYMENTS_ON_ORDER",
        "_SCOPE_": "$.message.order.payments[?(@.type=='ON_ORDER')]",
        "_RETURN_": [
          {
            "_NAME_": "REQUIRED_PAYMENT_COLLECTED_BY",
            "attr": "$.message.order.payments[?(@.type=='ON_ORDER')].collected_by",
            "_RETURN_": "attr are present"
          },
          {
            "_NAME_": "REQUIRED_PAYMENT_TAGS",
            "_RETURN_": [
              {
                "_NAME_": "REQUIRED_BUYER_FINDER_FEES_TAG",
                "validTags": [
                  "BUYER_FINDER_FEES"
                ],
                "tagPath": "$.message.order.payments[?(@.type=='ON_ORDER')].tags[*].descriptor.code",
                "_RETURN_": "tagPath any in validTags"
              },
              {
                "_NAME_": "REQUIRED_SETTLEMENT_TERMS_TAG",
                "validTags": [
                  "SETTLEMENT_TERMS"
                ],
                "tagPath": "$.message.order.payments[?(@.type=='ON_ORDER')].tags[*].descriptor.code",
                "_RETURN_": "tagPath any in validTags"
              }
            ]
          }
        ]
      },
      {
        "_NAME_": "ON_INIT_FULFILLMENTS",
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
            "_NAME_": "REQUIRED_FULFILLMENT_CUSTOMER_PERSON_NAME",
            "attr": "$.message.order.fulfillments[*].customer.person.name",
            "_RETURN_": "attr are present"
          },
          {
            "_NAME_": "REQUIRED_FULFILLMENT_STATE_CODE",
            "attr": "$.message.order.fulfillments[*].state.descriptor.code",
            "_RETURN_": "attr are present"
          }
        ]
      },
      {
        "_NAME_": "ON_INIT_XINPUT_PERSONAL_LOAN",
        "item_code": "$.message.order.items[*].descriptor.code",
        "loan_type_match": [
          "PERSONAL_LOAN"
        ],
        "xinputpath": "$.message.order.items[*].xinput.form.id",
        "_CONTINUE_": "!(item_code any in loan_type_match) || !(xinputpath are present)",
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