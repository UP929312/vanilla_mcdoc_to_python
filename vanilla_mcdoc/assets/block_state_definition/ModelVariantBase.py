"""
Generated from symbols.json for ::java::assets::block_state_definition::ModelVariantBase
Local link to file: vanilla_mcdoc/assets/block_state_definition/ModelVariantBase.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Literal

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.assets.model.ModelRef import ModelRef


class ModelVariantBase(GeneratedModel):
    model: ModelRef
    x: Literal[0] | Literal[90] | Literal[180] | Literal[270] | None = None
    y: Literal[0] | Literal[90] | Literal[180] | Literal[270] | None = None
    z: Literal[0] | Literal[90] | Literal[180] | Literal[270] | None = None
    uvlock: bool | None = None  # If set to `true`, the textures are not rotated with the block.
