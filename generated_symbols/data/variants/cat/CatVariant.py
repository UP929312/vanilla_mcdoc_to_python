# Generated from symbols.json for ::java::data::variants::cat::CatVariant
from dataclasses import dataclass
from generated_symbols.data.variants.SpawnPrioritySelectors import SpawnPrioritySelectors


@dataclass(kw_only=True)
class CatVariant(SpawnPrioritySelectors):
    asset_id: str  # The cat texture to use for this variant.
    baby_asset_id: str  # The baby cat texture to use for this variant.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::variants::cat::CatVariant": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "The cat texture to use for this variant.",
                "key": "asset_id",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "texture"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.1"
                            }
                        }
                    }
                ],
                "desc": "The baby cat texture to use for this variant.",
                "key": "baby_asset_id",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "texture"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::variants::SpawnPrioritySelectors"
                }
            }
        ]
    }
}

