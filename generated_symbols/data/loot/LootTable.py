# Generated from symbols.json for ::java::data::loot::LootTable
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.item_modifier.ItemModifier import ItemModifier
    from generated_symbols.data.loot.LootContextParamSets import LootContextParamSets
    from generated_symbols.data.loot.LootPool import LootPool


@dataclass(kw_only=True)
class LootTable:
    type: LootContextParamSets | None = None
    pools: list[LootPool] | None = None
    modifier: ItemModifier | None = None
    random_sequence: str | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::LootTable": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "type",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::loot::LootContextParamSets",
                    "attributes": [
                        {
                            "name": "id"
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "pools",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::data::loot::LootPool"
                    }
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
                                "value": "26.3"
                            }
                        }
                    }
                ],
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
                "key": "modifier",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::item_modifier::ItemModifier"
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
                                "value": "1.20"
                            }
                        }
                    }
                ],
                "key": "random_sequence",
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
                                            "value": "random_sequence"
                                        }
                                    },
                                    "definition": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "boolean",
                                            "value": True
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "optional": True
            }
        ]
    }
}

