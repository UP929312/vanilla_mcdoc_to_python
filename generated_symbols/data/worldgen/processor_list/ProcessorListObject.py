"""
Generated from symbols.json for ::java::data::worldgen::processor_list::ProcessorListObject
Local link to file: generated_symbols/data/worldgen/processor_list/ProcessorListObject.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.processor_list.Processor import Processor


class ProcessorListObject(GeneratedModel):
    processors: list[Processor]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::processor_list::ProcessorListObject": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "processors",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::data::worldgen::processor_list::Processor"
                    }
                }
            }
        ]
    }
}

