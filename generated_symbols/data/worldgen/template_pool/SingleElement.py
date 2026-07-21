# Generated from symbols.json for ::java::data::worldgen::template_pool::SingleElement
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.data.worldgen.template_pool.ElementBase import ElementBase

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.processor_list.ProcessorListRef import ProcessorListRef
    from generated_symbols.data.worldgen.structure.LiquidSettings import LiquidSettings


@dataclass(kw_only=True)
class SingleElement(ElementBase):
    location: str
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

