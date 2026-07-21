# Generated from symbols.json for ::java::data::worldgen::feature::tree::CherryTrunkPlacer
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.IntProvider import IntProvider
    from generated_symbols.data.worldgen.UniformIntProvider import UniformIntProvider


@dataclass(kw_only=True)
class CherryTrunkPlacer:
    branch_count: IntProvider[Annotated[int, 'Range | `1`-`3` | both inclusive']] | Annotated[int, 'Range | `1`-`3` | both inclusive']
    branch_horizontal_length: IntProvider[Annotated[int, 'Range | `2`-`16` | both inclusive']] | Annotated[int, 'Range | `2`-`16` | both inclusive']
    branch_start_offset_from_top: UniformIntProvider[Annotated[int, 'Range | `-16`-`0` | both inclusive']] | Annotated[int, 'Range | `-16`-`0` | both inclusive']
    branch_end_offset_from_top: IntProvider[Annotated[int, 'Range | `-16`-`16` | both inclusive']] | Annotated[int, 'Range | `-16`-`16` | both inclusive']


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::tree::CherryTrunkPlacer": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "branch_count",
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
                                "max": 3
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "branch_horizontal_length",
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
                                "min": 2,
                                "max": 16
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "branch_start_offset_from_top",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::data::worldgen::UniformIntProvider"
                    },
                    "typeArgs": [
                        {
                            "kind": "int",
                            "valueRange": {
                                "kind": 0,
                                "min": -16,
                                "max": 0
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "branch_end_offset_from_top",
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
                                "min": -16,
                                "max": 16
                            }
                        }
                    ]
                }
            }
        ]
    }
}

