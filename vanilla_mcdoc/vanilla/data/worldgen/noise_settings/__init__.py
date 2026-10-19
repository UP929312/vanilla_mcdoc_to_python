"""Vanilla's data/worldgen/noise_settings/ files"""
from vanilla_mcdoc.data.worldgen.density_function.DensityFunction import DensityFunctionStructAbs, DensityFunctionStructAdd, DensityFunctionStructBeardifier, DensityFunctionStructBlendDensity, DensityFunctionStructGradient, DensityFunctionStructInterpolated, DensityFunctionStructLerp, DensityFunctionStructMax, DensityFunctionStructMin, DensityFunctionStructMul, DensityFunctionStructNoise, DensityFunctionStructSqueeze, DensityFunctionStructSub
from vanilla_mcdoc.data.worldgen.noise_settings.Aquifer import Aquifer
from vanilla_mcdoc.data.worldgen.noise_settings.DebugFunctionEntry import DebugFunctionEntry
from vanilla_mcdoc.data.worldgen.noise_settings.NoiseGeneratorSettings import NoiseGeneratorSettings
from vanilla_mcdoc.data.worldgen.noise_settings.NoiseRouter import NoiseRouter
from vanilla_mcdoc.data.worldgen.noise_settings.NoiseSettings import NoiseSettings
from vanilla_mcdoc.util.direction.Axis import Axis

AMPLIFIED = NoiseGeneratorSettings(
    default_fluid='minecraft:water',
    sea_level=63,
    disable_mob_generation=False,
    aquifers=Aquifer(
        barrier=DensityFunctionStructNoise(noise='minecraft:aquifer_barrier', xz_scale=1.0, y_scale=0.5, type='minecraft:noise'),
        fluid_level_floodedness=DensityFunctionStructNoise(
            noise='minecraft:aquifer_fluid_level_floodedness',
            xz_scale=1.0,
            y_scale=0.67,
            type='minecraft:noise',
        ),
        fluid_level_spread=DensityFunctionStructNoise(
            noise='minecraft:aquifer_fluid_level_spread',
            xz_scale=1.0,
            y_scale=0.7142857142857143,
            type='minecraft:noise',
        ),
        lava=DensityFunctionStructNoise(noise='minecraft:aquifer_lava', xz_scale=1.0, y_scale=1.0, type='minecraft:noise'),
        exclusion=DensityFunctionStructMin(
            left=DensityFunctionStructSub(left=-0.225, right='minecraft:overworld/erosion', type='minecraft:sub'),
            right=DensityFunctionStructMax(
                left=DensityFunctionStructSub(left='minecraft:overworld_amplified/depth', right=0.9, type='minecraft:sub'),
                right=0.0,
                type='minecraft:max',
            ),
            type='minecraft:min',
        ),
        surface_level='minecraft:overworld_amplified/preliminary_surface_level',
    ),
    legacy_random_source=False,
    noise=NoiseSettings(min_y=-64, height=384),
    noise_router=NoiseRouter(
        temperature='minecraft:overworld/temperature',
        vegetation='minecraft:overworld/vegetation',
        continents='minecraft:overworld/continents',
        erosion='minecraft:overworld/erosion',
        depth='minecraft:overworld_amplified/depth',
        ridges='minecraft:overworld/ridges',
        chunk_surface_level='minecraft:overworld_amplified/chunk_surface_level',
        final_density='minecraft:overworld_amplified/final_density',
    ),
    spawn_target=[
        {
            'minecraft:overworld/continents': (-0.11, 1.0),
            'minecraft:overworld/erosion': (-1.0, 1.0),
            'minecraft:overworld/ridges': (-1.0, -0.16),
            'minecraft:overworld/temperature': (-1.0, 1.0),
            'minecraft:overworld/vegetation': (-1.0, 1.0),
        },
        {
            'minecraft:overworld/continents': (-0.11, 1.0),
            'minecraft:overworld/erosion': (-1.0, 1.0),
            'minecraft:overworld/ridges': (0.16, 1.0),
            'minecraft:overworld/temperature': (-1.0, 1.0),
            'minecraft:overworld/vegetation': (-1.0, 1.0),
        },
    ],
    material_rule='minecraft:overworld',
    debug_functions=[
        DebugFunctionEntry(label='Final density', function='minecraft:overworld_amplified/final_density'),
        DebugFunctionEntry(label='Temperature', function='minecraft:overworld/temperature'),
        DebugFunctionEntry(label='Vegetation', function='minecraft:overworld/vegetation'),
        DebugFunctionEntry(label='Continents', function='minecraft:overworld/continents'),
        DebugFunctionEntry(label='Erosion', function='minecraft:overworld/erosion'),
        DebugFunctionEntry(label='Depth', function='minecraft:overworld_amplified/depth'),
        DebugFunctionEntry(label='Ridges', function='minecraft:overworld/ridges'),
        DebugFunctionEntry(
            label='Peaks/Valleys',
            function=DensityFunctionStructMul(
                left=DensityFunctionStructAdd(
                    left=DensityFunctionStructAbs(
                        input=DensityFunctionStructAdd(
                            left=DensityFunctionStructAbs(input='minecraft:overworld/ridges', type='minecraft:abs'),
                            right=-0.6666667,
                            type='minecraft:add',
                        ),
                        type='minecraft:abs',
                    ),
                    right=-0.33333334,
                    type='minecraft:add',
                ),
                right=-3.0,
                type='minecraft:mul',
            ),
        ),
        DebugFunctionEntry(label='Prelim Surface', function='minecraft:overworld_amplified/preliminary_surface_level'),
    ],
)

