"""
Generated from symbols.json for ::java::world::entity::mob::Brain
Local link to file: vanilla_mcdoc/world/entity/mob/Brain.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.util.memory.Memories import Memories


class Brain(GeneratedModel):
    memories: Memories | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::Brain": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "memories",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::memory::Memories"
                },
                "optional": True
            }
        ]
    }
}
