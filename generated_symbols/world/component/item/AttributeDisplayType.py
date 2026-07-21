# Generated from symbols.json for ::java::world::component::item::AttributeDisplayType
from enum import Enum


class AttributeDisplayType(Enum):
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

