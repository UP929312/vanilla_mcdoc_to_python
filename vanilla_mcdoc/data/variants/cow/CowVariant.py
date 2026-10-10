"""
Generated from symbols.json for ::java::data::variants::cow::CowVariant
Local link to file: vanilla_mcdoc/data/variants/cow/CowVariant.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar

from vanilla_mcdoc.data.variants.SpawnPrioritySelectors import SpawnPrioritySelectors
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.variants.cow.CowModelType import CowModelType


class CowVariant(SpawnPrioritySelectors):
    __resource_dir__: ClassVar[str] = 'cow_variant'

    model: CowModelType | None = None
    asset_id: Annotated[str, IdSpec(registry='texture')]  # The cow texture to use for this variant.
    baby_asset_id: Annotated[str, IdSpec(registry='texture')]  # The baby cow texture to use for this variant.


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
