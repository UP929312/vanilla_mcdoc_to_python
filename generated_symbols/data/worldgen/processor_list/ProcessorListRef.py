# Generated from symbols.json for ::java::data::worldgen::processor_list::ProcessorListRef
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.processor_list.ProcessorList import ProcessorList


type ProcessorListRef = str | ProcessorList


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

