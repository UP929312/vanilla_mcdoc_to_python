"""Vanilla's data/cow_sound_variant/ files"""
from vanilla_mcdoc.data.variants.cow.OptionalCowSounds import OptionalCowSounds

CLASSIC = OptionalCowSounds(
    ambient_sound='minecraft:entity.cow.ambient',
    hurt_sound='minecraft:entity.cow.hurt',
    death_sound='minecraft:entity.cow.death',
    step_sound='minecraft:entity.cow.step',
)

MOODY = OptionalCowSounds(
    ambient_sound='minecraft:entity.cow_moody.ambient',
    hurt_sound='minecraft:entity.cow_moody.hurt',
    death_sound='minecraft:entity.cow_moody.death',
    step_sound='minecraft:entity.cow_moody.step',
)
