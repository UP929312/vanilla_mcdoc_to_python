# Generated from symbols.json for ::java::data::worldgen::dimension::biome_source::VanillaLayered
from dataclasses import dataclass


@dataclass(kw_only=True)
class VanillaLayered:
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

