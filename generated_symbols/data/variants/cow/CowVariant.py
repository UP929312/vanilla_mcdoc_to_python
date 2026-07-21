# Generated from symbols.json for ::java::data::variants::cow::CowVariant
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.data.variants.SpawnPrioritySelectors import SpawnPrioritySelectors

if TYPE_CHECKING:
    from generated_symbols.data.variants.cow.CowModelType import CowModelType


@dataclass(kw_only=True)
class CowVariant(SpawnPrioritySelectors):
    asset_id: str  # The cow texture to use for this variant.
    baby_asset_id: str  # The baby cow texture to use for this variant.
    model: CowModelType | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::variants::cow::CowVariant": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "model",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::variants::cow::CowModelType"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "The cow texture to use for this variant.",
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
                "desc": "The baby cow texture to use for this variant.",
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

