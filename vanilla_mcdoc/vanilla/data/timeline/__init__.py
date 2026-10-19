"""Vanilla's data/timeline/ files"""
from vanilla_mcdoc.data.timeline.CubicBezierEase import CubicBezierEase
from vanilla_mcdoc.data.timeline.EnvironmentAttributeTrackMap import EnvironmentAttributeTrackMapValueStruct1, EnvironmentAttributeTrackMapValueStruct12, EnvironmentAttributeTrackMapValueStruct4, EnvironmentAttributeTrackMapValueStruct5, KeyframesStruct, KeyframesStruct12, KeyframesStruct4, KeyframesStruct5
from vanilla_mcdoc.data.timeline.SimpleEasingType import SimpleEasingType
from vanilla_mcdoc.data.timeline.TimeMarker import TimeMarker
from vanilla_mcdoc.data.timeline.Timeline import Timeline
from vanilla_mcdoc.data.worldgen.attribute.modifier.BooleanModifierType import BooleanModifierType
from vanilla_mcdoc.data.worldgen.attribute.modifier.ColorModifierType import ColorModifierType
from vanilla_mcdoc.data.worldgen.attribute.modifier.FloatModifierType import FloatModifierType

DAY = Timeline(
    period_ticks=24000,
    clock='minecraft:overworld',
    time_markers={
        'minecraft:day': TimeMarker(ticks=1000, show_in_commands=True),
        'minecraft:midnight': TimeMarker(ticks=18000, show_in_commands=True),
        'minecraft:night': TimeMarker(ticks=13000, show_in_commands=True),
        'minecraft:noon': TimeMarker(ticks=6000, show_in_commands=True),
        'minecraft:roll_village_siege': 18000,
        'minecraft:wake_up_from_sleep': 0,
    },
    tracks={
        'minecraft:audio/firefly_bush_sounds': EnvironmentAttributeTrackMapValueStruct4(
            modifier=BooleanModifierType.OR,
            keyframes=[KeyframesStruct4(ticks=12600, value=True), KeyframesStruct4(ticks=23401, value=False)],
        ),
        'minecraft:gameplay/bees_stay_in_hive': EnvironmentAttributeTrackMapValueStruct4(
            modifier=BooleanModifierType.OR,
            keyframes=[KeyframesStruct4(ticks=12542, value=True), KeyframesStruct4(ticks=23460, value=False)],
        ),
        'minecraft:gameplay/cat_waking_up_gift_chance': EnvironmentAttributeTrackMapValueStruct5(
            ease=SimpleEasingType.CONSTANT,
            modifier=FloatModifierType.MAXIMUM,
            keyframes=[KeyframesStruct5(ticks=362, value=0.0), KeyframesStruct5(ticks=23667, value=0.7)],
        ),
        'minecraft:gameplay/creaking_active': EnvironmentAttributeTrackMapValueStruct4(
            modifier=BooleanModifierType.OR,
            keyframes=[KeyframesStruct4(ticks=12600, value=True), KeyframesStruct4(ticks=23401, value=False)],
        ),
        'minecraft:gameplay/eyeblossom_open': EnvironmentAttributeTrackMapValueStruct1(
            keyframes=[KeyframesStruct(ticks=12600, value=True), KeyframesStruct(ticks=23401, value=False)],
        ),
        'minecraft:gameplay/monsters_burn': EnvironmentAttributeTrackMapValueStruct4(
            modifier=BooleanModifierType.OR,
            keyframes=[KeyframesStruct4(ticks=12542, value=False), KeyframesStruct4(ticks=23460, value=True)],
        ),
        'minecraft:gameplay/sky_light_level': EnvironmentAttributeTrackMapValueStruct5(
            modifier=FloatModifierType.MULTIPLY,
            keyframes=[
                KeyframesStruct5(ticks=133, value=1.0),
                KeyframesStruct5(ticks=11867, value=1.0),
                KeyframesStruct5(ticks=13670, value=0.26666668),
                KeyframesStruct5(ticks=22330, value=0.26666668),
            ],
        ),
        'minecraft:gameplay/turtle_egg_hatch_chance': EnvironmentAttributeTrackMapValueStruct5(
            ease=SimpleEasingType.CONSTANT,
            modifier=FloatModifierType.MAXIMUM,
            keyframes=[KeyframesStruct5(ticks=21062, value=1.0), KeyframesStruct5(ticks=21905, value=0.002)],
        ),
        'minecraft:visual/cloud_color': EnvironmentAttributeTrackMapValueStruct12(
            modifier=ColorModifierType.MULTIPLY,
            keyframes=[
                KeyframesStruct12(ticks=133, value='#ffffffff'),
                KeyframesStruct12(ticks=11867, value='#ffffffff'),
                KeyframesStruct12(ticks=13670, value='#ff191926'),
                KeyframesStruct12(ticks=22330, value='#ff191926'),
            ],
        ),
        'minecraft:visual/fog_color': EnvironmentAttributeTrackMapValueStruct12(
            modifier=ColorModifierType.MULTIPLY,
            keyframes=[
                KeyframesStruct12(ticks=133, value='#ffffff'),
                KeyframesStruct12(ticks=11867, value='#ffffff'),
                KeyframesStruct12(ticks=13670, value='#0f0f16'),
                KeyframesStruct12(ticks=22330, value='#0f0f16'),
            ],
        ),
        'minecraft:visual/moon_angle': EnvironmentAttributeTrackMapValueStruct1(
            ease=CubicBezierEase(cubic_bezier=(0.362, 0.241, 0.638, 0.759)),
            keyframes=[KeyframesStruct(ticks=6000, value=540.0), KeyframesStruct(ticks=6000, value=180.0)],
        ),
        'minecraft:visual/sky_color': EnvironmentAttributeTrackMapValueStruct12(
            modifier=ColorModifierType.MULTIPLY,
            keyframes=[
                KeyframesStruct12(ticks=133, value='#ffffff'),
                KeyframesStruct12(ticks=11867, value='#ffffff'),
                KeyframesStruct12(ticks=13670, value='#000000'),
                KeyframesStruct12(ticks=22330, value='#000000'),
            ],
        ),
        'minecraft:visual/sky_light_color': EnvironmentAttributeTrackMapValueStruct12(
            modifier=ColorModifierType.MULTIPLY,
            keyframes=[
                KeyframesStruct12(ticks=730, value='#ffffff'),
                KeyframesStruct12(ticks=11270, value='#ffffff'),
                KeyframesStruct12(ticks=13140, value='#7a7aff'),
                KeyframesStruct12(ticks=22860, value='#7a7aff'),
            ],
        ),
        'minecraft:visual/sky_light_factor': EnvironmentAttributeTrackMapValueStruct5(
            modifier=FloatModifierType.MULTIPLY,
            keyframes=[
                KeyframesStruct5(ticks=730, value=1.0),
                KeyframesStruct5(ticks=11270, value=1.0),
                KeyframesStruct5(ticks=13140, value=0.24),
                KeyframesStruct5(ticks=22860, value=0.24),
            ],
        ),
        'minecraft:visual/star_angle': EnvironmentAttributeTrackMapValueStruct1(
            ease=CubicBezierEase(cubic_bezier=(0.362, 0.241, 0.638, 0.759)),
            keyframes=[KeyframesStruct(ticks=6000, value=360.0), KeyframesStruct(ticks=6000, value=0.0)],
        ),
        'minecraft:visual/star_brightness': EnvironmentAttributeTrackMapValueStruct5(
            modifier=FloatModifierType.MAXIMUM,
            keyframes=[
                KeyframesStruct5(ticks=92, value=0.037),
                KeyframesStruct5(ticks=627, value=0.0),
                KeyframesStruct5(ticks=11373, value=0.0),
                KeyframesStruct5(ticks=11732, value=0.016),
                KeyframesStruct5(ticks=11959, value=0.044),
                KeyframesStruct5(ticks=12399, value=0.143),
                KeyframesStruct5(ticks=12729, value=0.258),
                KeyframesStruct5(ticks=13228, value=0.5),
                KeyframesStruct5(ticks=22772, value=0.5),
                KeyframesStruct5(ticks=23032, value=0.364),
                KeyframesStruct5(ticks=23356, value=0.225),
                KeyframesStruct5(ticks=23758, value=0.101),
            ],
        ),
        'minecraft:visual/sun_angle': EnvironmentAttributeTrackMapValueStruct1(
            ease=CubicBezierEase(cubic_bezier=(0.362, 0.241, 0.638, 0.759)),
            keyframes=[KeyframesStruct(ticks=6000, value=360.0), KeyframesStruct(ticks=6000, value=0.0)],
        ),
        'minecraft:visual/sunrise_sunset_color': EnvironmentAttributeTrackMapValueStruct1(
            keyframes=[
                KeyframesStruct(ticks=71, value='#5fefa333'),
                KeyframesStruct(ticks=310, value='#29f5ba33'),
                KeyframesStruct(ticks=565, value='#06fbd433'),
                KeyframesStruct(ticks=730, value='#00ffe533'),
                KeyframesStruct(ticks=11270, value='#00ffe533'),
                KeyframesStruct(ticks=11397, value='#04fcd833'),
                KeyframesStruct(ticks=11522, value='#0ff9cb33'),
                KeyframesStruct(ticks=11690, value='#29f5ba33'),
                KeyframesStruct(ticks=11929, value='#5fefa333'),
                KeyframesStruct(ticks=12243, value='#b1e78733'),
                KeyframesStruct(ticks=12358, value='#cce47e33'),
                KeyframesStruct(ticks=12512, value='#e9e07233'),
                KeyframesStruct(ticks=12613, value='#f6dd6b33'),
                KeyframesStruct(ticks=12732, value='#feda6333'),
                KeyframesStruct(ticks=12841, value='#fed75c33'),
                KeyframesStruct(ticks=13035, value='#ecd25133'),
                KeyframesStruct(ticks=13252, value='#c1cc4733'),
                KeyframesStruct(ticks=13775, value='#36be3733'),
                KeyframesStruct(ticks=13888, value='#1fbb3533'),
                KeyframesStruct(ticks=14039, value='#09b73333'),
                KeyframesStruct(ticks=14192, value='#00b33333'),
                KeyframesStruct(ticks=21807, value='#00b23333'),
                KeyframesStruct(ticks=21961, value='#09b73333'),
                KeyframesStruct(ticks=22112, value='#1fbb3533'),
                KeyframesStruct(ticks=22225, value='#36be3733'),
                KeyframesStruct(ticks=22748, value='#c1cc4733'),
                KeyframesStruct(ticks=22965, value='#ecd25133'),
                KeyframesStruct(ticks=23159, value='#fed75c33'),
                KeyframesStruct(ticks=23272, value='#feda6333'),
                KeyframesStruct(ticks=23488, value='#e9e07233'),
                KeyframesStruct(ticks=23642, value='#cce47e33'),
                KeyframesStruct(ticks=23757, value='#b1e78733'),
            ],
        ),
    },
)

