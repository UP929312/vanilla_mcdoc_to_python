# Generated from symbols.json for ::java::data::loot::function::EnchantWithLevels
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.data.loot.function.Conditions import Conditions

if TYPE_CHECKING:
    from generated_symbols.data.number_provider.NumberProviderRef import NumberProviderRef


@dataclass(kw_only=True)
class EnchantWithLevels(Conditions):
    levels: NumberProviderRef  # The levels to enchant this item with.
    options: str | list[str] | None = None  # The allowed enchantments. If omitted, all enchantments applicable to the item are possible.
    include_additional_cost_component: bool | None = None  # Whether to add `additional_trade_cost` component to the enchanted item. Additional cost value is equal to the level cost determined by `levels`. Defaults to `false`.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::function::EnchantWithLevels": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "The levels to enchant this item with.",
                "key": "levels",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "reference",
                            "path": "::java::data::util::RandomIntGenerator",
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
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21"
                            }
                        }
                    }
                ],
                "desc": "The allowed enchantments. If omitted, all enchantments applicable to the item are possible.",
                "key": "options",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "tree",
                                        "values": {
                                            "registry": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "string",
                                                    "value": "enchantment"
                                                }
                                            },
                                            "tags": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "string",
                                                    "value": "allowed"
                                                }
                                            }
                                        }
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "list",
                            "item": {
                                "kind": "string",
                                "attributes": [
                                    {
                                        "name": "id",
                                        "value": {
                                            "kind": "literal",
                                            "value": {
                                                "kind": "string",
                                                "value": "enchantment"
                                            }
                                        }
                                    }
                                ]
                            }
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21"
                            }
                        }
                    }
                ],
                "desc": "Whether treasure enchantments are allowed on this item.",
                "key": "treasure",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.1"
                            }
                        }
                    }
                ],
                "desc": "Whether to add `additional_trade_cost` component to the enchanted item.\nAdditional cost value is equal to the level cost determined by `levels`.\nDefaults to `False`.",
                "key": "include_additional_cost_component",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::loot::function::Conditions"
                }
            }
        ]
    }
}

