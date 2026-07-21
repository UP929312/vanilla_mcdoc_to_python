# Generated from symbols.json for ::java::data::variants::chicken::ChickenVariant
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.data.variants.SpawnPrioritySelectors import SpawnPrioritySelectors

if TYPE_CHECKING:
    from generated_symbols.data.variants.chicken.ChickenModelType import ChickenModelType


@dataclass(kw_only=True)
class ChickenVariant(SpawnPrioritySelectors):
    asset_id: str  # The chicken texture to use for this variant.
    baby_asset_id: str  # The baby chicken texture to use for this variant.
    model: ChickenModelType | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::variants::chicken::ChickenVariant": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "model",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::variants::chicken::ChickenModelType"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "The chicken texture to use for this variant.",
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
                "desc": "The baby chicken texture to use for this variant.",
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

