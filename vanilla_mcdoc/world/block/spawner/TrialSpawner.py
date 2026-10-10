"""
Generated from symbols.json for ::java::world::block::spawner::TrialSpawner
Local link to file: vanilla_mcdoc/world/block/spawner/TrialSpawner.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec, MinecraftUUID

if TYPE_CHECKING:
    from vanilla_mcdoc.data.trial_spawner.TrialSpawnerConfig import TrialSpawnerConfig
    from vanilla_mcdoc.world.block.spawner.SpawnerEntry import SpawnerEntry


class TrialSpawner(GeneratedModel):
    normal_config: TrialSpawnerConfig | Annotated[str, IdSpec(registry='trial_spawner')] | None = None  # Spawning behavior when the player does not have the Bad Omen effect.
    ominous_config: TrialSpawnerConfig | Annotated[str, IdSpec(registry='trial_spawner')] | None = None  # Spawning behavior when the player has the Bad Omen effect.
    required_player_range: Annotated[int, Field(ge=1, le=128)] | None = None  # Maximum distance for players to activate the trial spawner, or join a battle
    target_cooldown_length: int | None = None  # Time in ticks for the cooldown period. Included the time spend dispensing the reward.
    registered_players: list[MinecraftUUID] | None = None  # Players that are have been nearby during the current battle
    current_mobs: list[MinecraftUUID] | None = None  # All mobs that have been spawned by this trial spawner and are currently alive
    cooldown_ends_at: int | None = None  # Gametime in ticks when the cooldown ends
    next_mob_spawns_at: int | None = None  # Gametime in ticks when the next spawning attempt happens
    total_mobs_spawned: int | None = None
    spawn_data: SpawnerEntry | None = None  # The next entity to spawn, also controlls the entity displayed in the trial spawner
    ejecting_loot_table: Annotated[str, IdSpec(registry='loot_table')] | None = None  # The loot table selected to be used to determine the reward
