# Generated from symbols.json for ::java::data::worldgen::feature::tree::RandomSpreadFoliagePlacer
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.IntProvider import IntProvider


@dataclass(kw_only=True)
class RandomSpreadFoliagePlacer:
    foliage_height: IntProvider[Annotated[int, 'Range | `1`-`512` | both inclusive']] | Annotated[int, 'Range | `1`-`512` | both inclusive']
    leaf_placement_attempts: Annotated[int, 'Range | `0`-`256` | both inclusive']


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::tree::RandomSpreadFoliagePlacer": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "foliage_height",
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
                                "max": 512
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "leaf_placement_attempts",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 256
                    }
                }
            }
        ]
    }
}

