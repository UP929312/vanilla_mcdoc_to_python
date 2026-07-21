# Generated from symbols.json for ::java::data::advancement::AdvancementFrame
from enum import Enum


class AdvancementFrame(Enum):
    TASK = "task"  # Normal border.
    CHALLENGE = "challenge"  # Fancy spiked border (used for the kill all mobs advancement).
    GOAL = "goal"  # Rounded border (used for the full beacon advancement).


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::AdvancementFrame": {
        "kind": "enum",
        "enumKind": "string",
        "values": [
            {
                "desc": "Normal border.",
                "identifier": "Task",
                "value": "task"
            },
            {
                "desc": "Fancy spiked border (used for the kill all mobs advancement).",
                "identifier": "Challenge",
                "value": "challenge"
            },
            {
                "desc": "Rounded border (used for the full beacon advancement).",
                "identifier": "Goal",
                "value": "goal"
            }
        ]
    }
}

