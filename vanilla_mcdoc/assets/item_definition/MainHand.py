"""
Generated from symbols.json for ::java::assets::item_definition::MainHand
Local link to file: vanilla_mcdoc/assets/item_definition/MainHand.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.assets.item_definition.SelectCases import SelectCases
from vanilla_mcdoc.util.avatar.HumanoidArm import HumanoidArm


class MainHand(SelectCases[HumanoidArm]):
    pass


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::item_definition::MainHand": {
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
                            "path": "::java::util::avatar::HumanoidArm"
                        }
                    ]
                }
            }
        ]
    }
}
