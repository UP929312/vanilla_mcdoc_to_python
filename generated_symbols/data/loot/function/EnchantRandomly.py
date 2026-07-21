# Generated from symbols.json for ::java::data::loot::function::EnchantRandomly
from dataclasses import dataclass
from generated_symbols.data.loot.function.Conditions import Conditions


@dataclass(kw_only=True)
class EnchantRandomly(Conditions):
    options: str | list[str] | None = None  # The allowed enchantments. If omitted, all enchantments applicable to the item are possible.
    only_compatible: bool | None = None  # Whether to only enchant with item-compatible enchantments. Defaults to `true`.  Note: Books are considered compatible with all Enchantments.
    include_additional_cost_component: bool | None = None  # Whether to add `additional_trade_cost` component to the enchanted item. Additional cost value is determined by the enchantment level, with the formula `2 + random(0, 5 + level * 10) + 3 * level`. Defaults to `false`.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::function::EnchantRandomly": {
        "kind": "struct",
        "fields": [
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
                "desc": "If omitted, all enchantments applicable to the item are possible",
                "key": "enchantments",
                "type": {
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
                },
                "optional": True
            },
            {
                "kind": "pair",
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
                "desc": "Whether to only enchant with item-compatible enchantments. Defaults to `True`.\n\nNote: Books are considered compatible with all Enchantments.",
                "key": "only_compatible",
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
                "desc": "Whether to add `additional_trade_cost` component to the enchanted item.\nAdditional cost value is determined by the enchantment level, with the formula `2 + random(0, 5 + level * 10) + 3 * level`.\nDefaults to `False`.",
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

