"""
Generated from symbols.json for ::java::data::timeline::AttributeTrackBase
Local link to file: generated_symbols/data/timeline/AttributeTrackBase.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.timeline.EasingType import EasingType


class AttributeTrackBase(GeneratedModel):
    ease: EasingType | None = None  # Defaults to `linear`. For visualization, check out: https://easings.net/


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::timeline::AttributeTrackBase": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Defaults to `linear`.\nFor visualization, check out: https://easings.net/",
                "key": "ease",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::timeline::EasingType"
                },
                "optional": True
            }
        ]
    }
}
