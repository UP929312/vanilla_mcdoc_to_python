# Generated from symbols.json for ::java::data::worldgen::feature::tree::PoplarTrunkPlacer
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.IntProvider import IntProvider


@dataclass(kw_only=True)
class PoplarTrunkPlacer:
    trunk_height_above_branches: IntProvider[Annotated[int, 'Range | `0`-`8` | both inclusive']] | Annotated[int, 'Range | `0`-`8` | both inclusive']
    branch_amount: IntProvider[Annotated[int, 'Range | `1`-`4` | both inclusive']] | Annotated[int, 'Range | `1`-`4` | both inclusive']


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::tree::PoplarTrunkPlacer": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "trunk_height_above_branches",
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
                                "min": 0,
                                "max": 8
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "branch_amount",
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
                                "max": 4
                            }
                        }
                    ]
                }
            }
        ]
    }
}

