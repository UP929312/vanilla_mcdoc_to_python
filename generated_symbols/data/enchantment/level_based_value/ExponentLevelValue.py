# Generated from symbols.json for ::java::data::enchantment::level_based_value::ExponentLevelValue
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.enchantment.level_based_value.LevelBasedValue import LevelBasedValue


@dataclass(kw_only=True)
class ExponentLevelValue:
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

