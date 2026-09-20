"""
Generated from symbols.json for ::java::data::enchantment::effect::ExponentialEffectValue
Local link to file: generated_symbols/data/enchantment/effect/ExponentialEffectValue.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.enchantment.LevelBasedValue import LevelBasedValue


class ExponentialEffectValue(GeneratedModel):
    base: LevelBasedValue
    exponent: LevelBasedValue


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::effect::ExponentialEffectValue": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "base",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::enchantment::LevelBasedValue"
                }
            },
            {
                "kind": "pair",
                "key": "exponent",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::enchantment::LevelBasedValue"
                }
            }
        ]
    }
}