CAVES = NoiseGeneratorSettings(
    default_fluid='minecraft:water',
    sea_level=32,
    disable_mob_generation=False,
    legacy_random_source=True,
    noise=NoiseSettings(min_y=-64, height=192),
    noise_router=NoiseRouter(
        temperature=0.0,
        vegetation=0.0,
        continents=0.0,
        erosion=0.0,
        depth=0.0,
        ridges=0.0,
        chunk_surface_level=0.0,
        final_density=DensityFunctionStructAdd(
            left=DensityFunctionStructSqueeze(
                input=DensityFunctionStructInterpolated(
                    input=DensityFunctionStructMul(
                        left=DensityFunctionStructBlendDensity(
                            input=DensityFunctionStructLerp(
                                alpha=DensityFunctionStructGradient(
                                    axis=Axis.Y,
                                    from_coordinate=-72,
                                    to_coordinate=-40,
                                    from_value=0.0,
                                    to_value=1.0,
                                    type='minecraft:gradient',
                                ),
                                first=2.5,
                                second=DensityFunctionStructLerp(
                                    alpha=DensityFunctionStructGradient(
                                        axis=Axis.Y,
                                        from_coordinate=104,
                                        to_coordinate=128,
                                        from_value=1.0,
                                        to_value=0.0,
                                        type='minecraft:gradient',
                                    ),
                                    first=0.9375,
                                    second='minecraft:nether/base_3d_noise',
                                    type='minecraft:lerp',
                                ),
                                type='minecraft:lerp',
                            ),
                            type='minecraft:blend_density',
                        ),
                        right=0.64,
                        type='minecraft:mul',
                    ),
                    cell_size_xz=4,
                    cell_size_y=8,
                    type='minecraft:interpolated',
                ),
                type='minecraft:squeeze',
            ),
            right=DensityFunctionStructBeardifier(type='minecraft:beardifier'),
            type='minecraft:add',
        ),
    ),
    spawn_target=[],
    material_rule='minecraft:overworld_caves',
    debug_functions=[
        DebugFunctionEntry(
            label='N',
            function=DensityFunctionStructAdd(
                left=DensityFunctionStructSqueeze(
                    input=DensityFunctionStructInterpolated(
                        input=DensityFunctionStructMul(
                            left=DensityFunctionStructBlendDensity(
                                input=DensityFunctionStructLerp(
                                    alpha=DensityFunctionStructGradient(
                                        axis=Axis.Y,
                                        from_coordinate=-72,
                                        to_coordinate=-40,
                                        from_value=0.0,
                                        to_value=1.0,
                                        type='minecraft:gradient',
                                    ),
                                    first=2.5,
                                    second=DensityFunctionStructLerp(
                                        alpha=DensityFunctionStructGradient(
                                            axis=Axis.Y,
                                            from_coordinate=104,
                                            to_coordinate=128,
                                            from_value=1.0,
                                            to_value=0.0,
                                            type='minecraft:gradient',
                                        ),
                                        first=0.9375,
                                        second='minecraft:nether/base_3d_noise',
                                        type='minecraft:lerp',
                                    ),
                                    type='minecraft:lerp',
                                ),
                                type='minecraft:blend_density',
                            ),
                            right=0.64,
                            type='minecraft:mul',
                        ),
                        cell_size_xz=4,
                        cell_size_y=8,
                        type='minecraft:interpolated',
                    ),
                    type='minecraft:squeeze',
                ),
                right=DensityFunctionStructBeardifier(type='minecraft:beardifier'),
                type='minecraft:add',
            ),
        ),
    ],
)

