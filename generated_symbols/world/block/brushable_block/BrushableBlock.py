# Generated from symbols.json for ::java::world::block::brushable_block::BrushableBlock
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.world.block.BlockEntity import BlockEntity

if TYPE_CHECKING:
    from generated_symbols.util.direction.DirectionInt import DirectionInt
    from generated_symbols.world.item.ItemStack import ItemStack


@dataclass(kw_only=True)
class BrushableBlock(BlockEntity):
    LootTable: str | None = None  # Loot table that will decide the brushed loot.
    LootTableSeed: int | None = None  # Seed of the loot table.
    item: ItemStack | None = None  # Item that was rolled from the loot table, which is currently peeking out.
    hit_direction: DirectionInt | None = None  # Direction of the block that was interacted with. Write-only, is not saved by the game.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::block::brushable_block::BrushableBlock": {
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
                "kind": "pair",
                "desc": "Loot table that will decide the brushed loot.",
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
            },
            {
                "kind": "pair",
                "desc": "Item that was rolled from the loot table, which is currently peeking out.",
                "key": "item",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::item::ItemStack"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Direction of the block that was interacted with.\nWrite-only, is not saved by the game.",
                "key": "hit_direction",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::direction::DirectionInt"
                },
                "optional": True
            }
        ]
    }
}

