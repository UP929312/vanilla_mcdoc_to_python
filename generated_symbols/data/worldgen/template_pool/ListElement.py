# Generated from symbols.json for ::java::data::worldgen::template_pool::ListElement
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.data.worldgen.template_pool.ElementBase import ElementBase

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.template_pool.Element import Element


@dataclass(kw_only=True)
class ListElement(ElementBase):
    elements: list[Element]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::template_pool::ListElement": {
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
                "key": "elements",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::data::worldgen::template_pool::Element"
                    }
                }
            }
        ]
    }
}

