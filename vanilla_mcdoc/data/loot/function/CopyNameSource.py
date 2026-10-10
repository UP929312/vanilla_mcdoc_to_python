"""
Generated from symbols.json for ::java::data::loot::function::CopyNameSource
Local link to file: vanilla_mcdoc/data/loot/function/CopyNameSource.py
"""
# ~~~ CODE ~~~
from enum import StrEnum


class CopyNameSource(StrEnum):
    THIS = "this"
    ATTACKINGENTITY = "attacking_entity"
    LASTDAMAGEPLAYER = "last_damage_player"
    BLOCKENTITY = "block_entity"
