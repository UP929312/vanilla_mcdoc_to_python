# Generated from symbols.json for ::java::data::enchantment::level_based_value::LookupLevelValue
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.data.enchantment.level_based_value.LevelBasedValue import LevelBasedValue


@dataclass(kw_only=True)
class LookupLevelValue:
    values: Annotated[list[LevelBasedValue], 'Length = 1 (inclusive) and above']  # Indexed by `level - 1` to apply, if present
    fallback: LevelBasedValue  # Applied if the level is greater than the size of `values`.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::level_based_value::LookupLevelValue": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Indexed by `level - 1` to apply, if present",
                "key": "values",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::data::enchantment::level_based_value::LevelBasedValue"
                    },
                    "lengthRange": {
                        "kind": 0,
                        "min": 1
                    }
                }
            },
            {
                "kind": "pair",
                "desc": "Applied if the level is greater than the size of `values`.",
                "key": "fallback",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::enchantment::level_based_value::LevelBasedValue"
                }
            }
        ]
    }
}

