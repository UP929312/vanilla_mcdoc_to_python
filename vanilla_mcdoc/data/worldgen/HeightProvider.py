"""
Generated from symbols.json for ::java::data::worldgen::HeightProvider
Local link to file: vanilla_mcdoc/data/worldgen/HeightProvider.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, Literal

from pydantic import Field

from vanilla_mcdoc.data.worldgen.BottomBiasHeightProvider import BottomBiasHeightProvider
from vanilla_mcdoc.data.worldgen.ConstantHeightProvider import ConstantHeightProvider
from vanilla_mcdoc.data.worldgen.TrapezoidHeightProvider import TrapezoidHeightProvider
from vanilla_mcdoc.data.worldgen.UniformHeightProvider import UniformHeightProvider
from vanilla_mcdoc.data.worldgen.WeightListHeightProvider import WeightListHeightProvider

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.VerticalAnchor import VerticalAnchor


class HeightProviderStructBiasedToBottom(BottomBiasHeightProvider):
    type: Literal['minecraft:biased_to_bottom', 'biased_to_bottom'] = 'minecraft:biased_to_bottom'


class HeightProviderStructConstant(ConstantHeightProvider):
    type: Literal['minecraft:constant', 'constant'] = 'minecraft:constant'


class HeightProviderStructTrapezoid(TrapezoidHeightProvider):
    type: Literal['minecraft:trapezoid', 'trapezoid'] = 'minecraft:trapezoid'


class HeightProviderStructUniform(UniformHeightProvider):
    type: Literal['minecraft:uniform', 'uniform'] = 'minecraft:uniform'


class HeightProviderStructVeryBiasedToBottom(BottomBiasHeightProvider):
    type: Literal['minecraft:very_biased_to_bottom', 'very_biased_to_bottom'] = 'minecraft:very_biased_to_bottom'


class HeightProviderStructWeightedList(WeightListHeightProvider):
    type: Literal['minecraft:weighted_list', 'weighted_list'] = 'minecraft:weighted_list'


type HeightProviderStruct = Annotated[
    HeightProviderStructBiasedToBottom | HeightProviderStructConstant | HeightProviderStructTrapezoid | HeightProviderStructUniform | HeightProviderStructVeryBiasedToBottom | HeightProviderStructWeightedList,
    Field(discriminator='type'),
]


type HeightProvider = HeightProviderStruct | VerticalAnchor
