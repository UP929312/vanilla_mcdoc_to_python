# Generated from symbols.json for ::java::world::entity::mob::ender_dragon::EnderDragon
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.world.entity.mob.MobBase import MobBase

if TYPE_CHECKING:
    from generated_symbols.world.entity.mob.ender_dragon.DragonPhase import DragonPhase


@dataclass(kw_only=True)
class EnderDragon(MobBase):
    DragonPhase: DragonPhase | None = None  # Fighting phase it is in.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::ender_dragon::EnderDragon": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::MobBase"
                }
            },
            {
                "kind": "pair",
                "desc": "Fighting phase it is in.",
                "key": "DragonPhase",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::ender_dragon::DragonPhase"
                },
                "optional": True
            }
        ]
    }
}

