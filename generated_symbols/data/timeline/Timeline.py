"""
Generated from symbols.json for ::java::data::timeline::Timeline
Local link to file: generated_symbols/data/timeline/Timeline.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar

from pydantic import Field

from generated_symbols.base import GeneratedModel
from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.timeline.EnvironmentAttributeTrackMap import EnvironmentAttributeTrackMap
    from generated_symbols.data.timeline.TimeMarkerMap import TimeMarkerMap


class Timeline(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'timeline'

    period_ticks: Annotated[int, Field(ge=1)] | None = None  # When not present, the timeline will not repeat.
    clock: Annotated[str, IdSpec(registry='world_clock')]  # The world clock this timeline is tied to.
    time_markers: TimeMarkerMap | None = None
    tracks: EnvironmentAttributeTrackMap | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::timeline::Timeline": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "When not present, the timeline will not repeat.",
                "key": "period_ticks",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 1
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.1"
                            }
                        }
                    }
                ],
                "desc": "The world clock this timeline is tied to.",
                "key": "clock",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "world_clock"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.1"
                            }
                        }
                    }
                ],
                "key": "time_markers",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::timeline::TimeMarkerMap"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "tracks",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::timeline::EnvironmentAttributeTrackMap"
                },
                "optional": True
            }
        ]
    }
}

