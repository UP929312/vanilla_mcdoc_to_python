"""
Generated from symbols.json for ::java::data::timeline::Timeline
Local link to file: vanilla_mcdoc/data/timeline/Timeline.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.timeline.EnvironmentAttributeTrackMap import EnvironmentAttributeTrackMap
    from vanilla_mcdoc.data.timeline.TimeMarkerMap import TimeMarkerMap


class Timeline(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'timeline'

    period_ticks: Annotated[int, Field(ge=1)] | None = None  # When not present, the timeline will not repeat.
    clock: Annotated[str, IdSpec(registry='world_clock')]  # The world clock this timeline is tied to.
    time_markers: TimeMarkerMap | None = None
    tracks: EnvironmentAttributeTrackMap | None = None
