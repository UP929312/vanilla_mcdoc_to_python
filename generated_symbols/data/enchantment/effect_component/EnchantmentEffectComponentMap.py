# Generated from symbols.json for ::java::data::enchantment::effect_component::EnchantmentEffectComponentMap
from typing import Any


type EnchantmentEffectComponentMap = dict[str, Any]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::effect_component::EnchantmentEffectComponentMap": {
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
                                    "value": "enchantment_effect_component_type"
                                }
                            }
                        }
                    ]
                },
                "type": {
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
                    "registry": "minecraft:effect_component"
                },
                "optional": True
            }
        ]
    }
}

