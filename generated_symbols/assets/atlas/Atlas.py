# Generated from symbols.json for ::java::assets::atlas::Atlas
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.assets.atlas.SpriteSource import SpriteSource


@dataclass(kw_only=True)
class Atlas:
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

