"""Vanilla's data/trial_spawner/trial_chamber/slow_ranged/stray/ files"""
from vanilla_mcdoc.data.trial_spawner.TrialSpawnerConfig import TrialSpawnerConfig
from vanilla_mcdoc.util.WeightedEntry import WeightedEntry
from vanilla_mcdoc.world.block.spawner.SpawnEquipment import SpawnEquipment
from vanilla_mcdoc.world.block.spawner.SpawnerEntry import SpawnerEntry
from vanilla_mcdoc.world.entity.AnyEntity import AnyEntityStray

NORMAL = TrialSpawnerConfig(
    simultaneous_mobs=4.0,
    simultaneous_mobs_added_per_player=2.0,
    ticks_between_spawn=160,
    spawn_potentials=[WeightedEntry(weight=1, data=SpawnerEntry(entity=AnyEntityStray(id='minecraft:stray')))],
)

OMINOUS = TrialSpawnerConfig(
    simultaneous_mobs=4.0,
    simultaneous_mobs_added_per_player=2.0,
    ticks_between_spawn=160,
    spawn_potentials=[
        WeightedEntry(
            weight=1,
            data=SpawnerEntry(
                entity=AnyEntityStray(id='minecraft:stray'),
                equipment=SpawnEquipment(loot_table='minecraft:equipment/trial_chamber_ranged', slot_drop_chances=0.0),
            ),
        ),
    ],
    loot_tables_to_eject=[
        WeightedEntry(weight=3, data='minecraft:spawners/ominous/trial_chamber/key'),
        WeightedEntry(weight=7, data='minecraft:spawners/ominous/trial_chamber/consumables'),
    ],
)
