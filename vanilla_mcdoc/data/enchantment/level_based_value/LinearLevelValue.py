"""
Generated from symbols.json for ::java::data::enchantment::level_based_value::LinearLevelValue
Local link to file: vanilla_mcdoc/data/enchantment/level_based_value/LinearLevelValue.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel


class LinearLevelValue(GeneratedModel):
    base: float  # Base value at level 1.
    per_level_above_first: float  # Value increase per level above 1.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::level_based_value::LinearLevelValue": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Base value at level 1.",
                "key": "base",
                "type": {
                    "kind": "float"
                }
            },
            {
                "kind": "pair",
                "desc": "Value increase per level above 1.",
                "key": "per_level_above_first",
                "type": {
                    "kind": "float"
                }
            }
        ]
    }
}
