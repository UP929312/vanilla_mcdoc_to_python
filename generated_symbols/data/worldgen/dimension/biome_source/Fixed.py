# Generated from symbols.json for ::java::data::worldgen::dimension::biome_source::Fixed
from dataclasses import dataclass


@dataclass(kw_only=True)
class Fixed:
    biome: str


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

