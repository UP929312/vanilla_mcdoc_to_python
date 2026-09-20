"""
Generated from symbols.json for ::java::data::worldgen::feature::OldSimpleBlockConfig
Local link to file: generated_symbols/data/worldgen/feature/OldSimpleBlockConfig.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.util.block_state.BlockState import BlockState


class OldSimpleBlockConfig(GeneratedModel):
    place_on: list[BlockState]
    place_in: list[BlockState]
    place_under: list[BlockState]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::OldSimpleBlockConfig": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "place_on",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::util::block_state::BlockState"
                    }
                }
            },
            {
                "kind": "pair",
                "key": "place_in",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::util::block_state::BlockState"
                    }
                }
            },
            {
                "kind": "pair",
                "key": "place_under",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::util::block_state::BlockState"
                    }
                }
            }
        ]
    }
}

