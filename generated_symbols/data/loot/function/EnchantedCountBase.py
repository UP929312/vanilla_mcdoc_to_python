# Generated from symbols.json for ::java::data::loot::function::EnchantedCountBase
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.number_provider.NumberProviderRef import NumberProviderRef


@dataclass(kw_only=True)
class EnchantedCountBase:
    count: NumberProviderRef  # If the number is fractional the result is rounded *after* the number was multiplied by the looting level.
    limit: int | None = None  # Limits the count of the item to a range.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::function::EnchantedCountBase": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "If the number is fractional the result is rounded *after* the number was multiplied by the looting level.",
                "key": "count",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "concrete",
                            "child": {
                                "kind": "reference",
                                "path": "::java::data::util::MinMaxBounds"
                            },
                            "typeArgs": [
                                {
                                    "kind": "float"
                                }
                            ],
                            "attributes": [
                                {
                                    "name": "until",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.17"
                                        }
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "reference",
                            "path": "::java::data::number_provider::NumberProviderRef",
                            "attributes": [
                                {
                                    "name": "since",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.17"
                                        }
                                    }
                                }
                            ]
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "desc": "Limits the count of the item to a range.",
                "key": "limit",
                "type": {
                    "kind": "int"
                },
                "optional": True
            }
        ]
    }
}

