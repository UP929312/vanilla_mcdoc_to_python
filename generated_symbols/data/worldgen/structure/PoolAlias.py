# Generated from symbols.json for ::java::data::worldgen::structure::PoolAlias
from dataclasses import dataclass


@dataclass(kw_only=True)
class PoolAlias:
    type: str


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::structure::PoolAlias": {
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
                                    "value": "worldgen/pool_alias_binding"
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
                    "registry": "minecraft:worldgen/pool_alias_binding"
                }
            }
        ]
    }
}

