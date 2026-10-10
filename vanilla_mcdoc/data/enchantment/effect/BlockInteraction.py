"""
Generated from symbols.json for ::java::data::enchantment::effect::BlockInteraction
Local link to file: vanilla_mcdoc/data/enchantment/effect/BlockInteraction.py
"""
# ~~~ CODE ~~~
from enum import StrEnum


class BlockInteraction(StrEnum):
    NONE = "none"  # No item drops or special behavior.
    BLOCK = "block"  # Drops items as if a block caused the explosion; `block_explosion_drop_decay` game rule applies.
    MOB = "mob"  # Drops items as if a mob caused the explosion; `mob_explosion_drop_decay` game rule applies.
    TNT = "tnt"  # Drops items as if TNT caused the explosion; `tnt_explosion_drop_decay` game rule applies.
    TRIGGER = "trigger"  # Triggers redstone-activated blocks.
