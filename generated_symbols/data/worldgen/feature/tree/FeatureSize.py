# Generated from symbols.json for ::java::data::worldgen::feature::tree::FeatureSize
from dataclasses import dataclass


@dataclass(kw_only=True)
class FeatureSize:
    type: str


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::tree::FeatureSize": {
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
                                    "value": "worldgen/feature_size_type"
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
                    "registry": "minecraft:feature_size"
                }
            }
        ]
    }
}

