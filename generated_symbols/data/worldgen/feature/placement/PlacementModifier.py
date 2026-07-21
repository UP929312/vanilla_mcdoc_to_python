# Generated from symbols.json for ::java::data::worldgen::feature::placement::PlacementModifier
from dataclasses import dataclass


@dataclass(kw_only=True)
class PlacementModifier:
    type: str


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::placement::PlacementModifier": {
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
                                    "value": "worldgen/placement_modifier_type"
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
                    "registry": "minecraft:placement_modifier"
                }
            }
        ]
    }
}

