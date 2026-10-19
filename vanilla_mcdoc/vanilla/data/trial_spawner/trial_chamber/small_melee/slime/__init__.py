"""Vanilla's data/trial_spawner/trial_chamber/small_melee/slime/ files"""
from vanilla_mcdoc.data.trial_spawner.TrialSpawnerConfig import TrialSpawnerConfig
from vanilla_mcdoc.util.WeightedEntry import WeightedEntry
from vanilla_mcdoc.world.block.spawner.SpawnerEntry import SpawnerEntry
from vanilla_mcdoc.world.entity.AnyEntity import AnyEntitySlime

NORMAL = TrialSpawnerConfig(
    simultaneous_mobs=3.0,
    simultaneous_mobs_added_per_player=0.5,
    ticks_between_spawn=20,
    spawn_potentials=[
        WeightedEntry(weight=3, data=SpawnerEntry(entity=AnyEntitySlime(Size=1, id='minecraft:slime'))),
        WeightedEntry(weight=1, data=SpawnerEntry(entity=AnyEntitySlime(Size=2, id='minecraft:slime'))),
    ],
)

OMINOUS = TrialSpawnerConfig(
    total_mobs=12.0,
    simultaneous_mobs=4.0,
    simultaneous_mobs_added_per_player=0.5,
    ticks_between_spawn=20,
    spawn_potentials=[
        WeightedEntry(weight=3, data=SpawnerEntry(entity=AnyEntitySlime(Size=1, id='minecraft:slime'))),
        WeightedEntry(weight=1, data=SpawnerEntry(entity=AnyEntitySlime(Size=2, id='minecraft:slime'))),
    ],
    loot_tables_to_eject=[
        WeightedEntry(weight=3, data='minecraft:spawners/ominous/trial_chamber/key'),
        WeightedEntry(weight=7, data='minecraft:spawners/ominous/trial_chamber/consumables'),
    ],
)
