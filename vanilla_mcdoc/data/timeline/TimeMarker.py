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
