# Generated from symbols.json for ::java::data::worldgen::feature::tree::BendingTrunkPlacer
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.IntProvider import IntProvider


@dataclass(kw_only=True)
class BendingTrunkPlacer:
    bend_length: IntProvider[Annotated[int, 'Range | `1`-`64` | both inclusive']] | Annotated[int, 'Range | `1`-`64` | both inclusive']
    min_height_for_leaves: Annotated[int, 'Range | Min `1` and above | inclusive'] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::tree::BendingTrunkPlacer": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "bend_length",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::data::worldgen::IntProvider"
                    },
                    "typeArgs": [
                        {
                            "kind": "int",
                            "valueRange": {
                                "kind": 0,
                                "min": 1,
                                "max": 64
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "min_height_for_leaves",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 1
                    }
                },
                "optional": True
            }
        ]
    }
}

