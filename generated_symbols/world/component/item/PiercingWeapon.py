# Generated from symbols.json for ::java::world::component::item::PiercingWeapon
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.util.SoundEventRef import SoundEventRef


@dataclass(kw_only=True)
class PiercingWeapon:
    deals_knockback: bool | None = None  # Whether the attack deals knockback. Defaults to `true`.
    dismounts: bool | None = None  # Whether the attack dismounts the target. Defaults to `false`.
    sound: SoundEventRef | None = None  # Sound to play when using the weapon to attack.
    hit_sound: SoundEventRef | None = None  # Sound to play when the weapon hits an entity.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::item::PiercingWeapon": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Whether the attack deals knockback.\nDefaults to `True`.",
                "key": "deals_knockback",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether the attack dismounts the target.\nDefaults to `False`.",
                "key": "dismounts",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Sound to play when using the weapon to attack.",
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

