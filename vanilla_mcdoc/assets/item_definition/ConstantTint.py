"""
Generated from symbols.json for ::java::assets::item_definition::ConstantTint
Local link to file: vanilla_mcdoc/assets/item_definition/ConstantTint.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.util.color.RGB import RGB


class ConstantTint(GeneratedModel):
    value: RGB  # Constant tint color to apply.
