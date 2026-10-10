"""
Generated from symbols.json for ::java::world::entity::display::Rotation
Local link to file: vanilla_mcdoc/world/entity/display/Rotation.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from vanilla_mcdoc.world.entity.display.AxisAngle import AxisAngle


type Rotation = tuple[float, float, float, float] | AxisAngle
