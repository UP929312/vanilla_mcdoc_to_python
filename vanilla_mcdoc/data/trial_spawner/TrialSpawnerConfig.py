"""
Generated from symbols.json for ::java::data::trial_spawner::TrialSpawnerConfig
Local link to file: vanilla_mcdoc/data/trial_spawner/TrialSpawnerConfig.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.util.WeightedList import WeightedList
    from vanilla_mcdoc.world.block.spawner.SpawnPotential import SpawnPotential


class TrialSpawnerConfig(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'trial_spawner'

    spawn_range: Annotated[int, Field(ge=1, le=128)] | None = None  # Maximum distance from the spawner that en entity can spawn
    total_mobs: float | None = None  # Total amount of entities that are spawned during one activation, when 1 player is nearby
    total_mobs_added_per_player: float | None = None  # Number added to `total_mobs` for each additional player
    simultaneous_mobs: float | None = None  # Number of entities that that can be present at once, when 1 player is nearby
    simultaneous_mobs_added_per_player: float | None = None  # Number added to `simultaneous_mobs` for each additional player
    ticks_between_spawn: int | None = None  # Ticks until the next spawn.
    spawn_potentials: list[SpawnPotential] | None = None  # Entities that can be placed.
    loot_tables_to_eject: WeightedList[Annotated[str, IdSpec(registry='loot_table')]] | None = None  # Loot tables to use when ejecting loot. Chooses one loot table based on weight and then uses it as often as there are players nearby.
    items_to_drop_when_ominous: Annotated[str, IdSpec(registry='loot_table')] | None = None  # Loot table to use when summoning ominous item spawners. One roll seeded based on rough location to determine all items used during the battle.
