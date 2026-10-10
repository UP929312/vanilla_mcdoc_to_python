"""
Generated from symbols.json for ::java::assets::item_definition::ConditionalPropertyType
Local link to file: vanilla_mcdoc/assets/item_definition/ConditionalPropertyType.py
"""
# ~~~ CODE ~~~
from enum import StrEnum


class ConditionalPropertyType(StrEnum):
    BROKEN = "broken"
    BUNDLEHASSELECTEDITEM = "bundle/has_selected_item"
    CARRIED = "carried"
    COMPONENT = "component"
    CUSTOMMODELDATA = "custom_model_data"
    DAMAGED = "damaged"
    EXTENDEDVIEW = "extended_view"
    FISHINGROD = "fishing_rod/cast"
    HASCOMPONENT = "has_component"
    KEYBINDDOWN = "keybind_down"
    SELECTED = "selected"
    USINGITEM = "using_item"
    VIEWENTITY = "view_entity"
