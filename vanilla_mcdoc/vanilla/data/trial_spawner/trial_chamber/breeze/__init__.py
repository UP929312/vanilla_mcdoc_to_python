"""Vanilla's data/trial_spawner/trial_chamber/breeze/ files"""
from vanilla_mcdoc.data.trial_spawner.TrialSpawnerConfig import TrialSpawnerConfig
from vanilla_mcdoc.util.WeightedEntry import WeightedEntry
from vanilla_mcdoc.world.block.spawner.SpawnerEntry import SpawnerEntry
from vanilla_mcdoc.world.entity.AnyEntity import AnyEntityBreeze

NORMAL = TrialSpawnerConfig(
    total_mobs=2.0,
    total_mobs_added_per_player=1.0,
    simultaneous_mobs=1.0,
    simultaneous_mobs_added_per_player=0.5,
    ticks_between_spawn=20,
    spawn_potentials=[WeightedEntry(weight=1, data=SpawnerEntry(entity=AnyEntityBreeze(id='minecraft:breeze')))],
)

OMINOUS = TrialSpawnerConfig(
    total_mobs=4.0,
    total_mobs_added_per_player=1.0,
    simultaneous_mobs_added_per_player=0.5,
    ticks_between_spawn=20,
    spawn_potentials=[WeightedEntry(weight=1, data=SpawnerEntry(entity=AnyEntityBreeze(id='minecraft:breeze')))],
    loot_tables_to_eject=[
        WeightedEntry(weight=3, data='minecraft:spawners/ominous/trial_chamber/key'),
        WeightedEntry(weight=7, data='minecraft:spawners/ominous/trial_chamber/consumables'),
    ],
)
