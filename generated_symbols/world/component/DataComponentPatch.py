# Generated from symbols.json for ::java::world::component::DataComponentPatch
from dataclasses import dataclass
from typing import Any


@dataclass(kw_only=True)
class DataComponentPatch:
    PersistentDataComponent: Any
    key_name: Any


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::DataComponentPatch": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": {
                    "kind": "reference",
                    "path": "::java::world::component::PersistentDataComponent"
                },
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "dynamic",
                            "accessor": [
                                {
                                    "keyword": "key"
                                }
                            ]
                        }
                    ],
                    "registry": "minecraft:data_component"
                }
            },
            {
                "kind": "pair",
                "key": {
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
                                            "value": "data_component_type"
                                        }
                                    },
                                    "prefix": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "!"
                                        }
                                    },
                                    "exclude": {
                                        "kind": "tree",
                                        "values": {
                                            "0": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "string",
                                                    "value": "additional_trade_cost"
                                                }
                                            },
                                            "1": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "string",
                                                    "value": "creative_slot_lock"
                                                }
                                            },
                                            "2": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "string",
                                                    "value": "map_post_processing"
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "type": {
                    "kind": "struct",
                    "fields": []
                }
            }
        ]
    }
}

