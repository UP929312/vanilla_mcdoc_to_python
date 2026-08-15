"""
Generated from symbols.json for ::java::data::worldgen::feature::block_predicate::VolumeMatchPredicate
Local link to file: generated_symbols/data/worldgen/feature/block_predicate/VolumeMatchPredicate.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.feature.block_predicate.BlockPredicate import BlockPredicate


@dataclass(kw_only=True)
class VolumeMatchPredicate:
    min: tuple[Annotated[int, 'Range | `-16`-`16` | both inclusive'], Annotated[int, 'Range | `-16`-`16` | both inclusive'], Annotated[int, 'Range | `-16`-`16` | both inclusive']]
    max: tuple[Annotated[int, 'Range | `-16`-`16` | both inclusive'], Annotated[int, 'Range | `-16`-`16` | both inclusive'], Annotated[int, 'Range | `-16`-`16` | both inclusive']]
    match: BlockPredicate


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::block_predicate::VolumeMatchPredicate": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "min",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "int",
                        "valueRange": {
                            "kind": 0,
                            "min": -16,
                            "max": 16
                        }
                    },
                    "lengthRange": {
                        "kind": 0,
                        "min": 3,
                        "max": 3
                    }
                }
            },
            {
                "kind": "pair",
                "key": "max",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "int",
                        "valueRange": {
                            "kind": 0,
                            "min": -16,
                            "max": 16
                        }
                    },
                    "lengthRange": {
                        "kind": 0,
                        "min": 3,
                        "max": 3
                    }
                }
            },
            {
                "kind": "pair",
                "key": "match",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::feature::block_predicate::BlockPredicate"
                }
            }
        ]
    }
}

