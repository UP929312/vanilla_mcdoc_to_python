"""
Generated from symbols.json for ::java::data::timeline::EasingType
Local link to file: vanilla_mcdoc/data/timeline/EasingType.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from vanilla_mcdoc.data.timeline.CubicBezierEase import CubicBezierEase
    from vanilla_mcdoc.data.timeline.SimpleEasingType import SimpleEasingType


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
