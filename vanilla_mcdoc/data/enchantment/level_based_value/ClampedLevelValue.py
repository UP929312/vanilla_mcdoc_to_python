"""
Generated from symbols.json for ::java::data::enchantment::level_based_value::ClampedLevelValue
Local link to file: generated_symbols/data/enchantment/level_based_value/ClampedLevelValue.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.enchantment.level_based_value.LevelBasedValue import LevelBasedValue


class ClampedLevelValue(GeneratedModel):
    value: LevelBasedValue
    min: float
    max: float


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::level_based_value::ClampedLevelValue": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "value",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::enchantment::level_based_value::LevelBasedValue"
                }
            },
            {
                "kind": "pair",
                "key": "min",
                "type": {
                    "kind": "float"
                }
            },
            {
                "kind": "pair",
                "key": "max",
                "type": {
                    "kind": "float"
                }
            }
        ]
    }
}
