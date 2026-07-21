# Generated from symbols.json for ::java::data::loot::LootPool
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.item_modifier.ItemModifier import ItemModifier
    from generated_symbols.data.loot.LootPoolEntry import LootPoolEntry
    from generated_symbols.data.number_provider.NumberProviderRef import NumberProviderRef
    from generated_symbols.data.predicate.PredicateRef import PredicateRef


@dataclass(kw_only=True)
class LootPool:
    rolls: NumberProviderRef
    entries: list[LootPoolEntry]
    bonus_rolls: NumberProviderRef | None = None
    modifier: ItemModifier | None = None
    condition: PredicateRef | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::LootPool": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "rolls",
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
                "key": "bonus_rolls",
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
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "entries",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::data::loot::LootPoolEntry"
                    }
                }
            },
            {
                "kind": "spread",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.3"
                            }
                        }
                    }
                ],
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "key": "functions",
                            "type": {
                                "kind": "list",
                                "item": {
                                    "kind": "reference",
                                    "path": "::java::data::loot::LootFunction"
                                }
                            },
                            "optional": True
                        },
                        {
                            "kind": "pair",
                            "key": "conditions",
                            "type": {
                                "kind": "list",
                                "item": {
                                    "kind": "reference",
                                    "path": "::java::data::loot::LootCondition"
                                }
                            },
                            "optional": True
                        }
                    ]
                }
            },
            {
                "kind": "spread",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.3"
                            }
                        }
                    }
                ],
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "key": "modifier",
                            "type": {
                                "kind": "reference",
                                "path": "::java::data::item_modifier::ItemModifier"
                            },
                            "optional": True
                        },
                        {
                            "kind": "pair",
                            "key": "condition",
                            "type": {
                                "kind": "reference",
                                "path": "::java::data::predicate::PredicateRef"
                            },
                            "optional": True
                        }
                    ]
                }
            }
        ]
    }
}

