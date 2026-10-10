"""
Generated from symbols.json for ::java::world::component::item::AttributeDisplayType
Local link to file: vanilla_mcdoc/world/component/item/AttributeDisplayType.py
"""
# ~~~ CODE ~~~
from enum import StrEnum


class AttributeDisplayType(StrEnum):
    DEFAULT = "default"  # Shows the calculated attribute modifier values on the tooltip.
    HIDDEN = "hidden"  # Does not show the attribute modifier entry in tooltips.
    OVERRIDE = "override"  # Replaces the shown attribute modifier text.
