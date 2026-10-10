"""
Generated from symbols.json for ::java::data::worldgen::attribute::NumericalEnvironmentAttribute
Local link to file: vanilla_mcdoc/data/worldgen/attribute/NumericalEnvironmentAttribute.py
"""
# ~~~ CODE ~~~
from enum import StrEnum


class NumericalEnvironmentAttribute(StrEnum):
    CLOUDHEIGHT = "visual/cloud_height"
    FOGSTARTDISTANCE = "visual/fog_start_distance"
    MOONANGLE = "visual/moon_angle"
    STARANGLE = "visual/star_angle"
    SUNANGLE = "visual/sun_angle"
    WATERFOGSTARTDISTANCE = "visual/water_fog_start_distance"
    CLOUDFOGENDDISTANCE = "visual/cloud_fog_end_distance"
    FOGENDDISTANCE = "visual/fog_end_distance"
    SKYFOGENDDISTANCE = "visual/sky_fog_end_distance"
    WATERFOGENDDISTANCE = "visual/water_fog_end_distance"
    SKYLIGHTFACTOR = "visual/sky_light_factor"
    STARBRIGHTNESS = "visual/star_brightness"
    MUSICVOLUME = "audio/music_volume"
    CATWAKINGUPGIFTCHANCE = "gameplay/cat_waking_up_gift_chance"
    CREATUREWORLDGENSPAWNPROBABILITY = "gameplay/creature_world_gen_spawn_probability"
    SURFACESLIMESPAWNCHANCE = "gameplay/surface_slime_spawn_chance"
    TURTLEEGGHATCHCHANCE = "gameplay/turtle_egg_hatch_chance"
    SKYLIGHTLEVEL = "gameplay/sky_light_level"
