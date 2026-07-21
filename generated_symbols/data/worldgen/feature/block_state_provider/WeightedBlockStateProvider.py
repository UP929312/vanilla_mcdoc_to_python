# Generated from symbols.json for ::java::data::worldgen::feature::block_state_provider::WeightedBlockStateProvider
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.util.NonEmptyWeightedList import NonEmptyWeightedList
    from generated_symbols.util.block_state.BlockState import BlockState


@dataclass(kw_only=True)
class WeightedBlockStateProvider:
    entries: NonEmptyWeightedList[BlockState]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::block_state_provider::WeightedBlockStateProvider": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "entries",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::util::NonEmptyWeightedList"
                    },
                    "typeArgs": [
                        {
                            "kind": "reference",
                            "path": "::java::util::block_state::BlockState"
                        }
                    ]
                }
            }
        ]
    }
}