END = NoiseGeneratorSettings(
    default_fluid='minecraft:air',
    sea_level=0,
    disable_mob_generation=True,
    legacy_random_source=True,
    noise=NoiseSettings(min_y=0, height=128),
    noise_router=NoiseRouter(
        temperature=0.0,
        vegetation=0.0,
        continents=0.0,
        erosion='minecraft:end/islands',
        depth=0.0,
        ridges=0.0,
        chunk_surface_level=0.0,
        final_density=DensityFunctionStructAdd(
            left=DensityFunctionStructSqueeze(
                input=DensityFunctionStructInterpolated(
                    input=DensityFunctionStructMul(
                        left=DensityFunctionStructBlendDensity(
                            input=DensityFunctionStructLerp(
                                alpha=DensityFunctionStructGradient(
                                    axis=Axis.Y,
                                    from_coordinate=4,
                                    to_coordinate=32,
                                    from_value=0.0,
                                    to_value=1.0,
                                    type='minecraft:gradient',
                                ),
                                first=-0.234375,
                                second=DensityFunctionStructLerp(
                                    alpha=DensityFunctionStructGradient(
                                        axis=Axis.Y,
                                        from_coordinate=56,
                                        to_coordinate=312,
                                        from_value=1.0,
                                        to_value=0.0,
                                        type='minecraft:gradient',
                                    ),
                                    first=-23.4375,
                                    second='minecraft:end/sloped_cheese',
                                    type='minecraft:lerp',
                                ),
                                type='minecraft:lerp',
                            ),
                            type='minecraft:blend_density',
                        ),
                        right=0.64,
                        type='minecraft:mul',
                    ),
                    cell_size_xz=8,
                    cell_size_y=4,
                    type='minecraft:interpolated',
                ),
                type='minecraft:squeeze',
            ),
            right=DensityFunctionStructBeardifier(type='minecraft:beardifier'),
            type='minecraft:add',
        ),
    ),
    spawn_target=[],
    material_rule='minecraft:end',
    debug_functions=[
        DebugFunctionEntry(
            label='N',
            function=DensityFunctionStructAdd(
                left=DensityFunctionStructSqueeze(
                    input=DensityFunctionStructInterpolated(
                        input=DensityFunctionStructMul(
                            left=DensityFunctionStructBlendDensity(
                                input=DensityFunctionStructLerp(
                                    alpha=DensityFunctionStructGradient(
                                        axis=Axis.Y,
                                        from_coordinate=4,
                                        to_coordinate=32,
                                        from_value=0.0,
                                        to_value=1.0,
                                        type='minecraft:gradient',
                                    ),
                                    first=-0.234375,
                                    second=DensityFunctionStructLerp(
                                        alpha=DensityFunctionStructGradient(
                                            axis=Axis.Y,
                                            from_coordinate=56,
                                            to_coordinate=312,
                                            from_value=1.0,
                                            to_value=0.0,
                                            type='minecraft:gradient',
                                        ),
                                        first=-23.4375,
                                        second='minecraft:end/sloped_cheese',
                                        type='minecraft:lerp',
                                    ),
                                    type='minecraft:lerp',
                                ),
                                type='minecraft:blend_density',
                            ),
                            right=0.64,
                            type='minecraft:mul',
                        ),
                        cell_size_xz=8,
                        cell_size_y=4,
                        type='minecraft:interpolated',
                    ),
                    type='minecraft:squeeze',
                ),
                right=DensityFunctionStructBeardifier(type='minecraft:beardifier'),
                type='minecraft:add',
            ),
        ),
        DebugFunctionEntry(label='IS', function='minecraft:end/islands'),
    ],
)

