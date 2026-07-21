# Generated from symbols.json for ::java::data::worldgen::processor_list::RandomBlockStateMatch
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.util.block_state.BlockState import BlockState


@dataclass(kw_only=True)
class RandomBlockStateMatch:
    block_state: BlockState
    probability: Annotated[float, 'Range | `0`-`1` | both inclusive']


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::processor_list::RandomBlockStateMatch": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "block_state",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::block_state::BlockState"
                }
            },
            {
                "kind": "pair",
                "key": "probability",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 1
                    }
                }
            }
        ]
    }
}

