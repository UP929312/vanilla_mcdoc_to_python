# Generated from symbols.json for ::java::assets::item_definition::ChargeType
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.assets.item_definition.SelectCases import SelectCases

if TYPE_CHECKING:
    from generated_symbols.assets.item_definition.CrossbowChargeType import CrossbowChargeType


@dataclass(kw_only=True)
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

