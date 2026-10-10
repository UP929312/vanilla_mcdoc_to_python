"""
Generated from symbols.json for ::java::data::worldgen::template_pool::SingleElement
Local link to file: vanilla_mcdoc/data/worldgen/template_pool/SingleElement.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.data.worldgen.template_pool.ElementBase import ElementBase
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.processor_list.ProcessorListRef import ProcessorListRef
    from vanilla_mcdoc.data.worldgen.structure.LiquidSettings import LiquidSettings


class SingleElement(ElementBase):
    location: Annotated[str, IdSpec(registry='structure')]
    processors: ProcessorListRef
    override_liquid_settings: LiquidSettings | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::template_pool::SingleElement": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::template_pool::ElementBase"
                }
            },
            {
                "kind": "pair",
                "key": "location",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "structure"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "processors",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::processor_list::ProcessorListRef"
                }
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21"
                            }
                        }
                    }
                ],
                "key": "override_liquid_settings",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::structure::LiquidSettings"
                },
                "optional": True
            }
        ]
    }
}
