"""
Generated from symbols.json for ::java::world::component::item::AttributeDisplayTextOverride
Local link to file: generated_symbols/world/component/item/AttributeDisplayTextOverride.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.util.text.Text import Text


@dataclass(kw_only=True)
class AttributeDisplayTextOverride:
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

