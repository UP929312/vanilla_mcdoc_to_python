"""
Generated from symbols.json for ::java::data::timeline::TimeMarkerMap
Local link to file: vanilla_mcdoc/data/timeline/TimeMarkerMap.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.timeline.TimeMarker import TimeMarker


type TimeMarkerMap = dict[Annotated[str, IdSpec()], Annotated[int, Field(ge=0)] | TimeMarker]
