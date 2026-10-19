"""Vanilla's data/cat_sound_variant/ files"""
from vanilla_mcdoc.data.variants.SoundVariant import SoundVariant
from vanilla_mcdoc.data.variants.cat.OptionalCatSounds import OptionalCatSounds

CLASSIC = SoundVariant(
    adult_sounds=OptionalCatSounds(
        ambient_sound='minecraft:entity.cat.ambient',
        stray_ambient_sound='minecraft:entity.cat.stray_ambient',
        hiss_sound='minecraft:entity.cat.hiss',
        hurt_sound='minecraft:entity.cat.hurt',
        death_sound='minecraft:entity.cat.death',
        eat_sound='minecraft:entity.cat.eat',
        beg_for_food_sound='minecraft:entity.cat.beg_for_food',
        purr_sound='minecraft:entity.cat.purr',
        purreow_sound='minecraft:entity.cat.purreow',
    ),
    baby_sounds=OptionalCatSounds(
        ambient_sound='minecraft:entity.baby_cat.ambient',
        stray_ambient_sound='minecraft:entity.baby_cat.stray_ambient',
        hiss_sound='minecraft:entity.baby_cat.hiss',
        hurt_sound='minecraft:entity.baby_cat.hurt',
        death_sound='minecraft:entity.baby_cat.death',
        eat_sound='minecraft:entity.baby_cat.eat',
        beg_for_food_sound='minecraft:entity.baby_cat.beg_for_food',
        purr_sound='minecraft:entity.baby_cat.purr',
        purreow_sound='minecraft:entity.baby_cat.purreow',
    ),
)

ROYAL = SoundVariant(
    adult_sounds=OptionalCatSounds(
        ambient_sound='minecraft:entity.cat_royal.ambient',
        stray_ambient_sound='minecraft:entity.cat_royal.stray_ambient',
        hiss_sound='minecraft:entity.cat_royal.hiss',
        hurt_sound='minecraft:entity.cat_royal.hurt',
        death_sound='minecraft:entity.cat_royal.death',
        eat_sound='minecraft:entity.cat_royal.eat',
        beg_for_food_sound='minecraft:entity.cat_royal.beg_for_food',
        purr_sound='minecraft:entity.cat_royal.purr',
        purreow_sound='minecraft:entity.cat_royal.purreow',
    ),
    baby_sounds=OptionalCatSounds(
        ambient_sound='minecraft:entity.baby_cat.ambient',
        stray_ambient_sound='minecraft:entity.baby_cat.stray_ambient',
        hiss_sound='minecraft:entity.baby_cat.hiss',
        hurt_sound='minecraft:entity.baby_cat.hurt',
        death_sound='minecraft:entity.baby_cat.death',
        eat_sound='minecraft:entity.baby_cat.eat',
        beg_for_food_sound='minecraft:entity.baby_cat.beg_for_food',
        purr_sound='minecraft:entity.baby_cat.purr',
        purreow_sound='minecraft:entity.baby_cat.purreow',
    ),
)
