# Generated from symbols.json for ::java::world::component::item::MapDecorations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.world.component.item.MapDecoration import MapDecoration


type MapDecorations = dict[str, MapDecoration]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::item::MapDecorations": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": {
                    "kind": "string"
                },
                "type": {
                    "kind": "reference",
                    "path": "::java::world::component::item::MapDecoration"
                }
            }
        ]
    }
}

