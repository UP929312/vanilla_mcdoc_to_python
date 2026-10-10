"""
Generated from symbols.json for ::java::world::entity::minecart::ContainerMinecart
Local link to file: vanilla_mcdoc/world/entity/minecart/ContainerMinecart.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec


class ContainerMinecart(GeneratedModel):
    LootTable: Annotated[str, IdSpec(registry='loot_table', empty='allowed')] | None = None  # Loot table that will populate this minecart.
    LootTableSeed: int | None = None  # Seed of the loot table.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::minecart::ContainerMinecart": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Loot table that will populate this minecart.",
                "key": "LootTable",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "tree",
                                "values": {
                                    "registry": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "loot_table"
                                        }
                                    },
                                    "empty": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "allowed"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Seed of the loot table.",
                "key": "LootTableSeed",
                "type": {
                    "kind": "long",
                    "attributes": [
                        {
                            "name": "random"
                        }
                    ]
                },
                "optional": True
            }
        ]
    }
}
