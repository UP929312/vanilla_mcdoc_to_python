"""
Generated from symbols.json for ::java::data::enchantment::effect::AllOfLocationBasedEffect
Local link to file: generated_symbols/data/enchantment/effect/AllOfLocationBasedEffect.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.enchantment.effect.LocationBasedEffect import LocationBasedEffect


class AllOfLocationBasedEffect(GeneratedModel):
    effects: Annotated[list[LocationBasedEffect], Field(min_length=1)]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::effect::AllOfLocationBasedEffect": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "effects",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::data::enchantment::effect::LocationBasedEffect"
                    },
                    "lengthRange": {
                        "kind": 0,
                        "min": 1
                    }
                }
            }
        ]
    }
}
