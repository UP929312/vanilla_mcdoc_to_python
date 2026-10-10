"""
Generated from symbols.json for ::java::world::component::item::DyedColor
Local link to file: vanilla_mcdoc/world/component/item/DyedColor.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel


class DyedColor(GeneratedModel):
    rgb: int  # Color of the armor. Calculated as `RED << 16 | GREEN << 8 | BLUE`. Each of these fields must be between 0 and 255, inclusive.
    show_in_tooltip: bool | None = None
