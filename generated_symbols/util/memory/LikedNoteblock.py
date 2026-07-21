# Generated from symbols.json for ::java::util::memory::LikedNoteblock
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.util.memory.ExpirableValue import ExpirableValue

if TYPE_CHECKING:
    from generated_symbols.util.GlobalPos import GlobalPos


@dataclass(kw_only=True)
class LikedNoteblock(ExpirableValue):
    value: GlobalPos  # The position and dimension of the note block that the allay likes.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::memory::LikedNoteblock": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::memory::ExpirableValue"
                }
            },
            {
                "kind": "pair",
                "desc": "The position and dimension of the note block that the allay likes.",
                "key": "value",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::GlobalPos"
                }
            }
        ]
    }
}

