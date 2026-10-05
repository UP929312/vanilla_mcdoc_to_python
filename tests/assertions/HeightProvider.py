# ~~~ WHAT ARE WE TESTING ~~~

# Dispatcher spread branches retain their correlated selector value and fields.

# ~~~ FILE CONTENT ~~~
"""
Generated from symbols.json for ::java::data::worldgen::HeightProvider
Local link to file: generated_symbols/data/worldgen/HeightProvider.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, Literal

from generated_symbols.data.worldgen.BottomBiasHeightProvider import BottomBiasHeightProvider
from generated_symbols.data.worldgen.ConstantHeightProvider import ConstantHeightProvider
from generated_symbols.data.worldgen.TrapezoidHeightProvider import TrapezoidHeightProvider
from generated_symbols.data.worldgen.UniformHeightProvider import UniformHeightProvider
from generated_symbols.data.worldgen.WeightListHeightProvider import WeightListHeightProvider
from pydantic import Field

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.VerticalAnchor import VerticalAnchor


class HeightProviderStructBiasedToBottom(BottomBiasHeightProvider):
    type: Literal['minecraft:biased_to_bottom'] = 'minecraft:biased_to_bottom'


class HeightProviderStructConstant(ConstantHeightProvider):
    type: Literal['minecraft:constant'] = 'minecraft:constant'


class HeightProviderStructTrapezoid(TrapezoidHeightProvider):
    type: Literal['minecraft:trapezoid'] = 'minecraft:trapezoid'


class HeightProviderStructUniform(UniformHeightProvider):
    type: Literal['minecraft:uniform'] = 'minecraft:uniform'


class HeightProviderStructVeryBiasedToBottom(BottomBiasHeightProvider):
    type: Literal['minecraft:very_biased_to_bottom'] = 'minecraft:very_biased_to_bottom'


class HeightProviderStructWeightedList(WeightListHeightProvider):
    type: Literal['minecraft:weighted_list'] = 'minecraft:weighted_list'


type HeightProviderStruct = Annotated[
    HeightProviderStructBiasedToBottom | HeightProviderStructConstant | HeightProviderStructTrapezoid | HeightProviderStructUniform | HeightProviderStructVeryBiasedToBottom | HeightProviderStructWeightedList,
    Field(discriminator='type'),
]

type HeightProvider = HeightProviderStruct | VerticalAnchor
