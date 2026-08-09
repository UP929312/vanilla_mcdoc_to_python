# Generated from symbols.json for ::java::data::worldgen::processor_list::ProcessorListRef
from typing import TYPE_CHECKING, Annotated

from runtime_metadata import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.processor_list.ProcessorList import ProcessorList


type ProcessorListRef = Annotated[str, IdSpec(registry='worldgen/processor_list')] | ProcessorList


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::processor_list::ProcessorListRef": {
        "kind": "union",
        "members": [
            {
                "kind": "string",
                "attributes": [
                    {
                        "name": "id",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "worldgen/processor_list"
                            }
                        }
                    }
                ]
            },
            {
                "kind": "reference",
                "path": "::java::data::worldgen::processor_list::ProcessorList"
            }
        ]
    }
}

