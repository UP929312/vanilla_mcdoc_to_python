# Generated from symbols.json for ::java::data::enchantment::effect::ExponentialEffectValue
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.enchantment.LevelBasedValue import LevelBasedValue


@dataclass(kw_only=True)
class ExponentialEffectValue:
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

