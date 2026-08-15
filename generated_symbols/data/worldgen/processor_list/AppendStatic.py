"""
Generated from symbols.json for ::java::data::worldgen::processor_list::AppendStatic
Local link to file: generated_symbols/data/worldgen/processor_list/AppendStatic.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass


@dataclass(kw_only=True)
class DataStruct:
    pass


@dataclass(kw_only=True)
class AppendStatic:
    data: DataStruct


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::processor_list::AppendStatic": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "data",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "dispatcher",
                            "parallelIndices": [
                                {
                                    "kind": "dynamic",
                                    "accessor": [
                                        {
                                            "keyword": "parent"
                                        },
                                        "output_state",
                                        "Name"
                                    ]
                                }
                            ],
                            "registry": "minecraft:block",
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
                            ]
                        },
                        {
                            "kind": "struct",
                            "fields": [
                                {
                                    "kind": "spread",
                                    "type": {
                                        "kind": "dispatcher",
                                        "parallelIndices": [
                                            {
                                                "kind": "dynamic",
                                                "accessor": [
                                                    {
                                                        "keyword": "parent"
                                                    },
                                                    {
                                                        "keyword": "parent"
                                                    },
                                                    "output_state"
                                                ]
                                            }
                                        ],
                                        "registry": "minecraft:block"
                                    }
                                },
                                {
                                    "kind": "spread",
                                    "type": {
                                        "kind": "dispatcher",
                                        "parallelIndices": [
                                            {
                                                "kind": "dynamic",
                                                "accessor": [
                                                    {
                                                        "keyword": "parent"
                                                    },
                                                    {
                                                        "keyword": "parent"
                                                    },
                                                    "output_state",
                                                    "id"
                                                ]
                                            }
                                        ],
                                        "registry": "minecraft:block"
                                    }
                                }
                            ],
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
                            ]
                        }
                    ]
                }
            }
        ]
    }
}

