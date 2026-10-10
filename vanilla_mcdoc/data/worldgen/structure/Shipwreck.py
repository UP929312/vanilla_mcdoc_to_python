"""
Generated from symbols.json for ::java::data::worldgen::structure::Shipwreck
Local link to file: vanilla_mcdoc/data/worldgen/structure/Shipwreck.py
"""
# ~~~ CODE ~~~
from typing import ClassVar

from vanilla_mcdoc.base import GeneratedModel


class Shipwreck(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/structure'

    is_beached: bool | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::structure::Shipwreck": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "is_beached",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}
