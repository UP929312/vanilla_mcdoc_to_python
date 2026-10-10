"""
Generated from symbols.json for ::java::data::enchantment::level_based_value::FractionLevelValue
Local link to file: vanilla_mcdoc/data/enchantment/level_based_value/FractionLevelValue.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.enchantment.level_based_value.LevelBasedValue import LevelBasedValue


class FractionLevelValue(GeneratedModel):
    numerator: LevelBasedValue
    denominator: LevelBasedValue


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::level_based_value::FractionLevelValue": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "numerator",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::enchantment::level_based_value::LevelBasedValue"
                }
            },
            {
                "kind": "pair",
                "key": "denominator",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::enchantment::level_based_value::LevelBasedValue"
                }
            }
        ]
    }
}
