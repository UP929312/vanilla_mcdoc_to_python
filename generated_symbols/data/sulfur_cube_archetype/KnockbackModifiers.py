# Generated from symbols.json for ::java::data::sulfur_cube_archetype::KnockbackModifiers
from dataclasses import dataclass


@dataclass(kw_only=True)
class KnockbackModifiers:
    horizontal_power: float  # The horizontal power of the knockback.
    vertical_power: float  # The vertical power of the knockback.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::sulfur_cube_archetype::KnockbackModifiers": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "The horizontal power of the knockback.",
                "key": "horizontal_power",
                "type": {
                    "kind": "float"
                }
            },
            {
                "kind": "pair",
                "desc": "The vertical power of the knockback.",
                "key": "vertical_power",
                "type": {
                    "kind": "float"
                }
            }
        ]
    }
}

