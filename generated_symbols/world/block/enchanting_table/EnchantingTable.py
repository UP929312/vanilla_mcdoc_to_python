"""
Generated from symbols.json for ::java::world::block::enchanting_table::EnchantingTable
Local link to file: generated_symbols/world/block/enchanting_table/EnchantingTable.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass

from generated_symbols.world.block.BlockEntity import BlockEntity
from generated_symbols.world.block.Nameable import Nameable


@dataclass(kw_only=True)
class EnchantingTable(BlockEntity, Nameable):
    pass


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::block::enchanting_table::EnchantingTable": {
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
            }
        ]
    }
}

