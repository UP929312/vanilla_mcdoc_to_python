"""
Generated from symbols.json for ::java::data::variants::frog::FrogVariant
Local link to file: generated_symbols/data/variants/frog/FrogVariant.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Annotated, ClassVar

from generated_symbols.data.variants.SpawnPrioritySelectors import SpawnPrioritySelectors
from minecraft_registry import IdSpec


@dataclass(kw_only=True)
class FrogVariant(SpawnPrioritySelectors):
    __resource_dir__: ClassVar[str] = 'frog_variant'

    asset_id: Annotated[str, IdSpec(registry='texture')]  # The frog texture to use for this variant.


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

