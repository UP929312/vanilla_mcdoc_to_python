"""
Generated from symbols.json for ::java::data::worldgen::processor_list::ProcessorList
Local link to file: vanilla_mcdoc/data/worldgen/processor_list/ProcessorList.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.processor_list.Processor import Processor


class ProcessorListStruct(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/processor_list'

    processors: list[Processor]


type ProcessorList = list[Processor] | ProcessorListStruct
