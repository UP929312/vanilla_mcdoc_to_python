"""
Generated from symbols.json for ::java::world::component::item::AttributeDisplayType
Local link to file: generated_symbols/world/component/item/AttributeDisplayType.py
"""
# ~~~ CODE ~~~
from enum import StrEnum


class AttributeDisplayType(StrEnum):
    DEFAULT = "default"  # Shows the calculated attribute modifier values on the tooltip.
    HIDDEN = "hidden"  # Does not show the attribute modifier entry in tooltips.
    OVERRIDE = "override"  # Replaces the shown attribute modifier text.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::item::AttributeDisplayType": {
        "kind": "enum",
        "enumKind": "string",
        "values": [
            {
                "desc": "Shows the calculated attribute modifier values on the tooltip.",
                "identifier": "Default",
                "value": "default"
            },
            {
                "desc": "Does not show the attribute modifier entry in tooltips.",
                "identifier": "Hidden",
                "value": "hidden"
            },
            {
                "desc": "Replaces the shown attribute modifier text.",
                "identifier": "Override",
                "value": "override"
            }
        ]
    }
}

