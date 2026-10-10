"""
Generated from symbols.json for ::java::world::component::item::AttributeDisplayTextOverride
Local link to file: generated_symbols/world/component/item/AttributeDisplayTextOverride.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.util.text.Text import Text


class AttributeDisplayTextOverride(GeneratedModel):
    value: Text  # The text contents to show for this attribute modifer entry.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::item::AttributeDisplayTextOverride": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "The text contents to show for this attribute modifer entry.",
                "key": "value",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::text::Text"
                }
            }
        ]
    }
}
