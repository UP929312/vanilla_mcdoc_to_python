# Generated from symbols.json for ::java::data::worldgen::FloatProvider
from dataclasses import dataclass
from typing import Generic, TypeVar


T = TypeVar('T')

@dataclass(kw_only=True)
class FloatProvider(Generic[T]):
    type: str


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::FloatProvider": {
        "kind": "template",
        "child": {
            "kind": "union",
            "members": [
                {
                    "kind": "reference",
                    "path": "::java::data::worldgen::T"
                },
                {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "key": "type",
                            "type": {
                                "kind": "string",
                                "attributes": [
                                    {
                                        "name": "id",
                                        "value": {
                                            "kind": "literal",
                                            "value": {
                                                "kind": "string",
                                                "value": "float_provider_type"
                                            }
                                        }
                                    }
                                ]
                            }
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
                                            "value": "1.20.5"
                                        }
                                    }
                                }
                            ],
                            "key": "value",
                            "type": {
                                "kind": "concrete",
                                "child": {
                                    "kind": "dispatcher",
                                    "parallelIndices": [
                                        {
                                            "kind": "dynamic",
                                            "accessor": [
                                                "type"
                                            ]
                                        }
                                    ],
                                    "registry": "minecraft:float_provider"
                                },
                                "typeArgs": [
                                    {
                                        "kind": "reference",
                                        "path": "::java::data::worldgen::T"
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
                                            "value": "1.20.5"
                                        }
                                    }
                                }
                            ],
                            "type": {
                                "kind": "concrete",
                                "child": {
                                    "kind": "dispatcher",
                                    "parallelIndices": [
                                        {
                                            "kind": "dynamic",
                                            "accessor": [
                                                "type"
                                            ]
                                        }
                                    ],
                                    "registry": "minecraft:float_provider"
                                },
                                "typeArgs": [
                                    {
                                        "kind": "reference",
                                        "path": "::java::data::worldgen::T"
                                    }
                                ]
                            }
                        }
                    ]
                }
            ]
        },
        "typeParams": [
            {
                "path": "::java::data::worldgen::T"
            }
        ]
    }
}

