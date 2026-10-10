"""
Generated from symbols.json for ::java::world::component::item::Rarity
Local link to file: vanilla_mcdoc/world/component/item/Rarity.py
"""
# ~~~ CODE ~~~
from enum import StrEnum


class Rarity(StrEnum):
    COMMON = "common"  # White name, or aqua when enchanted.
    UNCOMMON = "uncommon"  # Yellow name, or aqua when enchanted.
    RARE = "rare"  # Aqua name, or light purple when enchanted.
    EPIC = "epic"  # Light purple name.
