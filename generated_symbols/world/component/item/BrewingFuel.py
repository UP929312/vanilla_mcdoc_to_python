"""
Generated from symbols.json for ::java::world::component::item::BrewingFuel
Local link to file: generated_symbols/world/component/item/BrewingFuel.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.number_provider.ResolvableNumber import ResolvableNumber


class BrewingFuel(GeneratedModel):
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

