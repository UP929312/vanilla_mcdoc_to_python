"""
Generated from symbols.json for ::java::assets::equipment::Dyeable
Local link to file: vanilla_mcdoc/assets/equipment/Dyeable.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.util.color.RGB import RGB


class Dyeable(GeneratedModel):
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
