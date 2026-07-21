# Generated from symbols.json for ::java::world::component::block::Occupant
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.world.entity.AnyEntity import AnyEntity


@dataclass(kw_only=True)
class Occupant:
    entity_data: AnyEntity
    min_ticks_in_hive: int
    ticks_in_hive: int


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::block::Occupant": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "entity_data",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::AnyEntity"
                }
            },
            {
                "kind": "pair",
                "key": "min_ticks_in_hive",
                "type": {
                    "kind": "int"
                }
            },
            {
                "kind": "pair",
                "key": "ticks_in_hive",
                "type": {
                    "kind": "int"
                }
            }
        ]
    }
}

