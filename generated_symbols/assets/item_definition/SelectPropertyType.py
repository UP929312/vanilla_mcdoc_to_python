# Generated from symbols.json for ::java::assets::item_definition::SelectPropertyType
from enum import Enum


class SelectPropertyType(Enum):
    BLOCKSTATE = "block_state"
    CHARGETYPE = "charge_type"
    COMPONENT = "component"
    CONTEXTDIMENSION = "context_dimension"
    CONTEXTENTITYTYPE = "context_entity_type"
    CUSTOMMODELDATA = "custom_model_data"
    DISPLAYCONTEXT = "display_context"
    LOCALTIME = "local_time"
    MAINHAND = "main_hand"
    TRIMMATERIAL = "trim_material"


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::item_definition::SelectPropertyType": {
        "kind": "enum",
        "enumKind": "string",
        "values": [
            {
                "identifier": "BlockState",
                "value": "block_state"
            },
            {
                "identifier": "ChargeType",
                "value": "charge_type"
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
                "identifier": "ContextDimension",
                "value": "context_dimension"
            },
            {
                "identifier": "ContextEntityType",
                "value": "context_entity_type"
            },
            {
                "identifier": "CustomModelData",
                "value": "custom_model_data"
            },
            {
                "identifier": "DisplayContext",
                "value": "display_context"
            },
            {
                "identifier": "LocalTime",
                "value": "local_time"
            },
            {
                "identifier": "MainHand",
                "value": "main_hand"
            },
            {
                "identifier": "TrimMaterial",
                "value": "trim_material"
            }
        ]
    }
}

