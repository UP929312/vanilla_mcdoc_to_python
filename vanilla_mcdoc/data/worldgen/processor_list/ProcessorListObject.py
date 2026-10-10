"""
Generated from symbols.json for ::java::data::worldgen::processor_list::ProcessorListObject
Local link to file: vanilla_mcdoc/data/worldgen/processor_list/ProcessorListObject.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.processor_list.Processor import Processor


class ProcessorListObject(GeneratedModel):
    processors: list[Processor]
