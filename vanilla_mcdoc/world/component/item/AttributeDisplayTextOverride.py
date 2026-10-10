"""
Generated from symbols.json for ::java::world::component::item::AttributeDisplayTextOverride
Local link to file: vanilla_mcdoc/world/component/item/AttributeDisplayTextOverride.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.util.text.Text import Text


class AttributeDisplayTextOverride(GeneratedModel):
    value: Text  # The text contents to show for this attribute modifer entry.
