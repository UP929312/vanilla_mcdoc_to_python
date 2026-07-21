# Generated from symbols.json for ::java::world::component::item::KineticWeaponEffectCondition
from dataclasses import dataclass


@dataclass(kw_only=True)
class KineticWeaponEffectCondition:
    max_duration_ticks: int  # The duration in ticks this condition can pass. Starts counting after charged.
    min_speed: float | None = None  # The minimum attacker speed required. Defaults to 0.0
    min_relative_speed: float | None = None  # The minimum relative speed required. Defaults to 0.0


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::item::KineticWeaponEffectCondition": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "The duration in ticks this condition can pass.\nStarts counting after charged.",
                "key": "max_duration_ticks",
                "type": {
                    "kind": "int"
                }
            },
            {
                "kind": "pair",
                "desc": "The minimum attacker speed required.\nDefaults to 0.0",
                "key": "min_speed",
                "type": {
                    "kind": "float"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "The minimum relative speed required.\nDefaults to 0.0",
                "key": "min_relative_speed",
                "type": {
                    "kind": "float"
                },
                "optional": True
            }
        ]
    }
}

