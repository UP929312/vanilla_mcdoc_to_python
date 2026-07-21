# Generated from symbols.json for ::java::assets::equipment::Dyeable
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.util.color.RGB import RGB


@dataclass(kw_only=True)
class Dyeable:
    color_when_undyed: RGB | None = None  # If the item is not dyed, this color is used instead.  If not specified and the item is not dyed, this layer will be hidden.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::equipment::Dyeable": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "If the item is not dyed, this color is used instead. \\\nIf not specified and the item is not dyed, this layer will be hidden.",
                "key": "color_when_undyed",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::color::RGB"
                },
                "optional": True
            }
        ]
    }
}

