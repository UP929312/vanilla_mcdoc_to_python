"""
Generated from symbols.json for ::java::data::enchantment::effect::SetEffectValue
Local link to file: generated_symbols/data/enchantment/effect/SetEffectValue.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.enchantment.LevelBasedValue import LevelBasedValue


class SetEffectValue(GeneratedModel):
    value: LevelBasedValue


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::effect::SetEffectValue": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "value",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::enchantment::LevelBasedValue"
                }
            }
        ]
    }
}

