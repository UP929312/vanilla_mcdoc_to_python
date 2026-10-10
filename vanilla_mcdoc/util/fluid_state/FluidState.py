"""
Generated from symbols.json for ::java::util::fluid_state::FluidState
Local link to file: vanilla_mcdoc/util/fluid_state/FluidState.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec


class FluidStateStruct(GeneratedModel):
    id: Annotated[str, IdSpec(registry='fluid')]
    properties: dict[str, str] | None = None


type FluidState = Annotated[str, IdSpec(registry='fluid')] | FluidStateStruct
