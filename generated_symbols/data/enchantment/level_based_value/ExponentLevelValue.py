"""
Generated from symbols.json for ::java::data::enchantment::level_based_value::ExponentLevelValue
Local link to file: generated_symbols/data/enchantment/level_based_value/ExponentLevelValue.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.enchantment.level_based_value.LevelBasedValue import LevelBasedValue


class ExponentLevelValue(GeneratedModel):
    base: LevelBasedValue
    power: LevelBasedValue


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::level_based_value::ExponentLevelValue": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "base",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::enchantment::level_based_value::LevelBasedValue"
                }
            },
            {
                "kind": "pair",
                "key": "power",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::enchantment::level_based_value::LevelBasedValue"
                }
            }
        ]
    }
}

