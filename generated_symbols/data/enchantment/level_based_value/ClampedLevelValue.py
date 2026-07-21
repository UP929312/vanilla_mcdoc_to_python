# Generated from symbols.json for ::java::data::enchantment::level_based_value::ClampedLevelValue
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.enchantment.level_based_value.LevelBasedValue import LevelBasedValue


@dataclass(kw_only=True)
class ClampedLevelValue:
    value: LevelBasedValue
    min: float
    max: float


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::level_based_value::ClampedLevelValue": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "value",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::enchantment::level_based_value::LevelBasedValue"
                }
            },
            {
                "kind": "pair",
                "key": "min",
                "type": {
                    "kind": "float"
                }
            },
            {
                "kind": "pair",
                "key": "max",
                "type": {
                    "kind": "float"
                }
            }
        ]
    }
}

