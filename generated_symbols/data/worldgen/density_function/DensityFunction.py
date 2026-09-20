"""
Generated from symbols.json for ::java::data::worldgen::density_function::DensityFunction
Local link to file: generated_symbols/data/worldgen/density_function/DensityFunction.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar, Literal

from generated_symbols.base import GeneratedModel
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


class DensityFunctionStructUnknown(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/density_function'

    type: Annotated[str, IdSpec(registry='worldgen/density_function_type')]


class DensityFunctionStructAbs(OneArgument):
    type: Literal['minecraft:abs'] = 'minecraft:abs'


class DensityFunctionStructAdd(TwoArguments):
    type: Literal['minecraft:add'] = 'minecraft:add'


class DensityFunctionStructBlendDensity(OneArgument):
    type: Literal['minecraft:blend_density'] = 'minecraft:blend_density'


class DensityFunctionStructCache(OneArgument):
    type: Literal['minecraft:cache'] = 'minecraft:cache'


class DensityFunctionStructCeil(Round):
    type: Literal['minecraft:ceil'] = 'minecraft:ceil'


class DensityFunctionStructClamp(Clamp):
    type: Literal['minecraft:clamp'] = 'minecraft:clamp'


class DensityFunctionStructConstant(Constant):
    type: Literal['minecraft:constant'] = 'minecraft:constant'


class DensityFunctionStructCube(OneArgument):
    type: Literal['minecraft:cube'] = 'minecraft:cube'


class DensityFunctionStructDistanceToPoint(DistanceToPoint):
    type: Literal['minecraft:distance_to_point'] = 'minecraft:distance_to_point'


class DensityFunctionStructDiv(TwoArguments):
    type: Literal['minecraft:div'] = 'minecraft:div'


class DensityFunctionStructFindTopSurface(FindTopSurface):
    type: Literal['minecraft:find_top_surface'] = 'minecraft:find_top_surface'


class DensityFunctionStructFloor(Round):
    type: Literal['minecraft:floor'] = 'minecraft:floor'


class DensityFunctionStructGradient(Gradient):
    type: Literal['minecraft:gradient'] = 'minecraft:gradient'


class DensityFunctionStructHalfNegative(OneArgument):
    type: Literal['minecraft:half_negative'] = 'minecraft:half_negative'


class DensityFunctionStructInterpolated(Interpolated):
    type: Literal['minecraft:interpolated'] = 'minecraft:interpolated'


class DensityFunctionStructIntervalSelect(InvervalSelect):
    type: Literal['minecraft:interval_select'] = 'minecraft:interval_select'


class DensityFunctionStructLerp(Lerp):
    type: Literal['minecraft:lerp'] = 'minecraft:lerp'


class DensityFunctionStructLog(OneArgument):
    type: Literal['minecraft:log'] = 'minecraft:log'


class DensityFunctionStructMax(TwoArguments):
    type: Literal['minecraft:max'] = 'minecraft:max'


class DensityFunctionStructMin(TwoArguments):
    type: Literal['minecraft:min'] = 'minecraft:min'


class DensityFunctionStructMul(TwoArguments):
    type: Literal['minecraft:mul'] = 'minecraft:mul'


class DensityFunctionStructNegate(OneArgument):
    type: Literal['minecraft:negate'] = 'minecraft:negate'


class DensityFunctionStructNoise(Noise):
    type: Literal['minecraft:noise'] = 'minecraft:noise'


class DensityFunctionStructOldBlendedNoise(OldBlendedNoise):
    type: Literal['minecraft:old_blended_noise'] = 'minecraft:old_blended_noise'


class DensityFunctionStructPow(Pow):
    type: Literal['minecraft:pow'] = 'minecraft:pow'


class DensityFunctionStructQuarterNegative(OneArgument):
    type: Literal['minecraft:quarter_negative'] = 'minecraft:quarter_negative'


class DensityFunctionStructRangeChoice(RangeChoice):
    type: Literal['minecraft:range_choice'] = 'minecraft:range_choice'


class DensityFunctionStructReciprocal(OneArgument):
    type: Literal['minecraft:reciprocal'] = 'minecraft:reciprocal'


class DensityFunctionStructRound(Round):
    type: Literal['minecraft:round'] = 'minecraft:round'


class DensityFunctionStructShift(Shift):
    type: Literal['minecraft:shift'] = 'minecraft:shift'


class DensityFunctionStructShiftA(Shift):
    type: Literal['minecraft:shift_a'] = 'minecraft:shift_a'


class DensityFunctionStructShiftB(Shift):
    type: Literal['minecraft:shift_b'] = 'minecraft:shift_b'


class DensityFunctionStructSign(OneArgument):
    type: Literal['minecraft:sign'] = 'minecraft:sign'


class DensityFunctionStructSlice(Slice):
    type: Literal['minecraft:slice'] = 'minecraft:slice'


class DensityFunctionStructSlide(OneArgument):
    type: Literal['minecraft:slide'] = 'minecraft:slide'


class DensityFunctionStructSpline(Spline):
    type: Literal['minecraft:spline'] = 'minecraft:spline'


class DensityFunctionStructSqrt(OneArgument):
    type: Literal['minecraft:sqrt'] = 'minecraft:sqrt'


class DensityFunctionStructSquare(OneArgument):
    type: Literal['minecraft:square'] = 'minecraft:square'


class DensityFunctionStructSqueeze(OneArgument):
    type: Literal['minecraft:squeeze'] = 'minecraft:squeeze'


class DensityFunctionStructSub(TwoArguments):
    type: Literal['minecraft:sub'] = 'minecraft:sub'


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

