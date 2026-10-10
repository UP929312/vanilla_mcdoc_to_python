"""
Generated from symbols.json for ::java::data::worldgen::processor_list::Capped
Local link to file: generated_symbols/data/worldgen/processor_list/Capped.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.IntProvider import IntProvider
    from generated_symbols.data.worldgen.processor_list.Processor import Processor


class Capped(GeneratedModel):
    delegate: Processor
    limit: IntProvider[Annotated[int, Field(ge=0)]] | Annotated[int, Field(ge=0)]


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