FLOATING_ISLANDS = NoiseGeneratorSettings(
    default_fluid='minecraft:water',
    sea_level=-64,
    disable_mob_generation=False,
    legacy_random_source=True,
    noise=NoiseSettings(min_y=0, height=256),
    noise_router=NoiseRouter(
        temperature=0.0,
        vegetation=0.0,
        continents=0.0,
        erosion=0.0,
        depth=0.0,
        ridges=0.0,
        chunk_surface_level=0.0,
        final_density=DensityFunctionStructAdd(
            left=DensityFunctionStructSqueeze(
                input=DensityFunctionStructInterpolated(
                    input=DensityFunctionStructMul(
                        left=DensityFunctionStructBlendDensity(
                            input=DensityFunctionStructLerp(
                                alpha=DensityFunctionStructGradient(
                                    axis=Axis.Y,
                                    from_coordinate=4,
                                    to_coordinate=32,
                                    from_value=0.0,
                                    to_value=1.0,
                                    type='minecraft:gradient',
                                ),
                                first=-0.234375,
                                second=DensityFunctionStructLerp(
                                    alpha=DensityFunctionStructGradient(
                                        axis=Axis.Y,
                                        from_coordinate=184,
                                        to_coordinate=440,
                                        from_value=1.0,
                                        to_value=0.0,
                                        type='minecraft:gradient',
                                    ),
                                    first=-23.4375,
                                    second='minecraft:end/base_3d_noise',
                                    type='minecraft:lerp',
                                ),
                                type='minecraft:lerp',
                            ),
                            type='minecraft:blend_density',
                        ),
                        right=0.64,
                        type='minecraft:mul',
                    ),
                    cell_size_xz=8,
                    cell_size_y=4,
                    type='minecraft:interpolated',
                ),
                type='minecraft:squeeze',
            ),
            right=DensityFunctionStructBeardifier(type='minecraft:beardifier'),
            type='minecraft:add',
        ),
    ),
    spawn_target=[],
    material_rule='minecraft:overworld_floating_islands',
    debug_functions=[
        DebugFunctionEntry(
            label='N',
            function=DensityFunctionStructAdd(
                left=DensityFunctionStructSqueeze(
                    input=DensityFunctionStructInterpolated(
                        input=DensityFunctionStructMul(
                            left=DensityFunctionStructBlendDensity(
                                input=DensityFunctionStructLerp(
                                    alpha=DensityFunctionStructGradient(
                                        axis=Axis.Y,
                                        from_coordinate=4,
                                        to_coordinate=32,
                                        from_value=0.0,
                                        to_value=1.0,
                                        type='minecraft:gradient',
                                    ),
                                    first=-0.234375,
                                    second=DensityFunctionStructLerp(
                                        alpha=DensityFunctionStructGradient(
                                            axis=Axis.Y,
                                            from_coordinate=184,
                                            to_coordinate=440,
                                            from_value=1.0,
                                            to_value=0.0,
                                            type='minecraft:gradient',
                                        ),
                                        first=-23.4375,
                                        second='minecraft:end/base_3d_noise',
                                        type='minecraft:lerp',
                                    ),
                                    type='minecraft:lerp',
                                ),
                                type='minecraft:blend_density',
                            ),
                            right=0.64,
                            type='minecraft:mul',
                        ),
                        cell_size_xz=8,
                        cell_size_y=4,
                        type='minecraft:interpolated',
                    ),
                    type='minecraft:squeeze',
                ),
                right=DensityFunctionStructBeardifier(type='minecraft:beardifier'),
                type='minecraft:add',
            ),
        ),
    ],
)

