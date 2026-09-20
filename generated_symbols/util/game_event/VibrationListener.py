"""
Generated from symbols.json for ::java::util::game_event::VibrationListener
Local link to file: generated_symbols/util/game_event/VibrationListener.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from generated_symbols.base import GeneratedModel
from pydantic import Field

if TYPE_CHECKING:
    from generated_symbols.util.game_event.PositionSource import PositionSource
    from generated_symbols.util.game_event.ReceivingEvent import ReceivingEvent


class VibrationListener(GeneratedModel):
    source: PositionSource
    range: Annotated[int, Field(ge=1)]  # Range in blocks where vibrations can be detected
    event: ReceivingEvent | None = None  # Event that is being received, if any
    event_distance: Annotated[float, Field(ge=0)] | None = None  # Distance in blocks to the event that is being received
    event_delay: Annotated[int, Field(ge=1)] | None = None  # Delay in ticks until the event reaches this listener


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::game_event::VibrationListener": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "source",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::game_event::PositionSource"
                }
            },
            {
                "kind": "pair",
                "desc": "Range in blocks where vibrations can be detected",
                "key": "range",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 1
                    }
                }
            },
            {
                "kind": "pair",
                "desc": "Event that is being received, if any",
                "key": "event",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::game_event::ReceivingEvent"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Distance in blocks to the event that is being received",
                "key": "event_distance",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Delay in ticks until the event reaches this listener",
                "key": "event_delay",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 1
                    }
                },
                "optional": True
            }
        ]
    }
}