EARLY_GAME = Timeline(
    clock='minecraft:overworld',
    tracks={
        'minecraft:gameplay/can_pillager_patrol_spawn': EnvironmentAttributeTrackMapValueStruct4(
            modifier=BooleanModifierType.AND,
            keyframes=[KeyframesStruct4(ticks=0, value=False), KeyframesStruct4(ticks=120000, value=True)],
        ),
    },
)

MOON = Timeline(
    period_ticks=192000,
    clock='minecraft:overworld',
    tracks={
        'minecraft:gameplay/surface_slime_spawn_chance': EnvironmentAttributeTrackMapValueStruct5(
            ease=SimpleEasingType.CONSTANT,
            modifier=FloatModifierType.MAXIMUM,
            keyframes=[
                KeyframesStruct5(ticks=0, value=0.5),
                KeyframesStruct5(ticks=24000, value=0.375),
                KeyframesStruct5(ticks=48000, value=0.25),
                KeyframesStruct5(ticks=72000, value=0.125),
                KeyframesStruct5(ticks=96000, value=0.0),
                KeyframesStruct5(ticks=120000, value=0.125),
                KeyframesStruct5(ticks=144000, value=0.25),
                KeyframesStruct5(ticks=168000, value=0.375),
            ],
        ),
        'minecraft:visual/moon_phase': EnvironmentAttributeTrackMapValueStruct1(
            keyframes=[
                KeyframesStruct(ticks=0, value='full_moon'),
                KeyframesStruct(ticks=24000, value='waning_gibbous'),
                KeyframesStruct(ticks=48000, value='third_quarter'),
                KeyframesStruct(ticks=72000, value='waning_crescent'),
                KeyframesStruct(ticks=96000, value='new_moon'),
                KeyframesStruct(ticks=120000, value='waxing_crescent'),
                KeyframesStruct(ticks=144000, value='first_quarter'),
                KeyframesStruct(ticks=168000, value='waxing_gibbous'),
            ],
        ),
    },
)

VILLAGER_SCHEDULE = Timeline(
    period_ticks=24000,
    clock='minecraft:overworld',
    tracks={
        'minecraft:gameplay/baby_villager_activity': EnvironmentAttributeTrackMapValueStruct1(
            keyframes=[
                KeyframesStruct(ticks=10, value='minecraft:idle'),
                KeyframesStruct(ticks=3000, value='minecraft:play'),
                KeyframesStruct(ticks=6000, value='minecraft:idle'),
                KeyframesStruct(ticks=10000, value='minecraft:play'),
                KeyframesStruct(ticks=12000, value='minecraft:rest'),
            ],
        ),
        'minecraft:gameplay/villager_activity': EnvironmentAttributeTrackMapValueStruct1(
            keyframes=[
                KeyframesStruct(ticks=10, value='minecraft:idle'),
                KeyframesStruct(ticks=2000, value='minecraft:work'),
                KeyframesStruct(ticks=9000, value='minecraft:meet'),
                KeyframesStruct(ticks=11000, value='minecraft:idle'),
                KeyframesStruct(ticks=12000, value='minecraft:rest'),
            ],
        ),
    },
)
