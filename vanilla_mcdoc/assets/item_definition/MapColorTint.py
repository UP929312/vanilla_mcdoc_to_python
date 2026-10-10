"""
Generated from symbols.json for ::java::assets::item_definition::MapColorTint
Local link to file: generated_symbols/assets/item_definition/MapColorTint.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.util.color.RGB import RGB


class MapColorTint(GeneratedModel):
    default: RGB  # Tint to apply when the `map_color` component is not present.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::item_definition::MapColorTint": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Tint to apply when the `map_color` component is not present.",
                "key": "default",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::color::RGB"
                }
            }
        ]
    }
}
