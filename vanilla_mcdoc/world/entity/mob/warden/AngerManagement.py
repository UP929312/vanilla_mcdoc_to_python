"""
Generated from symbols.json for ::java::world::entity::mob::warden::AngerManagement
Local link to file: vanilla_mcdoc/world/entity/mob/warden/AngerManagement.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.world.entity.mob.warden.Suspect import Suspect


class AngerManagement(GeneratedModel):
    suspects: list[Suspect] | None = None  # Suspects that have angered the warden.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::warden::AngerManagement": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Suspects that have angered the warden.",
                "key": "suspects",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::world::entity::mob::warden::Suspect"
                    }
                },
                "optional": True
            }
        ]
    }
}
