# Generated from symbols.json for ::java::data::loot::condition::EnvironmentAttributeCheck
from dataclasses import dataclass
from typing import Any


@dataclass(kw_only=True)
class EnvironmentAttributeCheck:
    attribute: str
    value: Any


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::condition::EnvironmentAttributeCheck": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "attribute",
                "type": {
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
                }
            },
            {
                "kind": "pair",
                "key": "value",
                "type": {
                    "kind": "indexed",
                    "child": {
                        "kind": "dispatcher",
                        "parallelIndices": [
                            {
                                "kind": "dynamic",
                                "accessor": [
                                    "attribute"
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
                }
            }
        ]
    }
}

