# Generated from symbols.json for ::java::data::worldgen::IntProvider
from dataclasses import dataclass
from typing import Generic, TypeVar


T = TypeVar('T')

@dataclass(kw_only=True)
class IntProvider(Generic[T]):
    type: str


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::IntProvider": {
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
                                                "value": "int_provider_type"
                                            }
                                        }
                                    }
                                ]
                            }
                        },
                        {
                            "kind": "spread",
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
                                    "registry": "minecraft:int_provider"
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

