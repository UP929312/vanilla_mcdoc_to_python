"""
Generated from symbols.json for ::java::world::component::item::BrewingFuel
Local link to file: generated_symbols/world/component/item/BrewingFuel.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.number_provider.ResolvableNumber import ResolvableNumber


@dataclass(kw_only=True)
class BrewingFuel:
    uses: ResolvableNumber
    speed_multiplier: ResolvableNumber


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::item::BrewingFuel": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "uses",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::number_provider::ResolvableNumber"
                }
            },
            {
                "kind": "pair",
                "key": "speed_multiplier",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::number_provider::ResolvableNumber"
                }
            }
        ]
    }
}

