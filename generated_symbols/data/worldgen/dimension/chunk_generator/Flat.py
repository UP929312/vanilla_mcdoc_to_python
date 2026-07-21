# Generated from symbols.json for ::java::data::worldgen::dimension::chunk_generator::Flat
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.dimension.chunk_generator.FlatGeneratorSettings import FlatGeneratorSettings


@dataclass(kw_only=True)
class Flat:
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

