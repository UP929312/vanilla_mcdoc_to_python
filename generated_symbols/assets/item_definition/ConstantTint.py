"""
Generated from symbols.json for ::java::assets::item_definition::ConstantTint
Local link to file: generated_symbols/assets/item_definition/ConstantTint.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.util.color.RGB import RGB


class ConstantTint(GeneratedModel):
    value: RGB  # Constant tint color to apply.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::item_definition::ConstantTint": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Constant tint color to apply.",
                "key": "value",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::color::RGB"
                }
            }
        ]
    }
}

