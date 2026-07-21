# Generated from symbols.json for ::java::assets::item_definition::MapColorTint
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.util.color.RGB import RGB


@dataclass(kw_only=True)
class MapColorTint:
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

