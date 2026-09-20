"""
Generated from symbols.json for ::java::data::variants::MoonBrightnessCheck
Local link to file: generated_symbols/data/variants/MoonBrightnessCheck.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.util.MinMaxBounds import MinMaxBounds


class MoonBrightnessCheck(GeneratedModel):
    range: MinMaxBounds[float] | float  # Checks if the current moon brightness is within a certain range.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::variants::MoonBrightnessCheck": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Checks if the current moon brightness is within a certain range.",
                "key": "range",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::data::util::MinMaxBounds"
                    },
                    "typeArgs": [
                        {
                            "kind": "double"
                        }
                    ]
                }
            }
        ]
    }
}

