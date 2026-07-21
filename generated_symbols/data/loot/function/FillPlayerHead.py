# Generated from symbols.json for ::java::data::loot::function::FillPlayerHead
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.data.loot.function.Conditions import Conditions

if TYPE_CHECKING:
    from generated_symbols.data.loot.EntityTarget import EntityTarget


@dataclass(kw_only=True)
class FillPlayerHead(Conditions):
    entity: EntityTarget  # `this` to use the entity that died or the player that gained the advancement, opened the container, or broke the block.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::function::FillPlayerHead": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "`this` to use the entity that died or the player that gained the advancement, opened the container, or broke the block.",
                "key": "entity",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::loot::EntityTarget"
                }
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::loot::function::Conditions"
                }
            }
        ]
    }
}

