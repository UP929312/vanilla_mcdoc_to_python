"""
Generated from symbols.json for ::java::data::worldgen::dimension::biome_source::Fixed
Local link to file: generated_symbols/data/worldgen/dimension/biome_source/Fixed.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Annotated

from minecraft_registry import IdSpec


@dataclass(kw_only=True)
class Fixed:
    biome: Annotated[str, IdSpec(registry='worldgen/biome')]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::dimension::biome_source::Fixed": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "biome",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "worldgen/biome"
                                }
                            }
                        }
                    ]
                }
            }
        ]
    }
}

