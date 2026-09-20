"""
Generated from symbols.json for ::java::data::worldgen::feature::placement::EnvironmentScanModifier
Local link to file: generated_symbols/data/worldgen/feature/placement/EnvironmentScanModifier.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from generated_symbols.base import GeneratedModel
from pydantic import Field

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.feature.block_predicate.BlockPredicate import BlockPredicate
    from generated_symbols.util.direction.VerticalDirection import VerticalDirection


class EnvironmentScanModifier(GeneratedModel):
    direction_of_search: VerticalDirection
    max_steps: Annotated[int, Field(ge=1, le=32)]
    target_condition: BlockPredicate
    allowed_search_condition: BlockPredicate | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::placement::EnvironmentScanModifier": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "direction_of_search",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::direction::VerticalDirection"
                }
            },
            {
                "kind": "pair",
                "key": "max_steps",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 1,
                        "max": 32
                    }
                }
            },
            {
                "kind": "pair",
                "key": "target_condition",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::feature::block_predicate::BlockPredicate"
                }
            },
            {
                "kind": "pair",
                "key": "allowed_search_condition",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::feature::block_predicate::BlockPredicate"
                },
                "optional": True
            }
        ]
    }
}

