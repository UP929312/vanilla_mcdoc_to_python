# Generated from symbols.json for ::java::world::block::beehive::LegacyBee
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.world.entity.AnyEntity import AnyEntity


@dataclass(kw_only=True)
class LegacyBee:
    MinOccupationTicks: int | None = None
    TicksInHive: int | None = None
    EntityData: AnyEntity | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::block::beehive::LegacyBee": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "MinOccupationTicks",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "TicksInHive",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "EntityData",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::AnyEntity"
                },
                "optional": True
            }
        ]
    }
}