LARGE_BIOMES = NoiseGeneratorSettings(
    default_fluid='minecraft:water',
    sea_level=63,
    disable_mob_generation=False,
    aquifers=Aquifer(
        barrier=DensityFunctionStructNoise(noise='minecraft:aquifer_barrier', xz_scale=1.0, y_scale=0.5, type='minecraft:noise'),
        fluid_level_floodedness=DensityFunctionStructNoise(
            noise='minecraft:aquifer_fluid_level_floodedness',
            xz_scale=1.0,
            y_scale=0.67,
            type='minecraft:noise',
        ),
        fluid_level_spread=DensityFunctionStructNoise(
            noise='minecraft:aquifer_fluid_level_spread',
            xz_scale=1.0,
            y_scale=0.7142857142857143,
            type='minecraft:noise',
        ),
        lava=DensityFunctionStructNoise(noise='minecraft:aquifer_lava', xz_scale=1.0, y_scale=1.0, type='minecraft:noise'),
        exclusion=DensityFunctionStructMin(
            left=DensityFunctionStructSub(
                left=-0.225,
                right='minecraft:overworld_large_biomes/erosion',
                type='minecraft:sub',
            ),
            right=DensityFunctionStructMax(
                left=DensityFunctionStructSub(left='minecraft:overworld_large_biomes/depth', right=0.9, type='minecraft:sub'),
                right=0.0,
                type='minecraft:max',
            ),
            type='minecraft:min',
        ),
        surface_level='minecraft:overworld_large_biomes/preliminary_surface_level',
    ),
    legacy_random_source=False,
    noise=NoiseSettings(min_y=-64, height=384),
    noise_router=NoiseRouter(
        temperature='minecraft:overworld_large_biomes/temperature',
        vegetation='minecraft:overworld_large_biomes/vegetation',
        continents='minecraft:overworld_large_biomes/continents',
        erosion='minecraft:overworld_large_biomes/erosion',
        depth='minecraft:overworld_large_biomes/depth',
        ridges='minecraft:overworld/ridges',
        chunk_surface_level='minecraft:overworld_large_biomes/chunk_surface_level',
        final_density='minecraft:overworld_large_biomes/final_density',
    ),
    spawn_target=[
        {
            'minecraft:overworld/ridges': (-1.0, -0.16),
            'minecraft:overworld_large_biomes/continents': (-0.11, 1.0),
            'minecraft:overworld_large_biomes/erosion': (-1.0, 1.0),
            'minecraft:overworld_large_biomes/temperature': (-1.0, 1.0),
            'minecraft:overworld_large_biomes/vegetation': (-1.0, 1.0),
        },
        {
            'minecraft:overworld/ridges': (0.16, 1.0),
            'minecraft:overworld_large_biomes/continents': (-0.11, 1.0),
            'minecraft:overworld_large_biomes/erosion': (-1.0, 1.0),
            'minecraft:overworld_large_biomes/temperature': (-1.0, 1.0),
            'minecraft:overworld_large_biomes/vegetation': (-1.0, 1.0),
        },
    ],
    material_rule='minecraft:overworld',
    debug_functions=[
        DebugFunctionEntry(label='Final density', function='minecraft:overworld_large_biomes/final_density'),
        DebugFunctionEntry(label='Temperature', function='minecraft:overworld_large_biomes/temperature'),
        DebugFunctionEntry(label='Vegetation', function='minecraft:overworld_large_biomes/vegetation'),
        DebugFunctionEntry(label='Continents', function='minecraft:overworld_large_biomes/continents'),
        DebugFunctionEntry(label='Erosion', function='minecraft:overworld_large_biomes/erosion'),
        DebugFunctionEntry(label='Depth', function='minecraft:overworld_large_biomes/depth'),
        DebugFunctionEntry(label='Ridges', function='minecraft:overworld/ridges'),
        DebugFunctionEntry(
            label='Peaks/Valleys',
            function=DensityFunctionStructMul(
                left=DensityFunctionStructAdd(
                    left=DensityFunctionStructAbs(
                        input=DensityFunctionStructAdd(
                            left=DensityFunctionStructAbs(input='minecraft:overworld/ridges', type='minecraft:abs'),
                            right=-0.6666667,
                            type='minecraft:add',
                        ),
                        type='minecraft:abs',
                    ),
                    right=-0.33333334,
                    type='minecraft:add',
                ),
                right=-3.0,
                type='minecraft:mul',
            ),
        ),
        DebugFunctionEntry(
            label='Prelim Surface',
            function='minecraft:overworld_large_biomes/preliminary_surface_level',
        ),
    ],
)

