"""
Generated from symbols.json for ::java::data::worldgen::processor_list::ProcessorListRef
Local link to file: vanilla_mcdoc/data/worldgen/processor_list/ProcessorListRef.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.processor_list.ProcessorList import ProcessorList


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
