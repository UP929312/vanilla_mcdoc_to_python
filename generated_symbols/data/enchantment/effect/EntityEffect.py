# Generated from symbols.json for ::java::data::enchantment::effect::EntityEffect
from dataclasses import dataclass


@dataclass(kw_only=True)
class EntityEffect:
    type: str


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::effect::EntityEffect": {
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
                                    "value": "enchantment_entity_effect_type"
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
                    "registry": "minecraft:entity_effect"
                }
            }
        ]
    }
}

