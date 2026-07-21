# Generated from symbols.json for ::java::data::worldgen::feature::tree::TreeDecorator
from dataclasses import dataclass


@dataclass(kw_only=True)
class TreeDecorator:
    type: str


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::tree::TreeDecorator": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "type",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "worldgen/tree_decorator_type"
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
                                "type"
                            ]
                        }
                    ],
                    "registry": "minecraft:tree_decorator"
                }
            }
        ]
    }
}

