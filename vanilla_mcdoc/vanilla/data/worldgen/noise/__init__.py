"""Vanilla's data/worldgen/noise/ files"""
from vanilla_mcdoc.data.worldgen.dimension.biome_source.NoiseParameters import NoiseParameters

AQUIFER_BARRIER = NoiseParameters(base_octave=-3, base_amplitude=0.955388882960065)

AQUIFER_FLUID_LEVEL_FLOODEDNESS = NoiseParameters(base_octave=-7, base_amplitude=0.955388882960065)

AQUIFER_FLUID_LEVEL_SPREAD = NoiseParameters(base_octave=-5, base_amplitude=0.955388882960065)

AQUIFER_LAVA = NoiseParameters(base_octave=-1, base_amplitude=0.955388882960065)

BADLANDS_PILLAR = NoiseParameters(base_octave=-2, base_amplitude=0.939546696581729, octave_count=4)

BADLANDS_PILLAR_ROOF = NoiseParameters(base_octave=-8, base_amplitude=0.955388882960065)

BADLANDS_SURFACE = NoiseParameters(base_octave=-6, base_amplitude=0.9381732587751008, octave_count=3)

CALCITE = NoiseParameters(base_octave=-9, base_amplitude=0.939546696581729, octave_count=4)

CAVE_CHEESE = NoiseParameters(
    base_octave=-8,
    base_amplitude=0.8361300524356068,
    octave_count=9,
    amplitude_modifiers=[0.5, 1.0, 2.0, 1.0, 2.0, 1.0, 0.0, 2.0, 0.0],
)

CAVE_ENTRANCE = NoiseParameters(base_octave=-7, base_amplitude=0.8500634887071167, octave_count=3, amplitude_modifiers=[0.4, 0.5, 1.0])

CAVE_LAYER = NoiseParameters(base_octave=-8, base_amplitude=0.955388882960065)

CLAY_BANDS_OFFSET = NoiseParameters(base_octave=-8, base_amplitude=0.955388882960065)

CONTINENTALNESS = NoiseParameters(
    base_octave=-9,
    base_amplitude=0.8880832896205223,
    octave_count=9,
    amplitude_modifiers=[1.0, 1.0, 2.0, 2.0, 2.0, 1.0, 1.0, 1.0, 1.0],
)

CONTINENTALNESS_LARGE = NoiseParameters(
    base_octave=-11,
    base_amplitude=0.8880832896205223,
    octave_count=9,
    amplitude_modifiers=[1.0, 1.0, 2.0, 2.0, 2.0, 1.0, 1.0, 1.0, 1.0],
)

EROSION = NoiseParameters(
    base_octave=-9,
    base_amplitude=1.063180125160734,
    octave_count=5,
    amplitude_modifiers=[1.0, 1.0, 0.0, 1.0, 1.0],
)

EROSION_LARGE = NoiseParameters(
    base_octave=-11,
    base_amplitude=1.063180125160734,
    octave_count=5,
    amplitude_modifiers=[1.0, 1.0, 0.0, 1.0, 1.0],
)

GRAVEL = NoiseParameters(base_octave=-8, base_amplitude=0.939546696581729, octave_count=4)

GRAVEL_LAYER = NoiseParameters(
    base_octave=-8,
    base_amplitude=1.0569606747151457,
    octave_count=9,
    amplitude_modifiers=[1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.013333333333333334],
)

ICE = NoiseParameters(base_octave=-4, base_amplitude=0.939546696581729, octave_count=4)

ICEBERG_PILLAR = NoiseParameters(base_octave=-6, base_amplitude=0.939546696581729, octave_count=4)

ICEBERG_PILLAR_ROOF = NoiseParameters(base_octave=-3, base_amplitude=0.955388882960065)

ICEBERG_SURFACE = NoiseParameters(base_octave=-6, base_amplitude=0.9381732587751008, octave_count=3)

ICE_CAVE_GRADIENT = NoiseParameters(base_octave=-4, base_amplitude=1.1817507833955654, octave_count=3, amplitude_modifiers=[1.0, 0.0, 1.0])

JAGGED = NoiseParameters(base_octave=-16, base_amplitude=1.0383104856073737, octave_count=16)

NETHERRACK = NoiseParameters(
    base_octave=-3,
    base_amplitude=1.4659491761370222,
    octave_count=4,
    amplitude_modifiers=[1.0, 0.0, 0.0, 0.35],
)

NETHER_STATE_SELECTOR = NoiseParameters(base_octave=-4, base_amplitude=0.955388882960065)

NETHER_WART = NoiseParameters(
    base_octave=-3,
    base_amplitude=1.3827102115748344,
    octave_count=4,
    amplitude_modifiers=[1.0, 0.0, 0.0, 0.9],
)

NOODLE = NoiseParameters(base_octave=-8, base_amplitude=0.955388882960065)

NOODLE_RIDGE_A = NoiseParameters(base_octave=-7, base_amplitude=0.955388882960065)

NOODLE_RIDGE_B = NoiseParameters(base_octave=-7, base_amplitude=0.955388882960065)

