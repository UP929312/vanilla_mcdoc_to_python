# Generated from symbols.json for ::java::world::entity::mob::Brain
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.util.memory.Memories import Memories


@dataclass(kw_only=True)
class Brain:
    memories: Memories | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::Brain": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "memories",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::memory::Memories"
                },
                "optional": True
            }
        ]
    }
}

