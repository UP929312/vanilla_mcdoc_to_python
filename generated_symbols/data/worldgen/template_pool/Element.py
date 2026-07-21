# Generated from symbols.json for ::java::data::worldgen::template_pool::Element
from dataclasses import dataclass


@dataclass(kw_only=True)
class Element:
    element_type: str


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::template_pool::Element": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "element_type",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "worldgen/structure_pool_element"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "dynamic",
                            "accessor": [
                                "element_type"
                            ]
                        }
                    ],
                    "registry": "minecraft:template_pool_element"
                }
            }
        ]
    }
}

