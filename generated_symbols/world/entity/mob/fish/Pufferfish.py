# Generated from symbols.json for ::java::world::entity::mob::fish::Pufferfish
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.world.entity.mob.fish.Fish import Fish

if TYPE_CHECKING:
    from generated_symbols.world.entity.mob.fish.PuffState import PuffState


@dataclass(kw_only=True)
class Pufferfish(Fish):
    PuffState: PuffState | None = None  # How puffed it is.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::fish::Pufferfish": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::fish::Fish"
                }
            },
            {
                "kind": "pair",
                "desc": "How puffed it is.",
                "key": "PuffState",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::fish::PuffState"
                },
                "optional": True
            }
        ]
    }
}

