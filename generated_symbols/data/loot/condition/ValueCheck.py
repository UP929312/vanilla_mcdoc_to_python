# Generated from symbols.json for ::java::data::loot::condition::ValueCheck
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.number_provider.NumberProviderRef import NumberProviderRef
    from generated_symbols.data.util.IntRange import IntRange


@dataclass(kw_only=True)
class ValueCheck:
    value: NumberProviderRef  # Clamps to an integer.
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
                    "path": "::java::data::number_provider::NumberProviderRef"
                }
            },
            {
                "kind": "pair",
                "desc": "Passes when `value` is within this range.",
                "key": "range",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::util::IntRange"
                }
            }
        ]
    }
}

