# Generated from symbols.json for ::java::data::worldgen::attribute::BackgroundMusic
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.biome.BiomeMusic import BiomeMusic


@dataclass(kw_only=True)
class BackgroundMusic:
    default: BiomeMusic | None = None  # Default music to play
    underwater: BiomeMusic | None = None  # Overrides default music when underwater
    creative: BiomeMusic | None = None  # Overrides default music when in creative mode


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::attribute::BackgroundMusic": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Default music to play",
                "key": "default",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::biome::BiomeMusic"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Overrides default music when underwater",
                "key": "underwater",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::biome::BiomeMusic"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Overrides default music when in creative mode",
                "key": "creative",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::biome::BiomeMusic"
                },
                "optional": True
            }
        ]
    }
}

