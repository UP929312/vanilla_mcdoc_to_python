# Generated from symbols.json for ::java::data::worldgen::carver::CarverDebugSettings
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.util.block_state.BlockState import BlockState


@dataclass(kw_only=True)
class CarverDebugSettings:
    air_state: BlockState
    water_state: BlockState
    lava_state: BlockState
    barrier_state: BlockState
    debug_mode: bool | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::carver::CarverDebugSettings": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "debug_mode",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "air_state",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::block_state::BlockState"
                }
            },
            {
                "kind": "pair",
                "key": "water_state",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::block_state::BlockState"
                }
            },
            {
                "kind": "pair",
                "key": "lava_state",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::block_state::BlockState"
                }
            },
            {
                "kind": "pair",
                "key": "barrier_state",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::block_state::BlockState"
                }
            }
        ]
    }
}

