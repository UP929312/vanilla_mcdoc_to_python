# Generated from symbols.json for ::java::data::worldgen::processor_list::Capped
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.IntProvider import IntProvider
    from generated_symbols.data.worldgen.processor_list.Processor import Processor


@dataclass(kw_only=True)
class Capped:
    delegate: Processor
    limit: IntProvider[Annotated[int, 'Range | Min `0` and above | inclusive']] | Annotated[int, 'Range | Min `0` and above | inclusive']


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::processor_list::Capped": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "delegate",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::processor_list::Processor"
                }
            },
            {
                "kind": "pair",
                "key": "limit",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::data::worldgen::IntProvider"
                    },
                    "typeArgs": [
                        {
                            "kind": "int",
                            "valueRange": {
                                "kind": 0,
                                "min": 0
                            }
                        }
                    ]
                }
            }
        ]
    }
}

