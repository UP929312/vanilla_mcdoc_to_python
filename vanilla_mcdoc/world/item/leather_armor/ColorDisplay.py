"""
Generated from symbols.json for ::java::world::item::leather_armor::ColorDisplay
Local link to file: vanilla_mcdoc/world/item/leather_armor/ColorDisplay.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.world.item.Display import Display


class ColorDisplay(Display):
    color: int | None = None  # Color of the armor. Calculated as `RED << 16 | GREEN << 8 | BLUE`. Each of these fields must be between 0 and 255, inclusive.
