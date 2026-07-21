# Generated from symbols.json for ::java::data::enchantment::effect::ReduceBinomialEffectValue
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.enchantment.LevelBasedValue import LevelBasedValue


@dataclass(kw_only=True)
class ReduceBinomialEffectValue:
    chance: LevelBasedValue  # Chance that an input value is dropped by 1.  The span is 0 to 1, with 0 being no chance to drop an input value and 1 dropping all input values.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::effect::ReduceBinomialEffectValue": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Chance that an input value is dropped by 1.\n\nThe span is 0 to 1, with 0 being no chance to drop an input value and 1 dropping all input values.",
                "key": "chance",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::enchantment::LevelBasedValue"
                }
            }
        ]
    }
}

