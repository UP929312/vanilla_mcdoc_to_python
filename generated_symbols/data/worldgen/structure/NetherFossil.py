"""
Generated from symbols.json for ::java::data::worldgen::structure::NetherFossil
Local link to file: generated_symbols/data/worldgen/structure/NetherFossil.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.HeightProvider import HeightProvider


@dataclass(kw_only=True)
class NetherFossil:
    __resource_dir__: ClassVar[str] = 'worldgen/structure'

    height: HeightProvider


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::structure::NetherFossil": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "height",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::HeightProvider"
                }
            }
        ]
    }
}

