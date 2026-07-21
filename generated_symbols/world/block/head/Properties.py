# Generated from symbols.json for ::java::world::block::head::Properties
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.world.block.head.Texture import Texture


@dataclass(kw_only=True)
class Properties:
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

