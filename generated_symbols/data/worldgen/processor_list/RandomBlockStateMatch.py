"""
Generated from symbols.json for ::java::data::worldgen::processor_list::RandomBlockStateMatch
Local link to file: generated_symbols/data/worldgen/processor_list/RandomBlockStateMatch.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.util.block_state.BlockState import BlockState


class RandomBlockStateMatch(GeneratedModel):
    block_state: BlockState
    probability: Annotated[float, Field(ge=0, le=1)]


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

