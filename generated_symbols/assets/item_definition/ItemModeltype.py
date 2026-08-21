"""
Generated from symbols.json for ::java::assets::item_definition::ItemModeltype
Local link to file: generated_symbols/assets/item_definition/ItemModeltype.py
"""
# ~~~ CODE ~~~
from enum import StrEnum


class ItemModeltype(StrEnum):
    BUNDLESELECTEDITEM = "bundle/selected_item"
    COMPOSITE = "composite"
    CONDITION = "condition"
    EMPTY = "empty"
    MODEL = "model"
    RANGEDISPATCH = "range_dispatch"
    SELECT = "select"
    SPECIAL = "special"


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::item_definition::ItemModeltype": {
        "kind": "enum",
        "enumKind": "string",
        "values": [
            {
                "identifier": "BundleSelectedItem",
                "value": "bundle/selected_item"
            },
            {
                "identifier": "Composite",
                "value": "composite"
            },
            {
                "identifier": "Condition",
                "value": "condition"
            },
            {
                "identifier": "Empty",
                "value": "empty"
            },
            {
                "identifier": "Model",
                "value": "model"
            },
            {
                "identifier": "RangeDispatch",
                "value": "range_dispatch"
            },
            {
                "identifier": "Select",
                "value": "select"
            },
            {
                "identifier": "Special",
                "value": "special"
            }
        ]
    }
}

