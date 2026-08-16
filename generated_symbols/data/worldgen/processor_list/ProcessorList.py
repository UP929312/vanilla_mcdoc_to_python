"""
Generated from symbols.json for ::java::data::worldgen::processor_list::ProcessorList
Local link to file: generated_symbols/data/worldgen/processor_list/ProcessorList.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.processor_list.Processor import Processor


@dataclass(kw_only=True)
class ProcessorListStruct:
    __resource_dir__: ClassVar[str] = 'worldgen/processor_list'

    processors: list[Processor]


type ProcessorList = list[Processor] | ProcessorListStruct


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::processor_list::ProcessorList": {
        "kind": "union",
        "members": [
            {
                "kind": "list",
                "item": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::processor_list::Processor"
                }
            },
            {
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
        ]
    }
}

