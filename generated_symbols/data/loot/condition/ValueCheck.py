"""
Generated from symbols.json for ::java::data::loot::condition::ValueCheck
Local link to file: generated_symbols/data/loot/condition/ValueCheck.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.loot.IntRange import IntRange
    from generated_symbols.data.number_provider.LegacyNumberProvider import LegacyNumberProvider


class ValueCheck(GeneratedModel):
    value: LegacyNumberProvider  # Clamps to an integer.
    range: IntRange  # Passes when `value` is within this range.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::condition::ValueCheck": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Clamps to an integer.",
                "key": "value",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::number_provider::LegacyNumberProvider"
                }
            },
            {
                "kind": "pair",
                "desc": "Passes when `value` is within this range.",
                "key": "range",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::loot::IntRange"
                }
            }
        ]
    }
}

