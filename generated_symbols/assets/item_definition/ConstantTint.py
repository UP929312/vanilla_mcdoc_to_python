# Generated from symbols.json for ::java::assets::item_definition::ConstantTint
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.util.color.RGB import RGB


@dataclass(kw_only=True)
class ConstantTint:
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

