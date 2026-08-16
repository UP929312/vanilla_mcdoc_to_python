"""
Generated from symbols.json for ::java::data::worldgen::feature::ForestRockConfig
Local link to file: generated_symbols/data/worldgen/feature/ForestRockConfig.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from generated_symbols.util.block_state.BlockState import BlockState


@dataclass(kw_only=True)
class ForestRockConfig:
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    state: BlockState


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::ForestRockConfig": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "state",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::block_state::BlockState"
                }
            }
        ]
    }
}

