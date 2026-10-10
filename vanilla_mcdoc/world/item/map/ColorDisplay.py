"""
Generated from symbols.json for ::java::world::item::map::ColorDisplay
Local link to file: vanilla_mcdoc/world/item/map/ColorDisplay.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.world.item.Display import Display


class ColorDisplay(Display):
    MapColor: int | None = None  # Calculated as `RED << 16 | GREEN << 8 | BLUE`. Each of these fields must be between 0 and 255, inclusive.
