# Generated from symbols.json for ::java::data::worldgen::feature::placement::EnvironmentScanModifier
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.feature.block_predicate.BlockPredicate import BlockPredicate
    from generated_symbols.util.direction.VerticalDirection import VerticalDirection


@dataclass(kw_only=True)
class EnvironmentScanModifier:
    direction_of_search: VerticalDirection
    max_steps: Annotated[int, 'Range | `1`-`32` | both inclusive']
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

