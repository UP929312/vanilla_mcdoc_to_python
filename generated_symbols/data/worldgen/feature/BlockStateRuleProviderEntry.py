# Generated from symbols.json for ::java::data::worldgen::feature::BlockStateRuleProviderEntry
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.feature.block_predicate.BlockPredicate import BlockPredicate
    from generated_symbols.data.worldgen.feature.block_state_provider.BlockStateProvider import BlockStateProvider


@dataclass(kw_only=True)
class BlockStateRuleProviderEntry:
    if_true: BlockPredicate
    then: BlockStateProvider


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::BlockStateRuleProviderEntry": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "if_True",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::feature::block_predicate::BlockPredicate"
                }
            },
            {
                "kind": "pair",
                "key": "then",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::feature::block_state_provider::BlockStateProvider"
                }
            }
        ]
    }
}

