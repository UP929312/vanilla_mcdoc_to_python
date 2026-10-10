"""
Generated from symbols.json for ::java::data::loot::EntityTarget
Local link to file: vanilla_mcdoc/data/loot/EntityTarget.py
"""
# ~~~ CODE ~~~
from enum import StrEnum


class EntityTarget(StrEnum):
    THIS = "this"
    ATTACKER = "attacker"
    DIRECTATTACKER = "direct_attacker"
    ATTACKINGPLAYER = "attacking_player"
    TARGETENTITY = "target_entity"
    INTERACTINGENTITY = "interacting_entity"
