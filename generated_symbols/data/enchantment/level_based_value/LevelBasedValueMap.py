# Generated from symbols.json for ::java::data::enchantment::level_based_value::LevelBasedValueMap
from dataclasses import dataclass


@dataclass(kw_only=True)
class LevelBasedValueMap:
    type: str


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::level_based_value::LevelBasedValueMap": {
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
                                    "value": "enchantment_level_based_value_type"
                                }
                            }
                        }
                    ]
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
                                "type"
                            ]
                        }
                    ],
                    "registry": "minecraft:level_based_value"
                }
            }
        ]
    }
}

