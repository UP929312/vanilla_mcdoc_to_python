"""
Generated from symbols.json for ::java::data::worldgen::feature::FillLayerConfig
Local link to file: generated_symbols/data/worldgen/feature/FillLayerConfig.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar

from pydantic import Field

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.util.block_state.BlockState import BlockState


class FillLayerConfig(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    state: BlockState
    height: Annotated[int, Field(ge=0, le=255)]


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
