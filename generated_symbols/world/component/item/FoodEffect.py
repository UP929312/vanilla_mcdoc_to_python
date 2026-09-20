"""
Generated from symbols.json for ::java::world::component::item::FoodEffect
Local link to file: generated_symbols/world/component/item/FoodEffect.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from generated_symbols.base import GeneratedModel
from pydantic import Field

if TYPE_CHECKING:
    from generated_symbols.util.effect.MobEffectInstance import MobEffectInstance


class FoodEffect(GeneratedModel):
    effect: MobEffectInstance
    probability: Annotated[float, Field(ge=0, le=1)] | None = None  # Chance for the effect to be applied. Defaults to 1.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::item::FoodEffect": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "effect",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::effect::MobEffectInstance"
                }
            },
            {
                "kind": "pair",
                "desc": "Chance for the effect to be applied. Defaults to 1.",
                "key": "probability",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 1
                    }
                },
                "optional": True
            }
        ]
    }
}

