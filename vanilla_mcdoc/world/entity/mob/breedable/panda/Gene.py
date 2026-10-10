"""
Generated from symbols.json for ::java::world::entity::mob::breedable::panda::Gene
Local link to file: vanilla_mcdoc/world/entity/mob/breedable/panda/Gene.py
"""
# ~~~ CODE ~~~
from enum import StrEnum


class Gene(StrEnum):
    NORMAL = "normal"  # (dominant)
    LAZY = "lazy"  # (dominant)
    WORRIED = "worried"  # (dominant)
    PLAYFUL = "playful"  # (dominant)
    BROWN = "brown"  # (recessive)
    WEAK = "weak"  # (recessive)
    AGGRESSIVE = "aggressive"  # (dominant)
