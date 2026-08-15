"""
Generated from symbols.json for ::java::data::worldgen::density_function::DensityFunction
Local link to file: generated_symbols/data/worldgen/density_function/DensityFunction.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Literal

from generated_symbols.data.worldgen.density_function.Noise import Noise
from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.density_function.CubicSpline import CubicSpline
    from generated_symbols.data.worldgen.density_function.DensityFunctionRef import DensityFunctionRef
    from generated_symbols.data.worldgen.density_function.DistanceMetric import DistanceMetric
    from generated_symbols.data.worldgen.density_function.NoiseParametersRef import NoiseParametersRef
    from generated_symbols.data.worldgen.density_function.NoiseRange import NoiseRange
    from generated_symbols.data.worldgen.density_function.RarityType import RarityType
    from generated_symbols.data.worldgen.density_function.SplineType import SplineType
    from generated_symbols.data.worldgen.density_function.TilingMode import TilingMode
    from generated_symbols.util.direction.Axis import Axis


@dataclass(kw_only=True)
class DensityFunctionStructUnknown:
    type: Annotated[str, IdSpec(registry='worldgen/density_function_type')]


@dataclass(kw_only=True)
class DensityFunctionStructAbs:
    type: Literal['minecraft:abs']
    input: DensityFunctionRef


@dataclass(kw_only=True)
class DensityFunctionStructAdd:
    type: Literal['minecraft:add']
    left: DensityFunctionRef
    right: DensityFunctionRef


@dataclass(kw_only=True)
class DensityFunctionStructBlendDensity:
    type: Literal['minecraft:blend_density']
    input: DensityFunctionRef


@dataclass(kw_only=True)
class DensityFunctionStructCache2d:
    type: Literal['minecraft:cache_2d']
    input: DensityFunctionRef


@dataclass(kw_only=True)
class DensityFunctionStructCacheAllInCell:
    type: Literal['minecraft:cache_all_in_cell']
    input: DensityFunctionRef


@dataclass(kw_only=True)
class DensityFunctionStructCacheOnce:
    type: Literal['minecraft:cache_once']
    input: DensityFunctionRef


@dataclass(kw_only=True)
class DensityFunctionStructCeil:
    type: Literal['minecraft:ceil']
    input: DensityFunctionRef
    multiple: DensityFunctionRef | None = None  # Defaults to constant 1.


@dataclass(kw_only=True)
class DensityFunctionStructClamp:
    type: Literal['minecraft:clamp']
    input: DensityFunctionRef
    min: NoiseRange
    max: NoiseRange


@dataclass(kw_only=True)
class DensityFunctionStructConstant:
    type: Literal['minecraft:constant']
    value: NoiseRange


@dataclass(kw_only=True)
class DensityFunctionStructCube:
    type: Literal['minecraft:cube']
    input: DensityFunctionRef


@dataclass(kw_only=True)
class DensityFunctionStructDistanceToPoint:
    type: Literal['minecraft:distance_to_point']
    point: tuple[int, int, int]
    metric: DistanceMetric


@dataclass(kw_only=True)
class DensityFunctionStructDiv:
    type: Literal['minecraft:div']
    left: DensityFunctionRef
    right: DensityFunctionRef


@dataclass(kw_only=True)
class DensityFunctionStructFindTopSurface:
    type: Literal['minecraft:find_top_surface']
    density: DensityFunctionRef
    upper_bound: DensityFunctionRef
    lower_bound: Annotated[int, 'Range | `-4064`-`4062` | both inclusive']
    cell_height: Annotated[int, 'Range | Min `1` and above | inclusive']


@dataclass(kw_only=True)
class DensityFunctionStructFlatCache:
    type: Literal['minecraft:flat_cache']
    input: DensityFunctionRef


@dataclass(kw_only=True)
class DensityFunctionStructFloor:
    type: Literal['minecraft:floor']
    input: DensityFunctionRef
    multiple: DensityFunctionRef | None = None  # Defaults to constant 1.


@dataclass(kw_only=True)
class DensityFunctionStructGradient:
    type: Literal['minecraft:gradient']
    axis: Axis
    from_coordinate: int
    to_coordinate: int
    from_value: NoiseRange
    to_value: NoiseRange
    tiling: TilingMode | None = None  # Defaults to `clamp_to_edge`.


@dataclass(kw_only=True)
class DensityFunctionStructHalfNegative:
    type: Literal['minecraft:half_negative']
    input: DensityFunctionRef


@dataclass(kw_only=True)
class DensityFunctionStructInterpolated:
    type: Literal['minecraft:interpolated']
    input: DensityFunctionRef


@dataclass(kw_only=True)
class DensityFunctionStructIntervalSelect:
    type: Literal['minecraft:interval_select']
    input: DensityFunctionRef
    thresholds: Annotated[list[NoiseRange], 'Length = 1 (inclusive) and above']  # Must have exactly one fewer element than `functions`.
    functions: Annotated[list[DensityFunctionRef], 'Length = 2 (inclusive) and above']  # Must have exactly one more element than `thresholds`.


@dataclass(kw_only=True)
class DensityFunctionStructInvert:
    type: Literal['minecraft:invert']
    input: DensityFunctionRef


@dataclass(kw_only=True)
class DensityFunctionStructLerp:
    type: Literal['minecraft:lerp']
    alpha: DensityFunctionRef
    first: DensityFunctionRef
    second: DensityFunctionRef


@dataclass(kw_only=True)
class DensityFunctionStructLog:
    type: Literal['minecraft:log']
    input: DensityFunctionRef


@dataclass(kw_only=True)
class DensityFunctionStructMax:
    type: Literal['minecraft:max']
    left: DensityFunctionRef
    right: DensityFunctionRef


@dataclass(kw_only=True)
class DensityFunctionStructMin:
    type: Literal['minecraft:min']
    left: DensityFunctionRef
    right: DensityFunctionRef


@dataclass(kw_only=True)
class DensityFunctionStructMul:
    type: Literal['minecraft:mul']
    left: DensityFunctionRef
    right: DensityFunctionRef


@dataclass(kw_only=True)
class DensityFunctionStructNegate:
    type: Literal['minecraft:negate']
    input: DensityFunctionRef


@dataclass(kw_only=True)
class DensityFunctionStructNoise:
    type: Literal['minecraft:noise']
    noise: NoiseParametersRef
    xz_scale: float
    y_scale: float


@dataclass(kw_only=True)
class DensityFunctionStructOldBlendedNoise:
    type: Literal['minecraft:old_blended_noise']
    xz_scale: float
    y_scale: float
    xz_factor: float
    y_factor: float
    smear_scale_multiplier: Annotated[float, 'Range | `1`-`8` | both inclusive']


@dataclass(kw_only=True)
class DensityFunctionStructPow:
    type: Literal['minecraft:pow']
    base: DensityFunctionRef
    exponent: DensityFunctionRef


@dataclass(kw_only=True)
class DensityFunctionStructQuarterNegative:
    type: Literal['minecraft:quarter_negative']
    input: DensityFunctionRef


@dataclass(kw_only=True)
class DensityFunctionStructRangeChoice:
    type: Literal['minecraft:range_choice']
    input: DensityFunctionRef
    min_inclusive: NoiseRange
    max_exclusive: NoiseRange
    when_in_range: DensityFunctionRef
    when_out_of_range: DensityFunctionRef


@dataclass(kw_only=True)
class DensityFunctionStructReciprocal:
    type: Literal['minecraft:reciprocal']
    input: DensityFunctionRef


@dataclass(kw_only=True)
class DensityFunctionStructRound:
    type: Literal['minecraft:round']
    input: DensityFunctionRef
    multiple: DensityFunctionRef | None = None  # Defaults to constant 1.


@dataclass(kw_only=True)
class DensityFunctionStructShift:
    type: Literal['minecraft:shift']
    noise: NoiseParametersRef


@dataclass(kw_only=True)
class DensityFunctionStructShiftA:
    type: Literal['minecraft:shift_a']
    noise: NoiseParametersRef


@dataclass(kw_only=True)
class DensityFunctionStructShiftB:
    type: Literal['minecraft:shift_b']
    noise: NoiseParametersRef


@dataclass(kw_only=True)
class DensityFunctionStructShiftedNoise(Noise):
    type: Literal['minecraft:shifted_noise']
    shift_x: DensityFunctionRef
    shift_y: DensityFunctionRef
    shift_z: DensityFunctionRef


@dataclass(kw_only=True)
class DensityFunctionStructSign:
    type: Literal['minecraft:sign']
    input: DensityFunctionRef


@dataclass(kw_only=True)
class DensityFunctionStructSlice:
    type: Literal['minecraft:slice']
    axis: Axis
    coordinate: int
    input: DensityFunctionRef


@dataclass(kw_only=True)
class DensityFunctionStructSlide:
    type: Literal['minecraft:slide']
    input: DensityFunctionRef


@dataclass(kw_only=True)
class DensityFunctionStructSpline:
    type: Literal['minecraft:spline']
    spline: CubicSpline


@dataclass(kw_only=True)
class DensityFunctionStructSqrt:
    type: Literal['minecraft:sqrt']
    input: DensityFunctionRef


@dataclass(kw_only=True)
class DensityFunctionStructSquare:
    type: Literal['minecraft:square']
    input: DensityFunctionRef


@dataclass(kw_only=True)
class DensityFunctionStructSqueeze:
    type: Literal['minecraft:squeeze']
    input: DensityFunctionRef


@dataclass(kw_only=True)
class DensityFunctionStructSub:
    type: Literal['minecraft:sub']
    left: DensityFunctionRef
    right: DensityFunctionRef


@dataclass(kw_only=True)
class DensityFunctionStructTerrainShaperSpline:
    type: Literal['minecraft:terrain_shaper_spline']
    spline: SplineType
    min_value: NoiseRange
    max_value: NoiseRange
    continentalness: DensityFunctionRef
    erosion: DensityFunctionRef
    weirdness: DensityFunctionRef


@dataclass(kw_only=True)
class DensityFunctionStructTruncate:
    type: Literal['minecraft:truncate']
    input: DensityFunctionRef
    multiple: DensityFunctionRef | None = None  # Defaults to constant 1.


@dataclass(kw_only=True)
class DensityFunctionStructWeirdScaledSampler:
    type: Literal['minecraft:weird_scaled_sampler']
    rarity_value_mapper: RarityType
    noise: NoiseParametersRef
    input: DensityFunctionRef


@dataclass(kw_only=True)
class DensityFunctionStructYClampedGradient:
    type: Literal['minecraft:y_clamped_gradient']
    from_y: Annotated[int, 'Range | `-4064`-`4062` | both inclusive']
    to_y: Annotated[int, 'Range | `-4064`-`4062` | both inclusive']
    from_value: NoiseRange
    to_value: NoiseRange


type DensityFunctionStruct = DensityFunctionStructUnknown | DensityFunctionStructAbs | DensityFunctionStructAdd | DensityFunctionStructBlendDensity | DensityFunctionStructCache2d | DensityFunctionStructCacheAllInCell | DensityFunctionStructCacheOnce | DensityFunctionStructCeil | DensityFunctionStructClamp | DensityFunctionStructConstant | DensityFunctionStructCube | DensityFunctionStructDistanceToPoint | DensityFunctionStructDiv | DensityFunctionStructFindTopSurface | DensityFunctionStructFlatCache | DensityFunctionStructFloor | DensityFunctionStructGradient | DensityFunctionStructHalfNegative | DensityFunctionStructInterpolated | DensityFunctionStructIntervalSelect | DensityFunctionStructInvert | DensityFunctionStructLerp | DensityFunctionStructLog | DensityFunctionStructMax | DensityFunctionStructMin | DensityFunctionStructMul | DensityFunctionStructNegate | DensityFunctionStructNoise | DensityFunctionStructOldBlendedNoise | DensityFunctionStructPow | DensityFunctionStructQuarterNegative | DensityFunctionStructRangeChoice | DensityFunctionStructReciprocal | DensityFunctionStructRound | DensityFunctionStructShift | DensityFunctionStructShiftA | DensityFunctionStructShiftB | DensityFunctionStructShiftedNoise | DensityFunctionStructSign | DensityFunctionStructSlice | DensityFunctionStructSlide | DensityFunctionStructSpline | DensityFunctionStructSqrt | DensityFunctionStructSquare | DensityFunctionStructSqueeze | DensityFunctionStructSub | DensityFunctionStructTerrainShaperSpline | DensityFunctionStructTruncate | DensityFunctionStructWeirdScaledSampler | DensityFunctionStructYClampedGradient

type DensityFunction = NoiseRange | DensityFunctionStruct


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::density_function::DensityFunction": {
        "kind": "union",
        "members": [
            {
                "kind": "reference",
                "path": "::java::data::worldgen::density_function::NoiseRange"
            },
            {
                "kind": "struct",
                "fields": [
                    {
                        "kind": "pair",
                        "key": "type",
                        "type": {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "worldgen/density_function_type"
                                        }
                                    }
                                }
                            ]
                        }
                    },
                    {
                        "kind": "spread",
                        "type": {
                            "kind": "dispatcher",
                            "parallelIndices": [
                                {
                                    "kind": "dynamic",
                                    "accessor": [
                                        "type"
                                    ]
                                }
                            ],
                            "registry": "minecraft:density_function"
                        }
                    }
                ]
            }
        ]
    }
}

