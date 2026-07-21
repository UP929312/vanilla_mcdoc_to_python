# Generated from symbols.json for ::java::data::timeline::AttributeTrackBase
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.timeline.EasingType import EasingType


@dataclass(kw_only=True)
class AttributeTrackBase:
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