NETHER = NoiseGeneratorSettings(
    default_fluid='minecraft:lava',
    sea_level=32,
    disable_mob_generation=False,
    legacy_random_source=True,
    noise=NoiseSettings(min_y=0, height=128),
    noise_router=NoiseRouter(
        temperature=DensityFunctionStructNoise(
            noise='minecraft:nether/temperature',
            xz_scale=0.25,
            y_scale=0.0,
            type='minecraft:noise',
        ),
        vegetation=DensityFunctionStructNoise(
            noise='minecraft:nether/vegetation',
            xz_scale=0.25,
            y_scale=0.0,
            type='minecraft:noise',
        ),
        continents=0.0,
        erosion=0.0,
        depth=0.0,
        ridges=0.0,
        chunk_surface_level=0.0,
        final_density=DensityFunctionStructAdd(
            left=DensityFunctionStructSqueeze(
                input=DensityFunctionStructInterpolated(
                    input=DensityFunctionStructMul(
                        left=DensityFunctionStructBlendDensity(
                            input=DensityFunctionStructLerp(
                                alpha=DensityFunctionStructGradient(
                                    axis=Axis.Y,
                                    from_coordinate=-8,
                                    to_coordinate=24,
                                    from_value=0.0,
                                    to_value=1.0,
                                    type='minecraft:gradient',
                                ),
                                first=2.5,
                                second=DensityFunctionStructLerp(
                                    alpha=DensityFunctionStructGradient(
                                        axis=Axis.Y,
                                        from_coordinate=104,
                                        to_coordinate=128,
                                        from_value=1.0,
                                        to_value=0.0,
                                        type='minecraft:gradient',
                                    ),
                                    first=0.9375,
                                    second='minecraft:nether/base_3d_noise',
                                    type='minecraft:lerp',
                                ),
                                type='minecraft:lerp',
                            ),
                            type='minecraft:blend_density',
                        ),
                        right=0.64,
                        type='minecraft:mul',
                    ),
                    cell_size_xz=4,
                    cell_size_y=8,
                    type='minecraft:interpolated',
                ),
                type='minecraft:squeeze',
            ),
            right=DensityFunctionStructBeardifier(type='minecraft:beardifier'),
            type='minecraft:add',
        ),
    ),
    spawn_target=[],
    material_rule='minecraft:nether',
    debug_functions=[
        DebugFunctionEntry(
            label='N',
            function=DensityFunctionStructAdd(
                left=DensityFunctionStructSqueeze(
                    input=DensityFunctionStructInterpolated(
                        input=DensityFunctionStructMul(
                            left=DensityFunctionStructBlendDensity(
                                input=DensityFunctionStructLerp(
                                    alpha=DensityFunctionStructGradient(
                                        axis=Axis.Y,
                                        from_coordinate=-8,
                                        to_coordinate=24,
                                        from_value=0.0,
                                        to_value=1.0,
                                        type='minecraft:gradient',
                                    ),
                                    first=2.5,
                                    second=DensityFunctionStructLerp(
                                        alpha=DensityFunctionStructGradient(
                                            axis=Axis.Y,
                                            from_coordinate=104,
                                            to_coordinate=128,
                                            from_value=1.0,
                                            to_value=0.0,
                                            type='minecraft:gradient',
                                        ),
                                        first=0.9375,
                                        second='minecraft:nether/base_3d_noise',
                                        type='minecraft:lerp',
                                    ),
                                    type='minecraft:lerp',
                                ),
                                type='minecraft:blend_density',
                            ),
                            right=0.64,
                            type='minecraft:mul',
                        ),
                        cell_size_xz=4,
                        cell_size_y=8,
                        type='minecraft:interpolated',
                    ),
                    type='minecraft:squeeze',
                ),
                right=DensityFunctionStructBeardifier(type='minecraft:beardifier'),
                type='minecraft:add',
            ),
        ),
        DebugFunctionEntry(
            label='T',
            function=DensityFunctionStructNoise(
                noise='minecraft:nether/temperature',
                xz_scale=0.25,
                y_scale=0.0,
                type='minecraft:noise',
            ),
        ),
        DebugFunctionEntry(
            label='V',
            function=DensityFunctionStructNoise(
                noise='minecraft:nether/vegetation',
                xz_scale=0.25,
                y_scale=0.0,
                type='minecraft:noise',
            ),
        ),
    ],
)

