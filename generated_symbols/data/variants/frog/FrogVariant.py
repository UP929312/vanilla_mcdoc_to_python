# Generated from symbols.json for ::java::data::variants::frog::FrogVariant
from dataclasses import dataclass
from generated_symbols.data.variants.SpawnPrioritySelectors import SpawnPrioritySelectors


@dataclass(kw_only=True)
class FrogVariant(SpawnPrioritySelectors):
    asset_id: str  # The frog texture to use for this variant.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::variants::frog::FrogVariant": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "The frog texture to use for this variant.",
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
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::variants::SpawnPrioritySelectors"
                }
            }
        ]
    }
}

