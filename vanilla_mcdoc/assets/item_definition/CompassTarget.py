"""
Generated from symbols.json for ::java::assets::item_definition::CompassTarget
Local link to file: vanilla_mcdoc/assets/item_definition/CompassTarget.py
"""
# ~~~ CODE ~~~
from enum import StrEnum


class CompassTarget(StrEnum):
    NONE = "none"  # Always an invalid target.
    SPAWN = "spawn"  # Points at world spawn.
    LODESTONE = "lodestone"  # Points at the location stored in the `lodestone_tracker` component.
    RECOVERY = "recovery"  # Points at the last player death location.
