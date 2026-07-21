# Generated from symbols.json for ::java::assets::item_definition::ConditionalPropertyType
from enum import Enum


class ConditionalPropertyType(Enum):
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


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::item_definition::ConditionalPropertyType": {
        "kind": "enum",
        "enumKind": "string",
        "values": [
            {
                "identifier": "Broken",
                "value": "broken"
            },
            {
                "identifier": "BundleHasSelectedItem",
                "value": "bundle/has_selected_item"
            },
            {
                "identifier": "Carried",
                "value": "carried"
            },
            {
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.5"
                            }
                        }
                    }
                ],
                "identifier": "Component",
                "value": "component"
            },
            {
                "identifier": "CustomModelData",
                "value": "custom_model_data"
            },
            {
                "identifier": "Damaged",
                "value": "damaged"
            },
            {
                "identifier": "ExtendedView",
                "value": "extended_view"
            },
            {
                "identifier": "FishingRod",
                "value": "fishing_rod/cast"
            },
            {
                "identifier": "HasComponent",
                "value": "has_component"
            },
            {
                "identifier": "KeybindDown",
                "value": "keybind_down"
            },
            {
                "identifier": "Selected",
                "value": "selected"
            },
            {
                "identifier": "UsingItem",
                "value": "using_item"
            },
            {
                "identifier": "ViewEntity",
                "value": "view_entity"
            }
        ]
    }
}

