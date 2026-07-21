# Generated from symbols.json for ::java::data::enchantment::level_based_value::FractionLevelValue
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.enchantment.level_based_value.LevelBasedValue import LevelBasedValue


@dataclass(kw_only=True)
class FractionLevelValue:
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

