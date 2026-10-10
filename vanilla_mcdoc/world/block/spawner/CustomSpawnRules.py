"""
Generated from symbols.json for ::java::world::block::spawner::CustomSpawnRules
Local link to file: vanilla_mcdoc/world/block/spawner/CustomSpawnRules.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.util.InclusiveRange import InclusiveRange


class CustomSpawnRules(GeneratedModel):
    block_light_limit: InclusiveRange[Annotated[int, Field(ge=0, le=15)]] | Annotated[int, Field(ge=0, le=15)] | None = None  # Range of block light level required for the entity to spawn.
    sky_light_limit: InclusiveRange[Annotated[int, Field(ge=0, le=15)]] | Annotated[int, Field(ge=0, le=15)] | None = None  # Range of sky light level required for the entity to spawn.
