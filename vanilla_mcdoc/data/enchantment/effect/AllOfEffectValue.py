"""
Generated from symbols.json for ::java::data::enchantment::effect::AllOfEffectValue
Local link to file: generated_symbols/data/enchantment/effect/AllOfEffectValue.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.enchantment.effect.ValueEffect import ValueEffect


class AllOfEffectValue(GeneratedModel):
    effects: Annotated[list[ValueEffect], Field(min_length=1)]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::effect::AllOfEffectValue": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "effects",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::data::enchantment::effect::ValueEffect"
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
