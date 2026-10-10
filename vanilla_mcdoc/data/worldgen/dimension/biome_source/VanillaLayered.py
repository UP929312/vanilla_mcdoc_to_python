"""
Generated from symbols.json for ::java::data::worldgen::dimension::biome_source::VanillaLayered
Local link to file: vanilla_mcdoc/data/worldgen/dimension/biome_source/VanillaLayered.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel


class VanillaLayered(GeneratedModel):
    seed: int
    large_biomes: bool | None = None
    legacy_biome_init_layer: bool | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::dimension::biome_source::VanillaLayered": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "seed",
                "type": {
                    "kind": "long",
                    "attributes": [
                        {
                            "name": "random"
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "large_biomes",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "legacy_biome_init_layer",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}
