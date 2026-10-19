"""
Generated from symbols.json for ::java::data::worldgen::density_function::DensityFunction
Local link to file: vanilla_mcdoc/data/worldgen/density_function/DensityFunction.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar, Literal

from pydantic import Discriminator, Tag

from vanilla_mcdoc.base import GeneratedModel, tag_of
from vanilla_mcdoc.data.worldgen.density_function.Clamp import Clamp
from vanilla_mcdoc.data.worldgen.density_function.Constant import Constant
from vanilla_mcdoc.data.worldgen.density_function.DistanceToPoint import DistanceToPoint
from vanilla_mcdoc.data.worldgen.density_function.FindTopSurface import FindTopSurface
from vanilla_mcdoc.data.worldgen.density_function.Gradient import Gradient
from vanilla_mcdoc.data.worldgen.density_function.Interpolated import Interpolated
from vanilla_mcdoc.data.worldgen.density_function.InvervalSelect import InvervalSelect
from vanilla_mcdoc.data.worldgen.density_function.Lerp import Lerp
from vanilla_mcdoc.data.worldgen.density_function.Noise import Noise
from vanilla_mcdoc.data.worldgen.density_function.OldBlendedNoise import OldBlendedNoise
from vanilla_mcdoc.data.worldgen.density_function.OneArgument import OneArgument
from vanilla_mcdoc.data.worldgen.density_function.Pow import Pow
from vanilla_mcdoc.data.worldgen.density_function.RangeChoice import RangeChoice
from vanilla_mcdoc.data.worldgen.density_function.Round import Round
from vanilla_mcdoc.data.worldgen.density_function.Shift import Shift
from vanilla_mcdoc.data.worldgen.density_function.Slice import Slice
from vanilla_mcdoc.data.worldgen.density_function.Spline import Spline
from vanilla_mcdoc.data.worldgen.density_function.TwoArguments import TwoArguments

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.density_function.NoiseRange import NoiseRange


class DensityFunctionStructAbs(OneArgument):
    __resource_dir__: ClassVar[str] = 'worldgen/density_function'

    type: Literal['minecraft:abs', 'abs'] = 'minecraft:abs'


class DensityFunctionStructAdd(TwoArguments):
    __resource_dir__: ClassVar[str] = 'worldgen/density_function'

    type: Literal['minecraft:add', 'add'] = 'minecraft:add'


class DensityFunctionStructBlendDensity(OneArgument):
    __resource_dir__: ClassVar[str] = 'worldgen/density_function'

    type: Literal['minecraft:blend_density', 'blend_density'] = 'minecraft:blend_density'


class DensityFunctionStructCache(OneArgument):
    __resource_dir__: ClassVar[str] = 'worldgen/density_function'

    type: Literal['minecraft:cache', 'cache'] = 'minecraft:cache'


class DensityFunctionStructCeil(Round):
    __resource_dir__: ClassVar[str] = 'worldgen/density_function'

    type: Literal['minecraft:ceil', 'ceil'] = 'minecraft:ceil'


class DensityFunctionStructClamp(Clamp):
    __resource_dir__: ClassVar[str] = 'worldgen/density_function'

    type: Literal['minecraft:clamp', 'clamp'] = 'minecraft:clamp'


class DensityFunctionStructConstant(Constant):
    __resource_dir__: ClassVar[str] = 'worldgen/density_function'

    type: Literal['minecraft:constant', 'constant'] = 'minecraft:constant'


class DensityFunctionStructCube(OneArgument):
    __resource_dir__: ClassVar[str] = 'worldgen/density_function'

    type: Literal['minecraft:cube', 'cube'] = 'minecraft:cube'


class DensityFunctionStructDistanceToPoint(DistanceToPoint):
    __resource_dir__: ClassVar[str] = 'worldgen/density_function'

    type: Literal['minecraft:distance_to_point', 'distance_to_point'] = 'minecraft:distance_to_point'


class DensityFunctionStructDiv(TwoArguments):
    __resource_dir__: ClassVar[str] = 'worldgen/density_function'

    type: Literal['minecraft:div', 'div'] = 'minecraft:div'


class DensityFunctionStructFindTopSurface(FindTopSurface):
    __resource_dir__: ClassVar[str] = 'worldgen/density_function'

    type: Literal['minecraft:find_top_surface', 'find_top_surface'] = 'minecraft:find_top_surface'


class DensityFunctionStructFloor(Round):
    __resource_dir__: ClassVar[str] = 'worldgen/density_function'

    type: Literal['minecraft:floor', 'floor'] = 'minecraft:floor'


class DensityFunctionStructGradient(Gradient):
    __resource_dir__: ClassVar[str] = 'worldgen/density_function'

    type: Literal['minecraft:gradient', 'gradient'] = 'minecraft:gradient'


class DensityFunctionStructHalfNegative(OneArgument):
    __resource_dir__: ClassVar[str] = 'worldgen/density_function'

    type: Literal['minecraft:half_negative', 'half_negative'] = 'minecraft:half_negative'


class DensityFunctionStructInterpolated(Interpolated):
    __resource_dir__: ClassVar[str] = 'worldgen/density_function'

    type: Literal['minecraft:interpolated', 'interpolated'] = 'minecraft:interpolated'


class DensityFunctionStructIntervalSelect(InvervalSelect):
    __resource_dir__: ClassVar[str] = 'worldgen/density_function'

    type: Literal['minecraft:interval_select', 'interval_select'] = 'minecraft:interval_select'


class DensityFunctionStructLerp(Lerp):
    __resource_dir__: ClassVar[str] = 'worldgen/density_function'

    type: Literal['minecraft:lerp', 'lerp'] = 'minecraft:lerp'


class DensityFunctionStructLog(OneArgument):
    __resource_dir__: ClassVar[str] = 'worldgen/density_function'

    type: Literal['minecraft:log', 'log'] = 'minecraft:log'


class DensityFunctionStructMax(TwoArguments):
    __resource_dir__: ClassVar[str] = 'worldgen/density_function'

    type: Literal['minecraft:max', 'max'] = 'minecraft:max'


class DensityFunctionStructMin(TwoArguments):
    __resource_dir__: ClassVar[str] = 'worldgen/density_function'

    type: Literal['minecraft:min', 'min'] = 'minecraft:min'


class DensityFunctionStructMul(TwoArguments):
    __resource_dir__: ClassVar[str] = 'worldgen/density_function'

    type: Literal['minecraft:mul', 'mul'] = 'minecraft:mul'


class DensityFunctionStructNegate(OneArgument):
    __resource_dir__: ClassVar[str] = 'worldgen/density_function'

    type: Literal['minecraft:negate', 'negate'] = 'minecraft:negate'


class DensityFunctionStructNoise(Noise):
    __resource_dir__: ClassVar[str] = 'worldgen/density_function'

    type: Literal['minecraft:noise', 'noise'] = 'minecraft:noise'


class DensityFunctionStructOldBlendedNoise(OldBlendedNoise):
    __resource_dir__: ClassVar[str] = 'worldgen/density_function'

    type: Literal['minecraft:old_blended_noise', 'old_blended_noise'] = 'minecraft:old_blended_noise'


class DensityFunctionStructPow(Pow):
    __resource_dir__: ClassVar[str] = 'worldgen/density_function'

    type: Literal['minecraft:pow', 'pow'] = 'minecraft:pow'


class DensityFunctionStructQuarterNegative(OneArgument):
    __resource_dir__: ClassVar[str] = 'worldgen/density_function'

    type: Literal['minecraft:quarter_negative', 'quarter_negative'] = 'minecraft:quarter_negative'


class DensityFunctionStructRangeChoice(RangeChoice):
    __resource_dir__: ClassVar[str] = 'worldgen/density_function'

    type: Literal['minecraft:range_choice', 'range_choice'] = 'minecraft:range_choice'


class DensityFunctionStructReciprocal(OneArgument):
    __resource_dir__: ClassVar[str] = 'worldgen/density_function'

    type: Literal['minecraft:reciprocal', 'reciprocal'] = 'minecraft:reciprocal'


class DensityFunctionStructRound(Round):
    __resource_dir__: ClassVar[str] = 'worldgen/density_function'

    type: Literal['minecraft:round', 'round'] = 'minecraft:round'


class DensityFunctionStructShift(Shift):
    __resource_dir__: ClassVar[str] = 'worldgen/density_function'

    type: Literal['minecraft:shift', 'shift'] = 'minecraft:shift'


class DensityFunctionStructShiftA(Shift):
    __resource_dir__: ClassVar[str] = 'worldgen/density_function'

    type: Literal['minecraft:shift_a', 'shift_a'] = 'minecraft:shift_a'


class DensityFunctionStructShiftB(Shift):
    __resource_dir__: ClassVar[str] = 'worldgen/density_function'

    type: Literal['minecraft:shift_b', 'shift_b'] = 'minecraft:shift_b'


class DensityFunctionStructSign(OneArgument):
    __resource_dir__: ClassVar[str] = 'worldgen/density_function'

    type: Literal['minecraft:sign', 'sign'] = 'minecraft:sign'


class DensityFunctionStructSlice(Slice):
    __resource_dir__: ClassVar[str] = 'worldgen/density_function'

    type: Literal['minecraft:slice', 'slice'] = 'minecraft:slice'


class DensityFunctionStructSlide(OneArgument):
    __resource_dir__: ClassVar[str] = 'worldgen/density_function'

    type: Literal['minecraft:slide', 'slide'] = 'minecraft:slide'


class DensityFunctionStructSpline(Spline):
    __resource_dir__: ClassVar[str] = 'worldgen/density_function'

    type: Literal['minecraft:spline', 'spline'] = 'minecraft:spline'


class DensityFunctionStructSqrt(OneArgument):
    __resource_dir__: ClassVar[str] = 'worldgen/density_function'

    type: Literal['minecraft:sqrt', 'sqrt'] = 'minecraft:sqrt'


class DensityFunctionStructSquare(OneArgument):
    __resource_dir__: ClassVar[str] = 'worldgen/density_function'

    type: Literal['minecraft:square', 'square'] = 'minecraft:square'


class DensityFunctionStructSqueeze(OneArgument):
    __resource_dir__: ClassVar[str] = 'worldgen/density_function'

    type: Literal['minecraft:squeeze', 'squeeze'] = 'minecraft:squeeze'


class DensityFunctionStructSub(TwoArguments):
    __resource_dir__: ClassVar[str] = 'worldgen/density_function'

    type: Literal['minecraft:sub', 'sub'] = 'minecraft:sub'


class DensityFunctionStructTruncate(Round):
    __resource_dir__: ClassVar[str] = 'worldgen/density_function'

    type: Literal['minecraft:truncate', 'truncate'] = 'minecraft:truncate'


class DensityFunctionStructBeardifier(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/density_function'

    type: Literal['minecraft:beardifier', 'beardifier'] = 'minecraft:beardifier'


class DensityFunctionStructBlendAlpha(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/density_function'

    type: Literal['minecraft:blend_alpha', 'blend_alpha'] = 'minecraft:blend_alpha'


class DensityFunctionStructBlendOffset(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/density_function'

    type: Literal['minecraft:blend_offset', 'blend_offset'] = 'minecraft:blend_offset'


class DensityFunctionStructEndOuterIslands(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/density_function'

    type: Literal['minecraft:end_outer_islands', 'end_outer_islands'] = 'minecraft:end_outer_islands'


type DensityFunctionStruct = Annotated[
    Annotated[DensityFunctionStructAbs, Tag('minecraft:abs')]
    | Annotated[DensityFunctionStructAdd, Tag('minecraft:add')]
    | Annotated[DensityFunctionStructBlendDensity, Tag('minecraft:blend_density')]
    | Annotated[DensityFunctionStructCache, Tag('minecraft:cache')]
    | Annotated[DensityFunctionStructCeil, Tag('minecraft:ceil')]
    | Annotated[DensityFunctionStructClamp, Tag('minecraft:clamp')]
    | Annotated[DensityFunctionStructConstant, Tag('minecraft:constant')]
    | Annotated[DensityFunctionStructCube, Tag('minecraft:cube')]
    | Annotated[DensityFunctionStructDistanceToPoint, Tag('minecraft:distance_to_point')]
    | Annotated[DensityFunctionStructDiv, Tag('minecraft:div')]
    | Annotated[DensityFunctionStructFindTopSurface, Tag('minecraft:find_top_surface')]
    | Annotated[DensityFunctionStructFloor, Tag('minecraft:floor')]
    | Annotated[DensityFunctionStructGradient, Tag('minecraft:gradient')]
    | Annotated[DensityFunctionStructHalfNegative, Tag('minecraft:half_negative')]
    | Annotated[DensityFunctionStructInterpolated, Tag('minecraft:interpolated')]
    | Annotated[DensityFunctionStructIntervalSelect, Tag('minecraft:interval_select')]
    | Annotated[DensityFunctionStructLerp, Tag('minecraft:lerp')]
    | Annotated[DensityFunctionStructLog, Tag('minecraft:log')]
    | Annotated[DensityFunctionStructMax, Tag('minecraft:max')]
    | Annotated[DensityFunctionStructMin, Tag('minecraft:min')]
    | Annotated[DensityFunctionStructMul, Tag('minecraft:mul')]
    | Annotated[DensityFunctionStructNegate, Tag('minecraft:negate')]
    | Annotated[DensityFunctionStructNoise, Tag('minecraft:noise')]
    | Annotated[DensityFunctionStructOldBlendedNoise, Tag('minecraft:old_blended_noise')]
    | Annotated[DensityFunctionStructPow, Tag('minecraft:pow')]
    | Annotated[DensityFunctionStructQuarterNegative, Tag('minecraft:quarter_negative')]
    | Annotated[DensityFunctionStructRangeChoice, Tag('minecraft:range_choice')]
    | Annotated[DensityFunctionStructReciprocal, Tag('minecraft:reciprocal')]
    | Annotated[DensityFunctionStructRound, Tag('minecraft:round')]
    | Annotated[DensityFunctionStructShift, Tag('minecraft:shift')]
    | Annotated[DensityFunctionStructShiftA, Tag('minecraft:shift_a')]
    | Annotated[DensityFunctionStructShiftB, Tag('minecraft:shift_b')]
    | Annotated[DensityFunctionStructSign, Tag('minecraft:sign')]
    | Annotated[DensityFunctionStructSlice, Tag('minecraft:slice')]
    | Annotated[DensityFunctionStructSlide, Tag('minecraft:slide')]
    | Annotated[DensityFunctionStructSpline, Tag('minecraft:spline')]
    | Annotated[DensityFunctionStructSqrt, Tag('minecraft:sqrt')]
    | Annotated[DensityFunctionStructSquare, Tag('minecraft:square')]
    | Annotated[DensityFunctionStructSqueeze, Tag('minecraft:squeeze')]
    | Annotated[DensityFunctionStructSub, Tag('minecraft:sub')]
    | Annotated[DensityFunctionStructTruncate, Tag('minecraft:truncate')]
    | Annotated[DensityFunctionStructBeardifier, Tag('minecraft:beardifier')]
    | Annotated[DensityFunctionStructBlendAlpha, Tag('minecraft:blend_alpha')]
    | Annotated[DensityFunctionStructBlendOffset, Tag('minecraft:blend_offset')]
    | Annotated[DensityFunctionStructEndOuterIslands, Tag('minecraft:end_outer_islands')],
    Discriminator(tag_of('type')),
]


type DensityFunction = NoiseRange | DensityFunctionStruct
