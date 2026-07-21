# Generated from symbols.json for ::java::data::enchantment::effect::LocationBasedEffect
from dataclasses import dataclass


@dataclass(kw_only=True)
class LocationBasedEffect:
    type: str


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::effect::LocationBasedEffect": {
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
                                    "value": "enchantment_location_based_effect_type"
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
                    "registry": "minecraft:location_based_effect"
                }
            }
        ]
    }
}

