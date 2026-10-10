"""
Generated from symbols.json for ::java::util::game_event::VibrationListener
Local link to file: vanilla_mcdoc/util/game_event/VibrationListener.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.util.game_event.PositionSource import PositionSource
    from vanilla_mcdoc.util.game_event.ReceivingEvent import ReceivingEvent


class VibrationListener(GeneratedModel):
    source: PositionSource
    range: Annotated[int, Field(ge=1)]  # Range in blocks where vibrations can be detected
    event: ReceivingEvent | None = None  # Event that is being received, if any
    event_distance: Annotated[float, Field(ge=0)] | None = None  # Distance in blocks to the event that is being received
    event_delay: Annotated[int, Field(ge=1)] | None = None  # Delay in ticks until the event reaches this listener
