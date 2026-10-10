"""
Generated from symbols.json for ::java::data::worldgen::feature::EmeraldOreConfig
Local link to file: generated_symbols/data/worldgen/feature/EmeraldOreConfig.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.util.block_state.BlockState import BlockState


class EmeraldOreConfig(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    state: BlockState
    target: BlockState


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::EmeraldOreConfig": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "state",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::block_state::BlockState"
                }
            },
            {
                "kind": "pair",
                "key": "target",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::block_state::BlockState"
                }
            }
        ]
    }
}
