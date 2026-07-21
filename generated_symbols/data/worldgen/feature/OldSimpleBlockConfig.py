# Generated from symbols.json for ::java::data::worldgen::feature::OldSimpleBlockConfig
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.util.block_state.BlockState import BlockState


@dataclass(kw_only=True)
class OldSimpleBlockConfig:
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

