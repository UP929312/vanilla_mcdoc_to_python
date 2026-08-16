"""
Generated from symbols.json for ::java::assets::atlas::Atlas
Local link to file: generated_symbols/assets/atlas/Atlas.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from generated_symbols.assets.atlas.SpriteSource import SpriteSource


@dataclass(kw_only=True)
class Atlas:
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

