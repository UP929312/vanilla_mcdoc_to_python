"""
Generated from symbols.json for ::java::data::timeline::TimeMarkerMap
Local link to file: generated_symbols/data/timeline/TimeMarkerMap.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.timeline.TimeMarker import TimeMarker


type TimeMarkerMap = dict[Annotated[str, IdSpec()], Annotated[int, 'Range | Min `0` and above | inclusive'] | TimeMarker]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::timeline::TimeMarkerMap": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Time marker ID must be unique within the world clock.",
                "key": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id"
                        }
                    ]
                },
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "int",
                            "valueRange": {
                                "kind": 0,
                                "min": 0
                            }
                        },
                        {
                            "kind": "reference",
                            "path": "::java::data::timeline::TimeMarker"
                        }
                    ]
                }
            }
        ]
    }
}

