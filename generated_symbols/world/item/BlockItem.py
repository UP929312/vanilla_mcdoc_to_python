# Generated from symbols.json for ::java::world::item::BlockItem
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any
from generated_symbols.world.item.ItemBase import ItemBase

if TYPE_CHECKING:
    from generated_symbols.world.block.BlockEntityData import BlockEntityData


@dataclass(kw_only=True)
class BlockItem(ItemBase):
    BlockEntityTag: BlockEntityData | None = None
    BlockStateTag: Any | None = None  # Blockstate that the placed block will have.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::item::BlockItem": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::item::ItemBase"
                }
            },
            {
                "kind": "pair",
                "key": "BlockEntityTag",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::block::BlockEntityData"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Blockstate that the placed block will have.",
                "key": "BlockStateTag",
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "dynamic",
                            "accessor": [
                                {
                                    "keyword": "parent"
                                },
                                "id"
                            ]
                        }
                    ],
                    "registry": "mcdoc:block_item_states"
                },
                "optional": True
            }
        ]
    }
}

