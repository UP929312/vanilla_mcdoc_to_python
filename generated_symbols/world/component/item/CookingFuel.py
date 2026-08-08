# Generated from symbols.json for ::java::world::component::item::CookingFuel
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.number_provider.ResolvableNumber import ResolvableNumber


@dataclass(kw_only=True)
class CookingFuel:
    burn_time: ResolvableNumber
    speed_multiplier: ResolvableNumber


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::item::CookingFuel": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "burn_time",
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

