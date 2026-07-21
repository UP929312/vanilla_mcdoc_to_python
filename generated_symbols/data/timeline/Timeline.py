# Generated from symbols.json for ::java::data::timeline::Timeline
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.data.timeline.EnvironmentAttributeTrackMap import EnvironmentAttributeTrackMap
    from generated_symbols.data.timeline.TimeMarkerMap import TimeMarkerMap


@dataclass(kw_only=True)
class Timeline:
    clock: str  # The world clock this timeline is tied to.
    period_ticks: Annotated[int, 'Range | Min `1` and above | inclusive'] | None = None  # When not present, the timeline will not repeat.
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

