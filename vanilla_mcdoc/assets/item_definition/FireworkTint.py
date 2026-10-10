"""
Generated from symbols.json for ::java::assets::item_definition::FireworkTint
Local link to file: vanilla_mcdoc/assets/item_definition/FireworkTint.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.assets.item_definition.ActuallyTranslucentRGB import ActuallyTranslucentRGB


class FireworkTint(GeneratedModel):
    default: ActuallyTranslucentRGB  # Tint to apply when the `firework_explosion` component is not present.
