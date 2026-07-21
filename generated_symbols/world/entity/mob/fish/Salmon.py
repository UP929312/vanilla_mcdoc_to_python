# Generated from symbols.json for ::java::world::entity::mob::fish::Salmon
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.world.entity.mob.fish.Fish import Fish

if TYPE_CHECKING:
    from generated_symbols.world.component.entity.SalmonType import SalmonType


@dataclass(kw_only=True)
class Salmon(Fish):
    type: SalmonType | None = None  # The size variant of the salmon.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::fish::Salmon": {
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
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.2"
                            }
                        }
                    }
                ],
                "desc": "The size variant of the salmon.",
                "key": "type",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::component::entity::SalmonType"
                },
                "optional": True
            }
        ]
    }
}

