"""
Generated from symbols.json for ::java::assets::item_definition::ChargeType
Local link to file: vanilla_mcdoc/assets/item_definition/ChargeType.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.assets.item_definition.CrossbowChargeType import CrossbowChargeType
from vanilla_mcdoc.assets.item_definition.SelectCases import SelectCases


class ChargeType(SelectCases[CrossbowChargeType]):
    pass


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::item_definition::ChargeType": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::assets::item_definition::SelectCases"
                    },
                    "typeArgs": [
                        {
                            "kind": "reference",
                            "path": "::java::assets::item_definition::CrossbowChargeType"
                        }
                    ]
                }
            }
        ]
    }
}
