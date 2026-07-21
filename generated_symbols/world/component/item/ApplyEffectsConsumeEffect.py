# Generated from symbols.json for ::java::world::component::item::ApplyEffectsConsumeEffect
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.util.effect.MobEffectInstance import MobEffectInstance


@dataclass(kw_only=True)
class ApplyEffectsConsumeEffect:
    effects: list[MobEffectInstance]
    probability: Annotated[float, 'Range | `0`-`1` | both inclusive'] | None = None  # Chance the effects will be applied once consumed.


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

