# Generated from symbols.json for ::java::data::enchantment::level_based_value::LevelBasedValue
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.enchantment.level_based_value.LevelBasedValueMap import LevelBasedValueMap


type LevelBasedValue = float | LevelBasedValueMap


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::level_based_value::LevelBasedValue": {
        "kind": "union",
        "members": [
            {
                "kind": "float"
            },
            {
                "kind": "reference",
                "path": "::java::data::enchantment::level_based_value::LevelBasedValueMap"
            }
        ]
    }
}

