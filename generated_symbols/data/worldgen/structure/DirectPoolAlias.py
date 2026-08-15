"""
Generated from symbols.json for ::java::data::worldgen::structure::DirectPoolAlias
Local link to file: generated_symbols/data/worldgen/structure/DirectPoolAlias.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Annotated

from minecraft_registry import IdSpec


@dataclass(kw_only=True)
class DirectPoolAlias:
    alias: Annotated[str, IdSpec()]
    target: Annotated[str, IdSpec(registry='worldgen/template_pool')]


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

