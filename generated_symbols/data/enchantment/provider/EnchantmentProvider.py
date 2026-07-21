# Generated from symbols.json for ::java::data::enchantment::provider::EnchantmentProvider
from dataclasses import dataclass


@dataclass(kw_only=True)
class EnchantmentProvider:
    type: str


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::provider::EnchantmentProvider": {
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
                                    "value": "enchantment_provider_type"
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
                    "registry": "minecraft:enchantment_provider"
                }
            }
        ]
    }
}

