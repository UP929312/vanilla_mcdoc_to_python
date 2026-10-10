"""
Generated from symbols.json for ::java::world::entity::display::Billboard
Local link to file: vanilla_mcdoc/world/entity/display/Billboard.py
"""
# ~~~ CODE ~~~
from enum import StrEnum


class Billboard(StrEnum):
    FIXED = "fixed"  # No rotation.
    VERTICAL = "vertical"  # Pivot around the vertical axis.
    HORIZONTAL = "horizontal"  # Pivot around the horizontal axis.
    CENTER = "center"  # Pivot around both axes.
