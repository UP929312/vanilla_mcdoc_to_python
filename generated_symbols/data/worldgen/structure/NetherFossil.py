# Generated from symbols.json for ::java::data::worldgen::structure::NetherFossil
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.HeightProvider import HeightProvider


@dataclass(kw_only=True)
class NetherFossil:
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

