"""
Generated from symbols.json for ::java::world::component::item::Fireworks
Local link to file: vanilla_mcdoc/world/component/item/Fireworks.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.world.component.item.Explosion import Explosion


class Fireworks(GeneratedModel):
    explosions: Annotated[list[Explosion], Field(min_length=0, max_length=256)] | None = None
    flight_duration: int | None = None
