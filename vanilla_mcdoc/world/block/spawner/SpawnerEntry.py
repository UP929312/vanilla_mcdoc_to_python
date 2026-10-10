"""
Generated from symbols.json for ::java::world::block::spawner::SpawnerEntry
Local link to file: vanilla_mcdoc/world/block/spawner/SpawnerEntry.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.world.block.spawner.CustomSpawnRules import CustomSpawnRules
    from vanilla_mcdoc.world.block.spawner.SpawnEquipment import SpawnEquipment
    from vanilla_mcdoc.world.entity.AnyEntity import AnyEntity


class SpawnerEntry(GeneratedModel):
    entity: AnyEntity
    custom_spawn_rules: CustomSpawnRules | None = None
    equipment: SpawnEquipment | None = None  # Rolled items from the specified loot table will be equipped to the mob that spawns.
