"""
Generated from symbols.json for ::java::world::block::head::Properties
Local link to file: generated_symbols/world/block/head/Properties.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.world.block.head.Texture import Texture


class Properties(GeneratedModel):
    textures: list[Texture] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::block::head::Properties": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "textures",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::world::block::head::Texture"
                    }
                },
                "optional": True
            }
        ]
    }
}

