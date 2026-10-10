"""
Generated from symbols.json for ::java::data::worldgen::feature::placement::RandomlySelectedModifier
Local link to file: vanilla_mcdoc/data/worldgen/feature/placement/RandomlySelectedModifier.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.feature.placement.PlacementModifier import PlacementModifier


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
