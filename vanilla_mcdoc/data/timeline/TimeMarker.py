"""
Generated from symbols.json for ::java::data::timeline::TimeMarker
Local link to file: vanilla_mcdoc/data/timeline/TimeMarker.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel


class TimeMarker(GeneratedModel):
    ticks: Annotated[int, Field(ge=0)]
    show_in_commands: bool | None = None  # Whether the time marker shows up in command suggestions.  The time marker is still available in commands even if it is not suggested.  Defaults to `false`.
