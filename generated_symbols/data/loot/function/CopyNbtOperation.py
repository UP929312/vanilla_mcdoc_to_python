# Generated from symbols.json for ::java::data::loot::function::CopyNbtOperation
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.loot.function.CopyNbtStrategy import CopyNbtStrategy


@dataclass(kw_only=True)
class CopyNbtOperation:
    source: str
    target: str
    op: CopyNbtStrategy


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::function::CopyNbtOperation": {
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
}

