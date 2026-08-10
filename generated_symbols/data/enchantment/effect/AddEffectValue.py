"""
Generated from symbols.json for ::java::data::enchantment::effect::AddEffectValue
Local link to file: generated_symbols/data/enchantment/effect/AddEffectValue.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.enchantment.LevelBasedValue import LevelBasedValue


@dataclass(kw_only=True)
class AddEffectValue:
    value: LevelBasedValue


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::effect::AddEffectValue": {
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

