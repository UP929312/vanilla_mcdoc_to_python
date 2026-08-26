"""
Generated from symbols.json for ::java::data::worldgen::density_function::DensityFunction
Local link to file: generated_symbols/data/worldgen/density_function/DensityFunction.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, ClassVar, Literal

from generated_symbols.data.worldgen.density_function.Clamp import Clamp
from generated_symbols.data.worldgen.density_function.Constant import Constant
from generated_symbols.data.worldgen.density_function.DistanceToPoint import DistanceToPoint
from generated_symbols.data.worldgen.density_function.FindTopSurface import FindTopSurface
from generated_symbols.data.worldgen.density_function.Gradient import Gradient
from generated_symbols.data.worldgen.density_function.Interpolated import Interpolated
from generated_symbols.data.worldgen.density_function.InvervalSelect import InvervalSelect
from generated_symbols.data.worldgen.density_function.Lerp import Lerp
from generated_symbols.data.worldgen.density_function.Noise import Noise
from generated_symbols.data.worldgen.density_function.OldBlendedNoise import OldBlendedNoise
from generated_symbols.data.worldgen.density_function.OneArgument import OneArgument
from generated_symbols.data.worldgen.density_function.Pow import Pow
from generated_symbols.data.worldgen.density_function.RangeChoice import RangeChoice
from generated_symbols.data.worldgen.density_function.Round import Round
from generated_symbols.data.worldgen.density_function.Shift import Shift
from generated_symbols.data.worldgen.density_function.Slice import Slice
from generated_symbols.data.worldgen.density_function.Spline import Spline
from generated_symbols.data.worldgen.density_function.TwoArguments import TwoArguments
from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.density_function.NoiseRange import NoiseRange


@dataclass(kw_only=True)
class DensityFunctionStructUnknown:
    __resource_dir__: ClassVar[str] = 'worldgen/density_function'

    type: Annotated[str, IdSpec(registry='worldgen/density_function_type')]


@dataclass(kw_only=True)
class DensityFunctionStructAbs(OneArgument):
    type: Literal['minecraft:abs'] = 'minecraft:abs'


@dataclass(kw_only=True)
class DensityFunctionStructAdd(TwoArguments):
    type: Literal['minecraft:add'] = 'minecraft:add'


@dataclass(kw_only=True)
class DensityFunctionStructBlendDensity(OneArgument):
    type: Literal['minecraft:blend_density'] = 'minecraft:blend_density'


@dataclass(kw_only=True)
class DensityFunctionStructCache(OneArgument):
    type: Literal['minecraft:cache'] = 'minecraft:cache'


@dataclass(kw_only=True)
class DensityFunctionStructCeil(Round):
    type: Literal['minecraft:ceil'] = 'minecraft:ceil'


@dataclass(kw_only=True)
class DensityFunctionStructClamp(Clamp):
    type: Literal['minecraft:clamp'] = 'minecraft:clamp'


@dataclass(kw_only=True)
class DensityFunctionStructConstant(Constant):
    type: Literal['minecraft:constant'] = 'minecraft:constant'


@dataclass(kw_only=True)
class DensityFunctionStructCube(OneArgument):
    type: Literal['minecraft:cube'] = 'minecraft:cube'


@dataclass(kw_only=True)
class DensityFunctionStructDistanceToPoint(DistanceToPoint):
    type: Literal['minecraft:distance_to_point'] = 'minecraft:distance_to_point'


@dataclass(kw_only=True)
class DensityFunctionStructDiv(TwoArguments):
    type: Literal['minecraft:div'] = 'minecraft:div'


@dataclass(kw_only=True)
class DensityFunctionStructFindTopSurface(FindTopSurface):
    type: Literal['minecraft:find_top_surface'] = 'minecraft:find_top_surface'


@dataclass(kw_only=True)
class DensityFunctionStructFloor(Round):
    type: Literal['minecraft:floor'] = 'minecraft:floor'


@dataclass(kw_only=True)
class DensityFunctionStructGradient(Gradient):
    type: Literal['minecraft:gradient'] = 'minecraft:gradient'


@dataclass(kw_only=True)
class DensityFunctionStructHalfNegative(OneArgument):
    type: Literal['minecraft:half_negative'] = 'minecraft:half_negative'


@dataclass(kw_only=True)
class DensityFunctionStructInterpolated(Interpolated):
    type: Literal['minecraft:interpolated'] = 'minecraft:interpolated'


@dataclass(kw_only=True)
class DensityFunctionStructIntervalSelect(InvervalSelect):
    type: Literal['minecraft:interval_select'] = 'minecraft:interval_select'


@dataclass(kw_only=True)
class DensityFunctionStructLerp(Lerp):
    type: Literal['minecraft:lerp'] = 'minecraft:lerp'


@dataclass(kw_only=True)
class DensityFunctionStructLog(OneArgument):
    type: Literal['minecraft:log'] = 'minecraft:log'


@dataclass(kw_only=True)
class DensityFunctionStructMax(TwoArguments):
    type: Literal['minecraft:max'] = 'minecraft:max'


@dataclass(kw_only=True)
class DensityFunctionStructMin(TwoArguments):
    type: Literal['minecraft:min'] = 'minecraft:min'


@dataclass(kw_only=True)
class DensityFunctionStructMul(TwoArguments):
    type: Literal['minecraft:mul'] = 'minecraft:mul'


@dataclass(kw_only=True)
class DensityFunctionStructNegate(OneArgument):
    type: Literal['minecraft:negate'] = 'minecraft:negate'


@dataclass(kw_only=True)
class DensityFunctionStructNoise(Noise):
    type: Literal['minecraft:noise'] = 'minecraft:noise'


@dataclass(kw_only=True)
class DensityFunctionStructOldBlendedNoise(OldBlendedNoise):
    type: Literal['minecraft:old_blended_noise'] = 'minecraft:old_blended_noise'


@dataclass(kw_only=True)
class DensityFunctionStructPow(Pow):
    type: Literal['minecraft:pow'] = 'minecraft:pow'


@dataclass(kw_only=True)
class DensityFunctionStructQuarterNegative(OneArgument):
    type: Literal['minecraft:quarter_negative'] = 'minecraft:quarter_negative'


@dataclass(kw_only=True)
class DensityFunctionStructRangeChoice(RangeChoice):
    type: Literal['minecraft:range_choice'] = 'minecraft:range_choice'


@dataclass(kw_only=True)
class DensityFunctionStructReciprocal(OneArgument):
    type: Literal['minecraft:reciprocal'] = 'minecraft:reciprocal'


@dataclass(kw_only=True)
class DensityFunctionStructRound(Round):
    type: Literal['minecraft:round'] = 'minecraft:round'


@dataclass(kw_only=True)
class DensityFunctionStructShift(Shift):
    type: Literal['minecraft:shift'] = 'minecraft:shift'


@dataclass(kw_only=True)
class DensityFunctionStructShiftA(Shift):
    type: Literal['minecraft:shift_a'] = 'minecraft:shift_a'


@dataclass(kw_only=True)
class DensityFunctionStructShiftB(Shift):
    type: Literal['minecraft:shift_b'] = 'minecraft:shift_b'


@dataclass(kw_only=True)
class DensityFunctionStructSign(OneArgument):
    type: Literal['minecraft:sign'] = 'minecraft:sign'


@dataclass(kw_only=True)
class DensityFunctionStructSlice(Slice):
    type: Literal['minecraft:slice'] = 'minecraft:slice'


@dataclass(kw_only=True)
class DensityFunctionStructSlide(OneArgument):
    type: Literal['minecraft:slide'] = 'minecraft:slide'


@dataclass(kw_only=True)
class DensityFunctionStructSpline(Spline):
    type: Literal['minecraft:spline'] = 'minecraft:spline'


@dataclass(kw_only=True)
class DensityFunctionStructSqrt(OneArgument):
    type: Literal['minecraft:sqrt'] = 'minecraft:sqrt'


@dataclass(kw_only=True)
class DensityFunctionStructSquare(OneArgument):
    type: Literal['minecraft:square'] = 'minecraft:square'


@dataclass(kw_only=True)
class DensityFunctionStructSqueeze(OneArgument):
    type: Literal['minecraft:squeeze'] = 'minecraft:squeeze'


@dataclass(kw_only=True)
class DensityFunctionStructSub(TwoArguments):
    type: Literal['minecraft:sub'] = 'minecraft:sub'


@dataclass(kw_only=True)
class DensityFunctionStructTruncate(Round):
    type: Literal['minecraft:truncate'] = 'minecraft:truncate'


type DensityFunctionStruct = DensityFunctionStructUnknown | DensityFunctionStructAbs | DensityFunctionStructAdd | DensityFunctionStructBlendDensity | DensityFunctionStructCache | DensityFunctionStructCeil | DensityFunctionStructClamp | DensityFunctionStructConstant | DensityFunctionStructCube | DensityFunctionStructDistanceToPoint | DensityFunctionStructDiv | DensityFunctionStructFindTopSurface | DensityFunctionStructFloor | DensityFunctionStructGradient | DensityFunctionStructHalfNegative | DensityFunctionStructInterpolated | DensityFunctionStructIntervalSelect | DensityFunctionStructLerp | DensityFunctionStructLog | DensityFunctionStructMax | DensityFunctionStructMin | DensityFunctionStructMul | DensityFunctionStructNegate | DensityFunctionStructNoise | DensityFunctionStructOldBlendedNoise | DensityFunctionStructPow | DensityFunctionStructQuarterNegative | DensityFunctionStructRangeChoice | DensityFunctionStructReciprocal | DensityFunctionStructRound | DensityFunctionStructShift | DensityFunctionStructShiftA | DensityFunctionStructShiftB | DensityFunctionStructSign | DensityFunctionStructSlice | DensityFunctionStructSlide | DensityFunctionStructSpline | DensityFunctionStructSqrt | DensityFunctionStructSquare | DensityFunctionStructSqueeze | DensityFunctionStructSub | DensityFunctionStructTruncate

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

