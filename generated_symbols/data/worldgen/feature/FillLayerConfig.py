"""
Generated from symbols.json for ::java::data::worldgen::feature::FillLayerConfig
Local link to file: generated_symbols/data/worldgen/feature/FillLayerConfig.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, ClassVar

if TYPE_CHECKING:
    from generated_symbols.util.block_state.BlockState import BlockState


@dataclass(kw_only=True)
class FillLayerConfig:
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    state: BlockState
    height: Annotated[int, 'Range | `0`-`255` | both inclusive']


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::FillLayerConfig": {
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
                "key": "height",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 255
                    }
                }
            }
        ]
    }
}

