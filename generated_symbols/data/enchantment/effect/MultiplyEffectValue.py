# Generated from symbols.json for ::java::data::enchantment::effect::MultiplyEffectValue
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.enchantment.LevelBasedValue import LevelBasedValue


@dataclass(kw_only=True)
class MultiplyEffectValue:
    factor: LevelBasedValue  # Level-Based Value determining the factor to multiply in


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::effect::MultiplyEffectValue": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Level-Based Value determining the factor to multiply in",
                "key": "factor",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::enchantment::LevelBasedValue"
                }
            }
        ]
    }
}

