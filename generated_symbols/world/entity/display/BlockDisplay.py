# Generated from symbols.json for ::java::world::entity::display::BlockDisplay
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.world.entity.display.DisplayBase import DisplayBase

if TYPE_CHECKING:
    from generated_symbols.util.block_state.BlockState import BlockState


@dataclass(kw_only=True)
class BlockDisplay(DisplayBase):
    block_state: BlockState | None = None  # Block state to display. Can display most block entities (eg. Chests, Beds, Furnaces, etc).  Does not display specially rendered block entities (eg. The bell in a bell block, an end gateway, the book on an enchantment table, a banner, a sign, etc).


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::display::BlockDisplay": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::display::DisplayBase"
                }
            },
            {
                "kind": "pair",
                "desc": "Block state to display. Can display most block entities (eg. Chests, Beds, Furnaces, etc).\n\nDoes not display specially rendered block entities (eg. The bell in a bell block, an end gateway, the book on an enchantment table, a banner, a sign, etc).",
                "key": "block_state",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::block_state::BlockState"
                },
                "optional": True
            }
        ]
    }
}

