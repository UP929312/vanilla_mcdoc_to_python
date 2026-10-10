"""
Generated from symbols.json for ::java::data::timeline::AttributeTrackBase
Local link to file: vanilla_mcdoc/data/timeline/AttributeTrackBase.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.timeline.EasingType import EasingType


class AttributeTrackBase(GeneratedModel):
    ease: EasingType | None = None  # Defaults to `linear`. For visualization, check out: https://easings.net/
