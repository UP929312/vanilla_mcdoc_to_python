"""
Generated from symbols.json for ::java::world::entity::mob::fish::Pufferfish
Local link to file: generated_symbols/world/entity/mob/fish/Pufferfish.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from pydantic import Field

from generated_symbols.world.entity.mob.fish.Fish import Fish

if TYPE_CHECKING:
    from generated_symbols.world.entity.mob.fish.PuffState import PuffState


class Pufferfish(Fish):
    PuffState_: PuffState | None = Field(default=None, alias='PuffState')  # How puffed it is.


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
