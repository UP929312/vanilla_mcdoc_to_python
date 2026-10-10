"""
Generated from symbols.json for ::java::data::worldgen::feature::block_predicate::VolumeMatchPredicate
Local link to file: generated_symbols/data/worldgen/feature/block_predicate/VolumeMatchPredicate.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.feature.block_predicate.BlockPredicate import BlockPredicate


class VolumeMatchPredicate(GeneratedModel):
    min: tuple[Annotated[int, Field(ge=-16, le=16)], Annotated[int, Field(ge=-16, le=16)], Annotated[int, Field(ge=-16, le=16)]]
    max: tuple[Annotated[int, Field(ge=-16, le=16)], Annotated[int, Field(ge=-16, le=16)], Annotated[int, Field(ge=-16, le=16)]]
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

