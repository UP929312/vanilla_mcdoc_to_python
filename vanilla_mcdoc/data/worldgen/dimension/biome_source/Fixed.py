"""
Generated from symbols.json for ::java::data::worldgen::dimension::biome_source::Fixed
Local link to file: vanilla_mcdoc/data/worldgen/dimension/biome_source/Fixed.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec


class Fixed(GeneratedModel):
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
