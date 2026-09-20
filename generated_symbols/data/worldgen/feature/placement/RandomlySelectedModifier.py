"""
Generated from symbols.json for ::java::data::worldgen::feature::placement::RandomlySelectedModifier
Local link to file: generated_symbols/data/worldgen/feature/placement/RandomlySelectedModifier.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from generated_symbols.base import GeneratedModel
from pydantic import Field

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.feature.placement.PlacementModifier import PlacementModifier


class RandomlySelectedModifier(GeneratedModel):
    placements: Annotated[list[PlacementModifier], Field(min_length=1)]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::placement::RandomlySelectedModifier": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "placements",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::data::worldgen::feature::placement::PlacementModifier"
                    },
                    "lengthRange": {
                        "kind": 0,
                        "min": 1
                    }
                }
            }
        ]
    }
}

