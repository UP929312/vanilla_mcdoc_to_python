# Generated from symbols.json for ::java::data::variants::MoonBrightnessCheck
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.util.MinMaxBounds import MinMaxBounds


@dataclass(kw_only=True)
class MoonBrightnessCheck:
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

