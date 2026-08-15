"""
Generated from symbols.json for ::java::data::worldgen::feature::placement::RandomlySelectedModifier
Local link to file: generated_symbols/data/worldgen/feature/placement/RandomlySelectedModifier.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.feature.placement.PlacementModifier import PlacementModifier


@dataclass(kw_only=True)
class RandomlySelectedModifier:
    placements: Annotated[list[PlacementModifier], 'Length = 1 (inclusive) and above']


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

