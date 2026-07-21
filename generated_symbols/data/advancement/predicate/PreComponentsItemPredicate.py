# Generated from symbols.json for ::java::data::advancement::predicate::PreComponentsItemPredicate
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.advancement.predicate.EnchantmentPredicate import EnchantmentPredicate
    from generated_symbols.data.util.MinMaxBounds import MinMaxBounds


@dataclass(kw_only=True)
class PreComponentsItemPredicate:
    items: list[str] | None = None
    tag: str | None = None
    durability: MinMaxBounds[int] | int | None = None
    potion: str | None = None
    enchantments: list[EnchantmentPredicate] | None = None
    stored_enchantments: list[EnchantmentPredicate] | None = None
    nbt: str | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::predicate::PreComponentsItemPredicate": {
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
                                "value": "1.17"
                            }
                        }
                    }
                ],
                "key": "item",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "item"
                                }
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
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.17"
                            }
                        }
                    }
                ],
                "key": "items",
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
                                        "value": "item"
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
                "key": "tag",
                "type": {
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
                                            "value": "item"
                                        }
                                    },
                                    "tags": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "implicit"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "durability",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::data::util::MinMaxBounds"
                    },
                    "typeArgs": [
                        {
                            "kind": "int"
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "potion",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "potion"
                                }
                            }
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "enchantments",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::data::advancement::predicate::EnchantmentPredicate"
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "stored_enchantments",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::data::advancement::predicate::EnchantmentPredicate"
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "nbt",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "nbt",
                            "value": {
                                "kind": "dispatcher",
                                "parallelIndices": [
                                    {
                                        "kind": "dynamic",
                                        "accessor": [
                                            "item"
                                        ]
                                    }
                                ],
                                "registry": "minecraft:item"
                            }
                        }
                    ]
                },
                "optional": True
            }
        ],
        "attributes": [
            {
                "name": "until",
                "value": {
                    "kind": "literal",
                    "value": {
                        "kind": "string",
                        "value": "1.20.5"
                    }
                }
            }
        ]
    }
}

