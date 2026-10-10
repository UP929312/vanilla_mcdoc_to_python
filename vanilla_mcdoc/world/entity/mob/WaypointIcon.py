"""
Generated from symbols.json for ::java::world::entity::mob::WaypointIcon
Local link to file: vanilla_mcdoc/world/entity/mob/WaypointIcon.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.util.color.RGB import RGB


class WaypointIcon(GeneratedModel):
    style: Annotated[str, IdSpec(registry='waypoint_style')]
    color: RGB | None = None
