# Generated from symbols.json for ::java::data::loot::function::CopyNbt
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any
from generated_symbols.data.loot.function.Conditions import Conditions

if TYPE_CHECKING:
    from generated_symbols.data.util.NbtProvider import NbtProvider


@dataclass(kw_only=True)
class CopyNbt(Conditions):
    source: NbtProvider
    ops: list[Any]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::function::CopyNbt": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "source",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::util::NbtProvider"
                }
            },
            {
                "kind": "pair",
                "key": "ops",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "union",
                        "members": [
                            {
                                "kind": "struct",
                                "fields": [
                                    {
                                        "kind": "pair",
                                        "key": "source",
                                        "type": {
                                            "kind": "string",
                                            "attributes": [
                                                {
                                                    "name": "nbt_path"
                                                }
                                            ]
                                        }
                                    },
                                    {
                                        "kind": "pair",
                                        "key": "target",
                                        "type": {
                                            "kind": "union",
                                            "members": [
                                                {
                                                    "kind": "string",
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
                                                        },
                                                        {
                                                            "name": "nbt_path",
                                                            "value": {
                                                                "kind": "dispatcher",
                                                                "parallelIndices": [
                                                                    {
                                                                        "kind": "static",
                                                                        "value": "%fallback"
                                                                    }
                                                                ],
                                                                "registry": "minecraft:item"
                                                            }
                                                        }
                                                    ]
                                                },
                                                {
                                                    "kind": "string",
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
                                                        },
                                                        {
                                                            "name": "nbt_path",
                                                            "value": {
                                                                "kind": "dispatcher",
                                                                "parallelIndices": [
                                                                    {
                                                                        "kind": "static",
                                                                        "value": "%fallback"
                                                                    }
                                                                ],
                                                                "registry": "mcdoc:custom_data"
                                                            }
                                                        }
                                                    ]
                                                }
                                            ]
                                        }
                                    },
                                    {
                                        "kind": "pair",
                                        "key": "op",
                                        "type": {
                                            "kind": "reference",
                                            "path": "::java::data::loot::function::CopyNbtStrategy"
                                        }
                                    }
                                ]
                            }
                        ]
                    }
                }
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

