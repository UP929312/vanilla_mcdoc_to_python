"""Vanilla's data/wolf_sound_variant/ files"""
from typing import Any
from vanilla_mcdoc.data.variants.SoundVariant import SoundVariant
from vanilla_mcdoc.data.variants.wolf.OptionalWolfSounds import OptionalWolfSounds

ANGRY = SoundVariant(
    adult_sounds=OptionalWolfSounds(
        ambient_sound='minecraft:entity.wolf_angry.ambient',
        death_sound='minecraft:entity.wolf_angry.death',
        growl_sound='minecraft:entity.wolf_angry.growl',
        hurt_sound='minecraft:entity.wolf_angry.hurt',
        pant_sound='minecraft:entity.wolf_angry.pant',
        whine_sound='minecraft:entity.wolf_angry.whine',
        **dict[str, Any]({'step_sound': 'minecraft:entity.wolf.step'}),
    ),
    baby_sounds=OptionalWolfSounds(
        ambient_sound='minecraft:entity.baby_wolf.ambient',
        death_sound='minecraft:entity.baby_wolf.death',
        growl_sound='minecraft:entity.baby_wolf.growl',
        hurt_sound='minecraft:entity.baby_wolf.hurt',
        pant_sound='minecraft:entity.baby_wolf.pant',
        whine_sound='minecraft:entity.baby_wolf.whine',
        **dict[str, Any]({'step_sound': 'minecraft:entity.baby_wolf.step'}),
    ),
)

BIG = SoundVariant(
    adult_sounds=OptionalWolfSounds(
        ambient_sound='minecraft:entity.wolf_big.ambient',
        death_sound='minecraft:entity.wolf_big.death',
        growl_sound='minecraft:entity.wolf_big.growl',
        hurt_sound='minecraft:entity.wolf_big.hurt',
        pant_sound='minecraft:entity.wolf_big.pant',
        whine_sound='minecraft:entity.wolf_big.whine',
        **dict[str, Any]({'step_sound': 'minecraft:entity.wolf.step'}),
    ),
    baby_sounds=OptionalWolfSounds(
        ambient_sound='minecraft:entity.baby_wolf.ambient',
        death_sound='minecraft:entity.baby_wolf.death',
        growl_sound='minecraft:entity.baby_wolf.growl',
        hurt_sound='minecraft:entity.baby_wolf.hurt',
        pant_sound='minecraft:entity.baby_wolf.pant',
        whine_sound='minecraft:entity.baby_wolf.whine',
        **dict[str, Any]({'step_sound': 'minecraft:entity.baby_wolf.step'}),
    ),
)

CLASSIC = SoundVariant(
    adult_sounds=OptionalWolfSounds(
        ambient_sound='minecraft:entity.wolf.ambient',
        death_sound='minecraft:entity.wolf.death',
        growl_sound='minecraft:entity.wolf.growl',
        hurt_sound='minecraft:entity.wolf.hurt',
        pant_sound='minecraft:entity.wolf.pant',
        whine_sound='minecraft:entity.wolf.whine',
        **dict[str, Any]({'step_sound': 'minecraft:entity.wolf.step'}),
    ),
    baby_sounds=OptionalWolfSounds(
        ambient_sound='minecraft:entity.baby_wolf.ambient',
        death_sound='minecraft:entity.baby_wolf.death',
        growl_sound='minecraft:entity.baby_wolf.growl',
        hurt_sound='minecraft:entity.baby_wolf.hurt',
        pant_sound='minecraft:entity.baby_wolf.pant',
        whine_sound='minecraft:entity.baby_wolf.whine',
        **dict[str, Any]({'step_sound': 'minecraft:entity.baby_wolf.step'}),
    ),
)

