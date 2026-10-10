"""
Generated from symbols.json for ::java::data::worldgen::structure::DirectPoolAlias
Local link to file: vanilla_mcdoc/data/worldgen/structure/DirectPoolAlias.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec


class DirectPoolAlias(GeneratedModel):
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
