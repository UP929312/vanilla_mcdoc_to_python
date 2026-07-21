# Generated from symbols.json for ::java::data::timeline::TimeMarkerMap
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.data.timeline.TimeMarker import TimeMarker


type TimeMarkerMap = dict[str, Annotated[int, 'Range | Min `0` and above | inclusive'] | TimeMarker]


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