OVERWORLD = NoiseGeneratorSettings(
    default_fluid='minecraft:water',
    sea_level=63,
    disable_mob_generation=False,
    aquifers=Aquifer(
        barrier=DensityFunctionStructNoise(noise='minecraft:aquifer_barrier', xz_scale=1.0, y_scale=0.5, type='minecraft:noise'),
        fluid_level_floodedness=DensityFunctionStructNoise(
            noise='minecraft:aquifer_fluid_level_floodedness',
            xz_scale=1.0,
            y_scale=0.67,
            type='minecraft:noise',
        ),
        fluid_level_spread=DensityFunctionStructNoise(
            noise='minecraft:aquifer_fluid_level_spread',
            xz_scale=1.0,
            y_scale=0.7142857142857143,
            type='minecraft:noise',
        ),
        lava=DensityFunctionStructNoise(noise='minecraft:aquifer_lava', xz_scale=1.0, y_scale=1.0, type='minecraft:noise'),
        exclusion=DensityFunctionStructMin(
            left=DensityFunctionStructSub(left=-0.225, right='minecraft:overworld/erosion', type='minecraft:sub'),
            right=DensityFunctionStructMax(
                left=DensityFunctionStructSub(left='minecraft:overworld/depth', right=0.9, type='minecraft:sub'),
                right=0.0,
                type='minecraft:max',
            ),
            type='minecraft:min',
        ),
        surface_level='minecraft:overworld/preliminary_surface_level',
    ),
    legacy_random_source=False,
    noise=NoiseSettings(min_y=-64, height=384),
    noise_router=NoiseRouter(
        temperature='minecraft:overworld/temperature',
        vegetation='minecraft:overworld/vegetation',
        continents='minecraft:overworld/continents',
        erosion='minecraft:overworld/erosion',
        depth='minecraft:overworld/depth',
        ridges='minecraft:overworld/ridges',
        chunk_surface_level='minecraft:overworld/chunk_surface_level',
        final_density='minecraft:overworld/final_density',
    ),
    spawn_target=[
        {
            'minecraft:overworld/continents': (-0.11, 1.0),
            'minecraft:overworld/erosion': (-1.0, 1.0),
            'minecraft:overworld/ridges': (-1.0, -0.16),
            'minecraft:overworld/temperature': (-1.0, 1.0),
            'minecraft:overworld/vegetation': (-1.0, 1.0),
        },
        {
            'minecraft:overworld/continents': (-0.11, 1.0),
            'minecraft:overworld/erosion': (-1.0, 1.0),
            'minecraft:overworld/ridges': (0.16, 1.0),
            'minecraft:overworld/temperature': (-1.0, 1.0),
            'minecraft:overworld/vegetation': (-1.0, 1.0),
        },
    ],
    material_rule='minecraft:overworld',
    debug_functions=[
        DebugFunctionEntry(label='Final density', function='minecraft:overworld/final_density'),
        DebugFunctionEntry(label='Temperature', function='minecraft:overworld/temperature'),
        DebugFunctionEntry(label='Vegetation', function='minecraft:overworld/vegetation'),
        DebugFunctionEntry(label='Continents', function='minecraft:overworld/continents'),
        DebugFunctionEntry(label='Erosion', function='minecraft:overworld/erosion'),
        DebugFunctionEntry(label='Depth', function='minecraft:overworld/depth'),
        DebugFunctionEntry(label='Ridges', function='minecraft:overworld/ridges'),
        DebugFunctionEntry(
            label='Peaks/Valleys',
            function=DensityFunctionStructMul(
                left=DensityFunctionStructAdd(
                    left=DensityFunctionStructAbs(
                        input=DensityFunctionStructAdd(
                            left=DensityFunctionStructAbs(input='minecraft:overworld/ridges', type='minecraft:abs'),
                            right=-0.6666667,
                            type='minecraft:add',
                        ),
                        type='minecraft:abs',
                    ),
                    right=-0.33333334,
                    type='minecraft:add',
                ),
                right=-3.0,
                type='minecraft:mul',
            ),
        ),
        DebugFunctionEntry(label='Prelim Surface', function='minecraft:overworld/preliminary_surface_level'),
    ],
)
