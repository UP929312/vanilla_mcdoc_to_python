"""
Generated from symbols.json for ::java::world::entity::display::DecomposedTransformation
Local link to file: vanilla_mcdoc/world/entity/display/DecomposedTransformation.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.world.entity.display.Rotation import Rotation


class DecomposedTransformation(GeneratedModel):
    translation: tuple[float, float, float]  # Translation in [x, y, z].
    left_rotation: Rotation  # Using this rotation is enough for most transformations.
    right_rotation: Rotation  # For more complex transformations. Applied **before** scaling.
    scale: tuple[float, float, float]  # Scale in [x, y, z].
