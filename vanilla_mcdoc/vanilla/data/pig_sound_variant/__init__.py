"""Vanilla's data/pig_sound_variant/ files"""
from vanilla_mcdoc.data.variants.SoundVariant import SoundVariant
from vanilla_mcdoc.data.variants.pig.OptionalPigSounds import OptionalPigSounds

BIG = SoundVariant(
    adult_sounds=OptionalPigSounds(
        ambient_sound='minecraft:entity.pig_big.ambient',
        hurt_sound='minecraft:entity.pig_big.hurt',
        death_sound='minecraft:entity.pig_big.death',
        step_sound='minecraft:entity.pig.step',
        eat_sound='minecraft:entity.pig_big.eat',
    ),
    baby_sounds=OptionalPigSounds(
        ambient_sound='minecraft:entity.baby_pig.ambient',
        hurt_sound='minecraft:entity.baby_pig.hurt',
        death_sound='minecraft:entity.baby_pig.death',
        step_sound='minecraft:entity.baby_pig.step',
        eat_sound='minecraft:entity.baby_pig.eat',
    ),
)

CLASSIC = SoundVariant(
    adult_sounds=OptionalPigSounds(
        ambient_sound='minecraft:entity.pig.ambient',
        hurt_sound='minecraft:entity.pig.hurt',
        death_sound='minecraft:entity.pig.death',
        step_sound='minecraft:entity.pig.step',
        eat_sound='minecraft:entity.pig.eat',
    ),
    baby_sounds=OptionalPigSounds(
        ambient_sound='minecraft:entity.baby_pig.ambient',
        hurt_sound='minecraft:entity.baby_pig.hurt',
        death_sound='minecraft:entity.baby_pig.death',
        step_sound='minecraft:entity.baby_pig.step',
        eat_sound='minecraft:entity.baby_pig.eat',
    ),
)

MINI = SoundVariant(
    adult_sounds=OptionalPigSounds(
        ambient_sound='minecraft:entity.pig_mini.ambient',
        hurt_sound='minecraft:entity.pig_mini.hurt',
        death_sound='minecraft:entity.pig_mini.death',
        step_sound='minecraft:entity.pig.step',
        eat_sound='minecraft:entity.pig_mini.eat',
    ),
    baby_sounds=OptionalPigSounds(
        ambient_sound='minecraft:entity.baby_pig.ambient',
        hurt_sound='minecraft:entity.baby_pig.hurt',
        death_sound='minecraft:entity.baby_pig.death',
        step_sound='minecraft:entity.baby_pig.step',
        eat_sound='minecraft:entity.baby_pig.eat',
    ),
)
