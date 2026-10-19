"""Vanilla's data/trial_spawner/trial_chamber/melee/zombie/ files"""
from vanilla_mcdoc.data.trial_spawner.TrialSpawnerConfig import TrialSpawnerConfig
from vanilla_mcdoc.util.WeightedEntry import WeightedEntry
from vanilla_mcdoc.world.block.spawner.SpawnEquipment import SpawnEquipment
from vanilla_mcdoc.world.block.spawner.SpawnerEntry import SpawnerEntry
from vanilla_mcdoc.world.entity.AnyEntity import AnyEntityZombie

NORMAL = TrialSpawnerConfig(
    simultaneous_mobs=3.0,
    simultaneous_mobs_added_per_player=0.5,
    ticks_between_spawn=20,
    spawn_potentials=[WeightedEntry(weight=1, data=SpawnerEntry(entity=AnyEntityZombie(id='minecraft:zombie')))],
)

OMINOUS = TrialSpawnerConfig(
    simultaneous_mobs=3.0,
    simultaneous_mobs_added_per_player=0.5,
    ticks_between_spawn=20,
    spawn_potentials=[
        WeightedEntry(
            weight=1,
            data=SpawnerEntry(
                entity=AnyEntityZombie(id='minecraft:zombie'),
                equipment=SpawnEquipment(loot_table='minecraft:equipment/trial_chamber_melee', slot_drop_chances=0.0),
            ),
        ),
    ],
    loot_tables_to_eject=[
        WeightedEntry(weight=3, data='minecraft:spawners/ominous/trial_chamber/key'),
        WeightedEntry(weight=7, data='minecraft:spawners/ominous/trial_chamber/consumables'),
    ],
)
