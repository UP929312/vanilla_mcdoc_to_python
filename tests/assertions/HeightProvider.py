# ~~~ WHAT ARE WE TESTING ~~~

# Dispatcher spread branches retain their correlated selector value and fields.

# ~~~ FILE CONTENT ~~~
"""
Generated from symbols.json for ::java::data::worldgen::HeightProvider
Local link to file: generated_symbols/data/worldgen/HeightProvider.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Literal

from generated_symbols.data.worldgen.UniformHeightProvider import UniformHeightProvider

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.VerticalAnchor import VerticalAnchor
    from generated_symbols.util.NonEmptyWeightedList import NonEmptyWeightedList


@dataclass(kw_only=True)
class HeightProviderStructBiasedToBottom(UniformHeightProvider):
    type: Literal['minecraft:biased_to_bottom']
    inner: Annotated[int, 'Range | `1` and above | inclusive'] | None = None


@dataclass(kw_only=True)
class HeightProviderStructConstant:
    type: Literal['minecraft:constant']
    value: VerticalAnchor


@dataclass(kw_only=True)
class HeightProviderStructTrapezoid(UniformHeightProvider):
    type: Literal['minecraft:trapezoid']
    plateau: int | None = None


@dataclass(kw_only=True)
class HeightProviderStructUniform:
    type: Literal['minecraft:uniform']
    min_inclusive: VerticalAnchor
    max_inclusive: VerticalAnchor


@dataclass(kw_only=True)
class HeightProviderStructVeryBiasedToBottom(UniformHeightProvider):
    type: Literal['minecraft:very_biased_to_bottom']
    inner: Annotated[int, 'Range | `1` and above | inclusive'] | None = None


@dataclass(kw_only=True)
class HeightProviderStructWeightedList:
    type: Literal['minecraft:weighted_list']
    distribution: NonEmptyWeightedList[HeightProvider]


type HeightProviderStruct = HeightProviderStructBiasedToBottom | HeightProviderStructConstant | HeightProviderStructTrapezoid | HeightProviderStructUniform | HeightProviderStructVeryBiasedToBottom | HeightProviderStructWeightedList

type HeightProvider = HeightProviderStruct | VerticalAnchor
