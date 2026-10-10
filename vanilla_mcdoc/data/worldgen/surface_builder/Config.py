"""
Generated from symbols.json for ::java::data::worldgen::surface_builder::Config
Local link to file: vanilla_mcdoc/data/worldgen/surface_builder/Config.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.util.block_state.BlockState import BlockState


class Config(GeneratedModel):
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
