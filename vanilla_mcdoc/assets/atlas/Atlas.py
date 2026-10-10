"""
Generated from symbols.json for ::java::assets::atlas::Atlas
Local link to file: vanilla_mcdoc/assets/atlas/Atlas.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.assets.atlas.SpriteSource import SpriteSource


class Atlas(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'atlas'

    sources: list[SpriteSource]  # List of sprite sources which can add or remove sprite textures to this atlas.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::atlas::Atlas": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "List of sprite sources which can add or remove sprite textures to this atlas.",
                "key": "sources",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::assets::atlas::SpriteSource"
                    }
                }
            }
        ]
    }
}
