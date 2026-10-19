"""Vanilla's data/chicken_sound_variant/ files"""
from vanilla_mcdoc.data.variants.SoundVariant import SoundVariant
from vanilla_mcdoc.data.variants.chicken.OptionalChickenSounds import OptionalChickenSounds

CLASSIC = SoundVariant(
    adult_sounds=OptionalChickenSounds(
        ambient_sound='minecraft:entity.chicken.ambient',
        hurt_sound='minecraft:entity.chicken.hurt',
        death_sound='minecraft:entity.chicken.death',
        step_sound='minecraft:entity.chicken.step',
    ),
    baby_sounds=OptionalChickenSounds(
        ambient_sound='minecraft:entity.baby_chicken.ambient',
        hurt_sound='minecraft:entity.baby_chicken.hurt',
        death_sound='minecraft:entity.baby_chicken.death',
        step_sound='minecraft:entity.baby_chicken.step',
    ),
)

PICKY = SoundVariant(
    adult_sounds=OptionalChickenSounds(
        ambient_sound='minecraft:entity.chicken_picky.ambient',
        hurt_sound='minecraft:entity.chicken_picky.hurt',
        death_sound='minecraft:entity.chicken_picky.death',
        step_sound='minecraft:entity.chicken_picky.step',
    ),
    baby_sounds=OptionalChickenSounds(
        ambient_sound='minecraft:entity.baby_chicken.ambient',
        hurt_sound='minecraft:entity.baby_chicken.hurt',
        death_sound='minecraft:entity.baby_chicken.death',
        step_sound='minecraft:entity.baby_chicken.step',
    ),
)
