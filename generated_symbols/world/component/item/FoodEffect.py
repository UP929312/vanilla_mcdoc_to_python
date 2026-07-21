# Generated from symbols.json for ::java::world::component::item::FoodEffect
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.util.effect.MobEffectInstance import MobEffectInstance


@dataclass(kw_only=True)
class FoodEffect:
    effect: MobEffectInstance
    probability: Annotated[float, 'Range | `0`-`1` | both inclusive'] | None = None  # Chance for the effect to be applied. Defaults to 1.


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

