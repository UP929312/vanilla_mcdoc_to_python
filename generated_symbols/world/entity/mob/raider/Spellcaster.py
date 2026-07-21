# Generated from symbols.json for ::java::world::entity::mob::raider::Spellcaster
from dataclasses import dataclass
from generated_symbols.world.entity.mob.raider.RaiderBase import RaiderBase


@dataclass(kw_only=True)
class Spellcaster(RaiderBase):
    SpellTicks: int | None = None  # Ticks until the raider can cast its spell.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::raider::Spellcaster": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::raider::RaiderBase"
                }
            },
            {
                "kind": "pair",
                "desc": "Ticks until the raider can cast its spell.",
                "key": "SpellTicks",
                "type": {
                    "kind": "int"
                },
                "optional": True
            }
        ]
    }
}

