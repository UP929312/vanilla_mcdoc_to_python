# Generated from symbols.json for ::java::data::variants::pig::PigVariant
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.data.variants.SpawnPrioritySelectors import SpawnPrioritySelectors

if TYPE_CHECKING:
    from generated_symbols.data.variants.pig.PigModelType import PigModelType


@dataclass(kw_only=True)
class PigVariant(SpawnPrioritySelectors):
    asset_id: str  # The pig texture to use for this variant.
    baby_asset_id: str  # The baby pig texture to use for this variant.
    model: PigModelType | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::variants::pig::PigVariant": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "model",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::variants::pig::PigModelType"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "The pig texture to use for this variant.",
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
                "desc": "The baby pig texture to use for this variant.",
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

