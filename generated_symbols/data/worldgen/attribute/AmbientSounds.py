# Generated from symbols.json for ::java::data::worldgen::attribute::AmbientSounds
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.util.SoundEventRef import SoundEventRef
    from generated_symbols.data.worldgen.biome.BiomeSoundAdditions import BiomeSoundAdditions
    from generated_symbols.data.worldgen.biome.MoodSound import MoodSound


@dataclass(kw_only=True)
class AmbientSounds:
    loop: SoundEventRef | None = None
    mood: MoodSound | None = None
    additions: BiomeSoundAdditions | list[BiomeSoundAdditions] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::attribute::AmbientSounds": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "loop",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::util::SoundEventRef"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "mood",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::biome::MoodSound"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "additions",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "reference",
                            "path": "::java::data::worldgen::biome::BiomeSoundAdditions"
                        },
                        {
                            "kind": "list",
                            "item": {
                                "kind": "reference",
                                "path": "::java::data::worldgen::biome::BiomeSoundAdditions"
                            }
                        }
                    ]
                },
                "optional": True
            }
        ]
    }
}

