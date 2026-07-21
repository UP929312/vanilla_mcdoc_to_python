# Generated from symbols.json for ::java::assets::item_definition::CompassTarget
from enum import Enum


class CompassTarget(Enum):
    NONE = "none"  # Always an invalid target.
    SPAWN = "spawn"  # Points at world spawn.
    LODESTONE = "lodestone"  # Points at the location stored in the `lodestone_tracker` component.
    RECOVERY = "recovery"  # Points at the last player death location.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::item_definition::CompassTarget": {
        "kind": "enum",
        "enumKind": "string",
        "values": [
            {
                "desc": "Always an invalid target.",
                "identifier": "None",
                "value": "none"
            },
            {
                "desc": "Points at world spawn.",
                "identifier": "Spawn",
                "value": "spawn"
            },
            {
                "desc": "Points at the location stored in the `lodestone_tracker` component.",
                "identifier": "Lodestone",
                "value": "lodestone"
            },
            {
                "desc": "Points at the last player death location.",
                "identifier": "Recovery",
                "value": "recovery"
            }
        ]
    }
}

