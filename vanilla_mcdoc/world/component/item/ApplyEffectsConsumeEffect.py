"""
Generated from symbols.json for ::java::world::component::item::ApplyEffectsConsumeEffect
Local link to file: vanilla_mcdoc/world/component/item/ApplyEffectsConsumeEffect.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.util.effect.MobEffectInstance import MobEffectInstance


class ApplyEffectsConsumeEffect(GeneratedModel):
    effects: list[MobEffectInstance]
    probability: Annotated[float, Field(ge=0, le=1)] | None = None  # Chance the effects will be applied once consumed.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::item::ApplyEffectsConsumeEffect": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "effects",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::util::effect::MobEffectInstance"
                    }
                }
            },
            {
                "kind": "pair",
                "desc": "Chance the effects will be applied once consumed.",
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
