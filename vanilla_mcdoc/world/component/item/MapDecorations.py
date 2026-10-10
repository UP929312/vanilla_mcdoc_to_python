"""
Generated from symbols.json for ::java::world::component::item::MapDecorations
Local link to file: vanilla_mcdoc/world/component/item/MapDecorations.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from vanilla_mcdoc.world.component.item.MapDecoration import MapDecoration


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
