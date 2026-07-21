# Generated from symbols.json for ::java::world::item::map::IdentifiedDecoration
from dataclasses import dataclass
from generated_symbols.world.item.map.Decoration import Decoration


@dataclass(kw_only=True)
class IdentifiedDecoration(Decoration):
    id: str  # An arbitrary unique string identifying the decoration.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::item::map::IdentifiedDecoration": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::item::map::Decoration"
                }
            },
            {
                "kind": "pair",
                "desc": "An arbitrary unique string identifying the decoration.",
                "key": "id",
                "type": {
                    "kind": "string"
                }
            }
        ]
    }
}

