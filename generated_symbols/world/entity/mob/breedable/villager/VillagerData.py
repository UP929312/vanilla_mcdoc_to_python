"""
Generated from symbols.json for ::java::world::entity::mob::breedable::villager::VillagerData
Local link to file: generated_symbols/world/entity/mob/breedable/villager/VillagerData.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Annotated

from minecraft_registry import IdSpec


@dataclass(kw_only=True)
class VillagerData:
    level: int | None = None  # Used for trading and badge rendering.
    profession: Annotated[str, IdSpec(registry='villager_profession')] | None = None
    type: Annotated[str, IdSpec(registry='villager_type')] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::breedable::villager::VillagerData": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Used for trading and badge rendering.",
                "key": "level",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "profession",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "villager_profession"
                                }
                            }
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "type",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "villager_type"
                                }
                            }
                        }
                    ]
                },
                "optional": True
            }
        ]
    }
}

