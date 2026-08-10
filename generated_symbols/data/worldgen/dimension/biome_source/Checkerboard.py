"""
Generated from symbols.json for ::java::data::worldgen::dimension::biome_source::Checkerboard
Local link to file: generated_symbols/data/worldgen/dimension/biome_source/Checkerboard.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Annotated

from runtime_metadata import IdSpec


@dataclass(kw_only=True)
class Checkerboard:
    biomes: list[Annotated[str, IdSpec(registry='worldgen/biome')]] | Annotated[str, IdSpec(registry='worldgen/biome', tags='allowed')]
    scale: Annotated[int, 'Range | `0`-`62` | both inclusive'] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::dimension::biome_source::Checkerboard": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "scale",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 62
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "biomes",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "list",
                            "item": {
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
                        },
                        {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "since",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.18.2"
                                        }
                                    }
                                },
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "tree",
                                        "values": {
                                            "registry": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "string",
                                                    "value": "worldgen/biome"
                                                }
                                            },
                                            "tags": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "string",
                                                    "value": "allowed"
                                                }
                                            }
                                        }
                                    }
                                }
                            ]
                        }
                    ]
                }
            }
        ]
    }
}

