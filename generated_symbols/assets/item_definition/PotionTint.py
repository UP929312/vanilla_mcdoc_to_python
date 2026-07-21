# Generated from symbols.json for ::java::assets::item_definition::PotionTint
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.util.color.RGB import RGB


@dataclass(kw_only=True)
class PotionTint:
    default: RGB  # Tint to apply when the `potion_contents` component is not present, or it has no effects and no `custom_color` is set.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::item_definition::PotionTint": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Tint to apply when the `potion_contents` component is not present, or it has no effects and no `custom_color` is set.",
                "key": "default",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::color::RGB"
                }
            }
        ]
    }
}

