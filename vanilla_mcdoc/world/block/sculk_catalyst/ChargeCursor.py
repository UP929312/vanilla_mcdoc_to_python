"""
Generated from symbols.json for ::java::world::block::sculk_catalyst::ChargeCursor
Local link to file: vanilla_mcdoc/world/block/sculk_catalyst/ChargeCursor.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.util.direction.Direction import Direction


class ChargeCursor(GeneratedModel):
    pos: tuple[int, int, int]
    charge: Annotated[int, Field(ge=0, le=1000)] | None = None
    decay_delay: Annotated[int, Field(ge=0, le=1)] | None = None
    update_delay: Annotated[int, Field(ge=0)] | None = None
    facings: list[Direction] | None = None
