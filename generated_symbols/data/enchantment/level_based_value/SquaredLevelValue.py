"""
Generated from symbols.json for ::java::data::enchantment::level_based_value::SquaredLevelValue
Local link to file: generated_symbols/data/enchantment/level_based_value/SquaredLevelValue.py
"""
# ~~~ CODE ~~~
from generated_symbols.base import GeneratedModel


class SquaredLevelValue(GeneratedModel):
    added: float  # Added to the result so that the result becomes `square(level) + added`.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::level_based_value::SquaredLevelValue": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Added to the result so that the result becomes `square(level) + added`.",
                "key": "added",
                "type": {
                    "kind": "float"
                }
            }
        ]
    }
}

