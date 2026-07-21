# Generated from symbols.json for ::java::data::worldgen::feature::block_predicate::WouldSurvivePredicate
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.data.worldgen.feature.block_predicate.PredicateOffset import PredicateOffset

if TYPE_CHECKING:
    from generated_symbols.util.block_state.BlockState import BlockState


@dataclass(kw_only=True)
class WouldSurvivePredicate(PredicateOffset):
    state: BlockState


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::block_predicate::WouldSurvivePredicate": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::feature::block_predicate::PredicateOffset"
                }
            },
            {
                "kind": "pair",
                "key": "state",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::block_state::BlockState"
                }
            }
        ]
    }
}

