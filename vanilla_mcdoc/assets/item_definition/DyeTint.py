"""
Generated from symbols.json for ::java::assets::item_definition::DyeTint
Local link to file: vanilla_mcdoc/assets/item_definition/DyeTint.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.assets.item_definition.ActuallyTranslucentRGB import ActuallyTranslucentRGB


class DyeTint(GeneratedModel):
    default: ActuallyTranslucentRGB  # Tint to apply when the `dyed_color` component is not present.
