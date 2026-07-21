# Generated from symbols.json for ::java::world::block::beehive::Bee
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.world.entity.AnyEntity import AnyEntity


@dataclass(kw_only=True)
class Bee:
    min_ticks_in_hive: int
    ticks_in_hive: int
    entity_data: AnyEntity


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::block::beehive::Bee": {
        "kind": "struct",
        "fields": [
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
            },
            {
                "kind": "pair",
                "key": "entity_data",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::AnyEntity"
                }
            }
        ]
    }
}

