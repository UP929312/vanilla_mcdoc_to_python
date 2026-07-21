# Generated from symbols.json for ::java::assets::item_definition::MainHand
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.assets.item_definition.SelectCases import SelectCases

if TYPE_CHECKING:
    from generated_symbols.util.avatar.HumanoidArm import HumanoidArm


@dataclass(kw_only=True)
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

