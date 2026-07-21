# Generated from symbols.json for ::java::data::timeline::TimeMarker
from dataclasses import dataclass
from typing import Annotated


@dataclass(kw_only=True)
class TimeMarker:
    ticks: Annotated[int, 'Range | Min `0` and above | inclusive']
    show_in_commands: bool | None = None  # Whether the time marker shows up in command suggestions.  The time marker is still available in commands even if it is not suggested.  Defaults to `false`.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::timeline::TimeMarker": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "ticks",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0
                    }
                }
            },
            {
                "kind": "pair",
                "desc": "Whether the time marker shows up in command suggestions. \\\nThe time marker is still available in commands even if it is not suggested. \\\nDefaults to `False`.",
                "key": "show_in_commands",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}

