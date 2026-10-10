"""
Generated from symbols.json for ::java::world::block::beehive::LegacyBee
Local link to file: vanilla_mcdoc/world/block/beehive/LegacyBee.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.world.entity.AnyEntity import AnyEntity


class LegacyBee(GeneratedModel):
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
