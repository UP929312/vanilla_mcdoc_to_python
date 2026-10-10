"""
Generated from symbols.json for ::java::data::worldgen::processor_list::AxisAlignedLinearPos
Local link to file: vanilla_mcdoc/data/worldgen/processor_list/AxisAlignedLinearPos.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.data.worldgen.processor_list.LinearPos import LinearPos

if TYPE_CHECKING:
    from vanilla_mcdoc.util.direction.Axis import Axis


class AxisAlignedLinearPos(LinearPos):
    axis: Axis
