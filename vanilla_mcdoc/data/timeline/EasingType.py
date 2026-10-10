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
