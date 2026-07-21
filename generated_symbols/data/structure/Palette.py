# Generated from symbols.json for ::java::data::structure::Palette
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.util.block_state.BlockState import BlockState


@dataclass(kw_only=True)
class Palette:
    palette: list[BlockState]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::structure::Palette": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "palette",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::util::block_state::BlockState"
                    }
                }
            }
        ]
    }
}

