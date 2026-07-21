# Generated from symbols.json for ::java::world::component::item::KineticWeapon
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.data.util.SoundEventRef import SoundEventRef
    from generated_symbols.world.component.item.KineticWeaponEffectCondition import KineticWeaponEffectCondition


@dataclass(kw_only=True)
class KineticWeapon:
    delay_ticks: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # The time in ticks required for charging. Defaults to 0
    contact_cooldown_ticks: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # The cooldown in ticks after hitting, and loosing contact with an entity before being able to hit it again Defaults to 10
    dismount_conditions: KineticWeaponEffectCondition | None = None
    knockback_conditions: KineticWeaponEffectCondition | None = None
    damage_conditions: KineticWeaponEffectCondition | None = None
    forward_movement: float | None = None  # The distance the item moves out of hand during animation. Defaults to 0.0
    damage_multiplier: float | None = None  # The multiplier for the final damage from the relative speed. Defaults to 1.0
    sound: SoundEventRef | None = None  # Sound to play when the weapon is engaged.
    hit_sound: SoundEventRef | None = None  # Sound to play when the weapon hits an entity.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::item::KineticWeapon": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "The time in ticks required for charging.\nDefaults to 0",
                "key": "delay_ticks",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "The cooldown in ticks after hitting, and loosing contact with an entity before being able to hit it again\nDefaults to 10",
                "key": "contact_cooldown_ticks",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "dismount_conditions",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::component::item::KineticWeaponEffectCondition"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "knockback_conditions",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::component::item::KineticWeaponEffectCondition"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "damage_conditions",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::component::item::KineticWeaponEffectCondition"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "The distance the item moves out of hand during animation.\nDefaults to 0.0",
                "key": "forward_movement",
                "type": {
                    "kind": "float"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "The multiplier for the final damage from the relative speed.\nDefaults to 1.0",
                "key": "damage_multiplier",
                "type": {
                    "kind": "float"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Sound to play when the weapon is engaged.",
                "key": "sound",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::util::SoundEventRef"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Sound to play when the weapon hits an entity.",
                "key": "hit_sound",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::util::SoundEventRef"
                },
                "optional": True
            }
        ]
    }
}

