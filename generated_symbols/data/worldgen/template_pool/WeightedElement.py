"""
Generated from symbols.json for ::java::data::worldgen::template_pool::WeightedElement
Local link to file: generated_symbols/data/worldgen/template_pool/WeightedElement.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from generated_symbols.base import GeneratedModel
from pydantic import Field

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.template_pool.Element import Element


class WeightedElement(GeneratedModel):
    weight: Annotated[int, Field(ge=1, le=150)]
    element: Element


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::template_pool::WeightedElement": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "weight",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "int",
                            "valueRange": {
                                "kind": 0,
                                "min": 1
                            },
                            "attributes": [
                                {
                                    "name": "until",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.17"
                                        }
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "int",
                            "valueRange": {
                                "kind": 0,
                                "min": 1,
                                "max": 150
                            },
                            "attributes": [
                                {
                                    "name": "since",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.17"
                                        }
                                    }
                                }
                            ]
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "element",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::template_pool::Element"
                }
            }
        ]
    }
}

