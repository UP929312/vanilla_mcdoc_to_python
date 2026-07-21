# Generated from symbols.json for ::java::data::enchantment::level_based_value::SquaredLevelValue
from dataclasses import dataclass


@dataclass(kw_only=True)
class SquaredLevelValue:
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

