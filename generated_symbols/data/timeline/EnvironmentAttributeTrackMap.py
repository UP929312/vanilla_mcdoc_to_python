# Generated from symbols.json for ::java::data::timeline::EnvironmentAttributeTrackMap
from typing import Any


type EnvironmentAttributeTrackMap = dict[str, Any]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::timeline::EnvironmentAttributeTrackMap": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "environment_attribute"
                                }
                            }
                        }
                    ]
                },
                "type": {
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
                            "value": "attribute_track"
                        }
                    ]
                }
            }
        ]
    }
}

