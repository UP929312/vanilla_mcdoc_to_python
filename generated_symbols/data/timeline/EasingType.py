# Generated from symbols.json for ::java::data::timeline::EasingType
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.timeline.CubicBezierEase import CubicBezierEase
    from generated_symbols.data.timeline.SimpleEasingType import SimpleEasingType


type EasingType = SimpleEasingType | CubicBezierEase


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::timeline::EasingType": {
        "kind": "union",
        "members": [
            {
                "kind": "reference",
                "path": "::java::data::timeline::SimpleEasingType"
            },
            {
                "kind": "reference",
                "path": "::java::data::timeline::CubicBezierEase"
            }
        ]
    }
}

