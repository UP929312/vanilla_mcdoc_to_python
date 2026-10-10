"""
Generated from symbols.json for ::java::assets::waypoint_style::WaypointStyle
Local link to file: vanilla_mcdoc/assets/waypoint_style/WaypointStyle.py
"""
# ~~~ CODE ~~~
from typing import Annotated, ClassVar

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec


class WaypointStyle(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'waypoint_style'

    near_distance: Annotated[int, Field(ge=0, le=60000000)] | None = None  # Defaults to 128.
    far_distance: Annotated[int, Field(ge=0, le=60000000)] | None = None  # Defaults to 322.
    sprites: Annotated[list[Annotated[str, IdSpec(registry='texture', path='gui/sprites/hud/locator_bar_dot/')]], Field(min_length=1)]
