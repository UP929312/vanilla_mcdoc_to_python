# Generated from symbols.json for ::java::data::worldgen::structure::DirectPoolAlias
from dataclasses import dataclass


@dataclass(kw_only=True)
class DirectPoolAlias:
    alias: str
    target: str


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::structure::DirectPoolAlias": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "alias",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id"
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "target",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "worldgen/template_pool"
                                }
                            }
                        }
                    ]
                }
            }
        ]
    }
}