NOODLE_THICKNESS = NoiseParameters(base_octave=-8, base_amplitude=0.955388882960065)

OFFSET = NoiseParameters(
    base_octave=-3,
    base_amplitude=0.9381732587751005,
    octave_count=4,
    amplitude_modifiers=[1.0, 1.0, 1.0, 0.0],
)

ORE_GAP = NoiseParameters(base_octave=-5, base_amplitude=0.955388882960065)

ORE_VEININESS = NoiseParameters(base_octave=-8, base_amplitude=0.955388882960065)

ORE_VEIN_A = NoiseParameters(base_octave=-7, base_amplitude=0.955388882960065)

ORE_VEIN_B = NoiseParameters(base_octave=-7, base_amplitude=0.955388882960065)

PACKED_ICE = NoiseParameters(base_octave=-7, base_amplitude=0.939546696581729, octave_count=4)

PATCH = NoiseParameters(
    base_octave=-5,
    base_amplitude=1.637127519350388,
    octave_count=6,
    amplitude_modifiers=[1.0, 0.0, 0.0, 0.0, 0.0, 0.013333333333333334],
)

PILLAR = NoiseParameters(base_octave=-7, base_amplitude=0.9494731054427981, octave_count=2)

PILLAR_RARENESS = NoiseParameters(base_octave=-8, base_amplitude=0.955388882960065)

PILLAR_THICKNESS = NoiseParameters(base_octave=-8, base_amplitude=0.955388882960065)

POWDER_SNOW = NoiseParameters(base_octave=-6, base_amplitude=0.939546696581729, octave_count=4)

RIDGE = NoiseParameters(
    base_octave=-7,
    base_amplitude=0.9147152149950137,
    octave_count=6,
    amplitude_modifiers=[1.0, 2.0, 1.0, 0.0, 0.0, 0.0],
)

SMALL_PATCH = NoiseParameters(base_octave=-3, base_amplitude=0.955388882960065, amplitude_modifiers=[3.0])

SOUL_SAND_LAYER = NoiseParameters(
    base_octave=-8,
    base_amplitude=1.0569606747151457,
    octave_count=9,
    amplitude_modifiers=[1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.013333333333333334],
)

SPAGHETTI_2D = NoiseParameters(base_octave=-7, base_amplitude=0.955388882960065)

SPAGHETTI_2D_ELEVATION = NoiseParameters(base_octave=-8, base_amplitude=0.955388882960065)

SPAGHETTI_2D_MODULATOR = NoiseParameters(base_octave=-11, base_amplitude=0.955388882960065)

SPAGHETTI_2D_THICKNESS = NoiseParameters(base_octave=-11, base_amplitude=0.955388882960065)

SPAGHETTI_3D_1 = NoiseParameters(base_octave=-7, base_amplitude=0.955388882960065)

SPAGHETTI_3D_2 = NoiseParameters(base_octave=-7, base_amplitude=0.955388882960065)

SPAGHETTI_3D_RARITY = NoiseParameters(base_octave=-11, base_amplitude=0.955388882960065)

SPAGHETTI_3D_THICKNESS = NoiseParameters(base_octave=-8, base_amplitude=0.955388882960065)

SPAGHETTI_ROUGHNESS = NoiseParameters(base_octave=-5, base_amplitude=0.955388882960065)

SPAGHETTI_ROUGHNESS_MODULATOR = NoiseParameters(base_octave=-8, base_amplitude=0.955388882960065)

SULFUR_CAVE_GRADIENT = NoiseParameters(base_octave=-5, base_amplitude=1.1817507833955654, octave_count=3, amplitude_modifiers=[1.0, 0.0, 1.0])

SURFACE = NoiseParameters(base_octave=-6, base_amplitude=0.9381732587751008, octave_count=3)

SURFACE_SECONDARY = NoiseParameters(
    base_octave=-6,
    base_amplitude=1.0582769165096106,
    octave_count=4,
    amplitude_modifiers=[1.0, 1.0, 0.0, 1.0],
)

SURFACE_SWAMP = NoiseParameters(base_octave=-2, base_amplitude=0.955388882960065)

TEMPERATURE = NoiseParameters(
    base_octave=-10,
    base_amplitude=1.2453007926713473,
    octave_count=6,
    amplitude_modifiers=[1.5, 0.0, 1.0, 0.0, 0.0, 0.0],
)

TEMPERATURE_LARGE = NoiseParameters(
    base_octave=-12,
    base_amplitude=1.2453007926713473,
    octave_count=6,
    amplitude_modifiers=[1.5, 0.0, 1.0, 0.0, 0.0, 0.0],
)

VEGETATION = NoiseParameters(
    base_octave=-8,
    base_amplitude=0.9494731054427978,
    octave_count=6,
    amplitude_modifiers=[1.0, 1.0, 0.0, 0.0, 0.0, 0.0],
)

VEGETATION_LARGE = NoiseParameters(
    base_octave=-10,
    base_amplitude=0.9494731054427978,
    octave_count=6,
    amplitude_modifiers=[1.0, 1.0, 0.0, 0.0, 0.0, 0.0],
)
