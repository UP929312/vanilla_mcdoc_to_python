"""
Generated from symbols.json for ::java::world::block::enchanting_table::EnchantingTable
Local link to file: vanilla_mcdoc/world/block/enchanting_table/EnchantingTable.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.world.block.BlockEntity import BlockEntity
from vanilla_mcdoc.world.block.Nameable import Nameable


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
