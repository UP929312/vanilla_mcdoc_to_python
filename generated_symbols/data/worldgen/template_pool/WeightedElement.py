# Generated from symbols.json for ::java::data::worldgen::template_pool::WeightedElement
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.template_pool.Element import Element


@dataclass(kw_only=True)
class WeightedElement:
    weight: Annotated[int, 'Range | `1`-`150` | both inclusive']
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

