# ~~~ WHAT ARE WE TESTING ~~~

# Shows one of the pairs owning their own struct

# ~~~ FILE CONTENT ~~~
"""
Generated from symbols.json for ::java::world::entity::mob::MobBase
Local link to file: generated_symbols/world/entity/mob/MobBase.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

from generated_symbols.world.entity.mob.LivingEntity import LivingEntity
from runtime_metadata import IdSpec

if TYPE_CHECKING:
    from generated_symbols.world.entity.mob.DropChances import DropChances
    from generated_symbols.world.entity.mob.EntityEquipment import EntityEquipment


@dataclass(kw_only=True)
class LeashStruct:
    UUID: tuple[int, int, int, int] | None = None


@dataclass(kw_only=True)
class MobBase(LivingEntity):
    equipment: EntityEquipment | None = None  # The equipment items of the mob, such as armor or weapons.
    drop_chances: DropChances | None = None  # Chances of the mob dropping an equipment slot on death.
    DeathLootTable: Annotated[str, IdSpec(registry='loot_table', empty='allowed')] | None = None  # Loot table that is dropped when the mob dies.
    DeathLootTableSeed: int | None = None  # Seed for generating the death loot table.
    CanPickUpLoot: bool | None = None  # Whether it can pick up loot.
    PersistenceRequired: bool | None = None  # Whether it should not despawn naturally.
    LeftHanded: bool | None = None  # Whether it is left handed.
    NoAI: bool | None = None  # Whether it should have an AI.
    leash: tuple[int, int, int] | LeashStruct | None = None  # What the leash is attached to.
    home_radius: int | None = None  # Defaults to -1, which represents "no home".
    home_pos: tuple[int, int, int] | None = None  # This field will be discarded if `home_radius` is less than 0.
