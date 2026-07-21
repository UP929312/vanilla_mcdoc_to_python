# Generated from symbols.json for ::java::data::worldgen::surface_builder::Config
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.util.block_state.BlockState import BlockState


@dataclass(kw_only=True)
class Config:
    top_material: BlockState
    under_material: BlockState
    underwater_material: BlockState


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::surface_builder::Config": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "top_material",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::block_state::BlockState"
                }
            },
            {
                "kind": "pair",
                "key": "under_material",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::block_state::BlockState"
                }
            },
            {
                "kind": "pair",
                "key": "underwater_material",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::block_state::BlockState"
                }
            }
        ]
    }
}

