"""
Generated from symbols.json for ::java::data::worldgen::dimension::chunk_generator::Flat
Local link to file: generated_symbols/data/worldgen/dimension/chunk_generator/Flat.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.dimension.chunk_generator.FlatGeneratorSettings import FlatGeneratorSettings


class Flat(GeneratedModel):
    settings: FlatGeneratorSettings


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::dimension::chunk_generator::Flat": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "settings",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::dimension::chunk_generator::FlatGeneratorSettings"
                }
            }
        ]
    }
}
