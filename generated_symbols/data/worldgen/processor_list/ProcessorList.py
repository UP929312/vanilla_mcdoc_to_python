# Generated from symbols.json for ::java::data::worldgen::processor_list::ProcessorList
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.processor_list.Processor import Processor


@dataclass(kw_only=True)
class ProcessorListStruct1:
    processors: list[Processor]

type ProcessorList = list[Processor] | ProcessorListStruct1


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

