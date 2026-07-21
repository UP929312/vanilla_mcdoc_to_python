# Generated from symbols.json for ::java::data::worldgen::processor_list::BlockRot
from dataclasses import dataclass
from typing import Annotated


@dataclass(kw_only=True)
class BlockRot:
    integrity: Annotated[float, 'Range | `0`-`1` | both inclusive']
    rottable_blocks: list[str] | str | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::processor_list::BlockRot": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "integrity",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 1
                    }
                }
            },
            {
                "kind": "pair",
                "key": "rottable_blocks",
                "type": {
                    "kind": "union",
                    "members": [
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
                                                "value": "block"
                                            }
                                        }
                                    }
                                ]
                            }
                        },
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
                                                    "value": "block"
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
                        }
                    ]
                },
                "optional": True
            }
        ]
    }
}

