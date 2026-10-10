"""
Generated from symbols.json for ::java::data::util::NbtProviderSource
Local link to file: vanilla_mcdoc/data/util/NbtProviderSource.py
"""
# ~~~ CODE ~~~
from enum import StrEnum


class NbtProviderSource(StrEnum):
    THIS = "this"
    ATTACKER = "attacker"
    DIRECTATTACKER = "direct_attacker"
    ATTACKINGPLAYER = "attacking_player"
    BLOCKENTITY = "block_entity"
