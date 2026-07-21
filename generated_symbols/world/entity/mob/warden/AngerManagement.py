# Generated from symbols.json for ::java::world::entity::mob::warden::AngerManagement
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.world.entity.mob.warden.Suspect import Suspect


@dataclass(kw_only=True)
class AngerManagement:
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

