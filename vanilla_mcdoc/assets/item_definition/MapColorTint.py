"""
Generated from symbols.json for ::java::assets::item_definition::MapColorTint
Local link to file: vanilla_mcdoc/assets/item_definition/MapColorTint.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.util.color.RGB import RGB


class MapColorTint(GeneratedModel):
    default: RGB  # Tint to apply when the `map_color` component is not present.
