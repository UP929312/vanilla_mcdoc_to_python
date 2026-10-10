"""
Generated from symbols.json for ::java::assets::item_definition::PotionTint
Local link to file: vanilla_mcdoc/assets/item_definition/PotionTint.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.util.color.RGB import RGB


class PotionTint(GeneratedModel):
    default: RGB  # Tint to apply when the `potion_contents` component is not present, or it has no effects and no `custom_color` is set.
