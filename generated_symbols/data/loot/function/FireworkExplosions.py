# Generated from symbols.json for ::java::data::loot::function::FireworkExplosions
from dataclasses import dataclass
from typing import TYPE_CHECKING

from generated_symbols.data.loot.function.ListOperation import ListOperation

if TYPE_CHECKING:
    from generated_symbols.world.component.item.Explosion import Explosion


@dataclass(kw_only=True)
class FireworkExplosions(ListOperation):
    values: list[Explosion]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::function::FireworkExplosions": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "values",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "dispatcher",
                        "parallelIndices": [
                            {
                                "kind": "static",
                                "value": "firework_explosion"
                            }
                        ],
                        "registry": "minecraft:data_component"
                    }
                }
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::loot::function::ListOperation"
                }
            }
        ]
    }
}