CUTE = SoundVariant(
    adult_sounds=OptionalWolfSounds(
        ambient_sound='minecraft:entity.wolf_cute.ambient',
        death_sound='minecraft:entity.wolf_cute.death',
        growl_sound='minecraft:entity.wolf_cute.growl',
        hurt_sound='minecraft:entity.wolf_cute.hurt',
        pant_sound='minecraft:entity.wolf_cute.pant',
        whine_sound='minecraft:entity.wolf_cute.whine',
        **dict[str, Any]({'step_sound': 'minecraft:entity.wolf.step'}),
    ),
    baby_sounds=OptionalWolfSounds(
        ambient_sound='minecraft:entity.baby_wolf.ambient',
        death_sound='minecraft:entity.baby_wolf.death',
        growl_sound='minecraft:entity.baby_wolf.growl',
        hurt_sound='minecraft:entity.baby_wolf.hurt',
        pant_sound='minecraft:entity.baby_wolf.pant',
        whine_sound='minecraft:entity.baby_wolf.whine',
        **dict[str, Any]({'step_sound': 'minecraft:entity.baby_wolf.step'}),
    ),
)

GRUMPY = SoundVariant(
    adult_sounds=OptionalWolfSounds(
        ambient_sound='minecraft:entity.wolf_grumpy.ambient',
        death_sound='minecraft:entity.wolf_grumpy.death',
        growl_sound='minecraft:entity.wolf_grumpy.growl',
        hurt_sound='minecraft:entity.wolf_grumpy.hurt',
        pant_sound='minecraft:entity.wolf_grumpy.pant',
        whine_sound='minecraft:entity.wolf_grumpy.whine',
        **dict[str, Any]({'step_sound': 'minecraft:entity.wolf.step'}),
    ),
    baby_sounds=OptionalWolfSounds(
        ambient_sound='minecraft:entity.baby_wolf.ambient',
        death_sound='minecraft:entity.baby_wolf.death',
        growl_sound='minecraft:entity.baby_wolf.growl',
        hurt_sound='minecraft:entity.baby_wolf.hurt',
        pant_sound='minecraft:entity.baby_wolf.pant',
        whine_sound='minecraft:entity.baby_wolf.whine',
        **dict[str, Any]({'step_sound': 'minecraft:entity.baby_wolf.step'}),
    ),
)

PUGLIN = SoundVariant(
    adult_sounds=OptionalWolfSounds(
        ambient_sound='minecraft:entity.wolf_puglin.ambient',
        death_sound='minecraft:entity.wolf_puglin.death',
        growl_sound='minecraft:entity.wolf_puglin.growl',
        hurt_sound='minecraft:entity.wolf_puglin.hurt',
        pant_sound='minecraft:entity.wolf_puglin.pant',
        whine_sound='minecraft:entity.wolf_puglin.whine',
        **dict[str, Any]({'step_sound': 'minecraft:entity.wolf.step'}),
    ),
    baby_sounds=OptionalWolfSounds(
        ambient_sound='minecraft:entity.baby_wolf.ambient',
        death_sound='minecraft:entity.baby_wolf.death',
        growl_sound='minecraft:entity.baby_wolf.growl',
        hurt_sound='minecraft:entity.baby_wolf.hurt',
        pant_sound='minecraft:entity.baby_wolf.pant',
        whine_sound='minecraft:entity.baby_wolf.whine',
        **dict[str, Any]({'step_sound': 'minecraft:entity.baby_wolf.step'}),
    ),
)

SAD = SoundVariant(
    adult_sounds=OptionalWolfSounds(
        ambient_sound='minecraft:entity.wolf_sad.ambient',
        death_sound='minecraft:entity.wolf_sad.death',
        growl_sound='minecraft:entity.wolf_sad.growl',
        hurt_sound='minecraft:entity.wolf_sad.hurt',
        pant_sound='minecraft:entity.wolf_sad.pant',
        whine_sound='minecraft:entity.wolf_sad.whine',
        **dict[str, Any]({'step_sound': 'minecraft:entity.wolf.step'}),
    ),
    baby_sounds=OptionalWolfSounds(
        ambient_sound='minecraft:entity.baby_wolf.ambient',
        death_sound='minecraft:entity.baby_wolf.death',
        growl_sound='minecraft:entity.baby_wolf.growl',
        hurt_sound='minecraft:entity.baby_wolf.hurt',
        pant_sound='minecraft:entity.baby_wolf.pant',
        whine_sound='minecraft:entity.baby_wolf.whine',
        **dict[str, Any]({'step_sound': 'minecraft:entity.baby_wolf.step'}),
    ),
)
