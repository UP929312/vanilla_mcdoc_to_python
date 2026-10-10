"""
Generated from symbols.json for ::java::data::worldgen::structure::RuinedPortalSetup
Local link to file: vanilla_mcdoc/data/worldgen/structure/RuinedPortalSetup.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.structure.RuinedPortalPlacement import RuinedPortalPlacement


class RuinedPortalSetup(GeneratedModel):
    placement: RuinedPortalPlacement
    air_pocket_probability: Annotated[float, Field(ge=0, le=1)]
    mossiness: Annotated[float, Field(ge=0, le=1)]
    overgrown: bool
    vines: bool
    can_be_cold: bool
    replace_with_blackstone: bool
    weight: Annotated[float, Field(ge=0)]
