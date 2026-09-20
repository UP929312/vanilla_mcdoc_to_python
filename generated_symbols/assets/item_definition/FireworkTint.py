"""
Generated from symbols.json for ::java::assets::item_definition::FireworkTint
Local link to file: generated_symbols/assets/item_definition/FireworkTint.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.assets.item_definition.ActuallyTranslucentRGB import ActuallyTranslucentRGB


class FireworkTint(GeneratedModel):
    default: ActuallyTranslucentRGB  # Tint to apply when the `firework_explosion` component is not present.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::item_definition::FireworkTint": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Tint to apply when the `firework_explosion` component is not present.",
                "key": "default",
                "type": {
                    "kind": "reference",
                    "path": "::java::assets::item_definition::ActuallyTranslucentRGB"
                }
            }
        ]
    }
}

