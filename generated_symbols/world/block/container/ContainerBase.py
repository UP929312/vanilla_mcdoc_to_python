"""
Generated from symbols.json for ::java::world::block::container::ContainerBase
Local link to file: generated_symbols/world/block/container/ContainerBase.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Annotated

from generated_symbols.world.block.BlockEntity import BlockEntity
from generated_symbols.world.block.Lockable import Lockable
from generated_symbols.world.block.Nameable import Nameable
from runtime_metadata import IdSpec


@dataclass(kw_only=True)
class ContainerBase(BlockEntity, Nameable, Lockable):
    LootTable: Annotated[str, IdSpec(registry='loot_table', empty='allowed')] | None = None  # Loot table that will populate this container.
    LootTableSeed: int | None = None  # Seed of the loot table.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::block::container::ContainerBase": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::block::BlockEntity"
                }
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::block::Nameable"
                }
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::block::Lockable"
                }
            },
            {
                "kind": "pair",
                "desc": "Loot table that will populate this container.",
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

