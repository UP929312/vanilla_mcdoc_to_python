# Generated from symbols.json for ::java::data::advancement::predicate::ItemPredicate
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.util.MinMaxBounds import MinMaxBounds
    from generated_symbols.world.component.DataComponentExactPredicate import DataComponentExactPredicate
    from generated_symbols.world.component.DataComponentPredicate import DataComponentPredicate


@dataclass(kw_only=True)
class ItemPredicate:
    items: str | list[str] | None = None
    count: MinMaxBounds[int] | int | None = None
    components: DataComponentExactPredicate | None = None
    predicates: DataComponentPredicate | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::predicate::ItemPredicate": {
        "kind": "union",
        "members": [
            {
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
            },
            {
                "kind": "struct",
                "fields": [
                    {
                        "kind": "pair",
                        "key": "items",
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
                                                            "value": "item"
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
                                                        "value": "item"
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
                        "key": "count",
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
                        "key": "components",
                        "type": {
                            "kind": "reference",
                            "path": "::java::world::component::DataComponentExactPredicate"
                        },
                        "optional": True
                    },
                    {
                        "kind": "pair",
                        "key": "predicates",
                        "type": {
                            "kind": "reference",
                            "path": "::java::world::component::DataComponentPredicate"
                        },
                        "optional": True
                    }
                ],
                "attributes": [
                    {
                        "name": "since",
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
        ]
    }
}

