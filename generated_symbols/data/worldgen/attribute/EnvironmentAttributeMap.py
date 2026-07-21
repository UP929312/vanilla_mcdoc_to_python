# Generated from symbols.json for ::java::data::worldgen::attribute::EnvironmentAttributeMap
from typing import Any, TypeVar


K = TypeVar('K')

type EnvironmentAttributeMap[K] = dict[K, Any]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::attribute::EnvironmentAttributeMap": {
        "kind": "template",
        "child": {
            "kind": "struct",
            "fields": [
                {
                    "kind": "pair",
                    "key": {
                        "kind": "reference",
                        "path": "::java::data::worldgen::attribute::K"
                    },
                    "type": {
                        "kind": "union",
                        "members": [
                            {
                                "kind": "indexed",
                                "child": {
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
                                    "registry": "minecraft:environment_attribute"
                                },
                                "parallelIndices": [
                                    {
                                        "kind": "static",
                                        "value": "value"
                                    }
                                ]
                            },
                            {
                                "kind": "indexed",
                                "child": {
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
                                    "registry": "minecraft:environment_attribute"
                                },
                                "parallelIndices": [
                                    {
                                        "kind": "static",
                                        "value": "modifier"
                                    }
                                ]
                            }
                        ]
                    }
                }
            ]
        },
        "typeParams": [
            {
                "path": "::java::data::worldgen::attribute::K"
            }
        ]
    }
}

