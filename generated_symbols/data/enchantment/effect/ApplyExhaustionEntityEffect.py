"""
Generated from symbols.json for ::java::data::enchantment::effect::ApplyExhaustionEntityEffect
Local link to file: generated_symbols/data/enchantment/effect/ApplyExhaustionEntityEffect.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.enchantment.LevelBasedValue import LevelBasedValue


class ApplyExhaustionEntityEffect(GeneratedModel):
    amount: LevelBasedValue  # The amount of exhaustion to apply to player.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::effect::ApplyExhaustionEntityEffect": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "The amount of exhaustion to apply to player.",
                "key": "amount",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::enchantment::LevelBasedValue"
                }
            }
        ]
    }
}

