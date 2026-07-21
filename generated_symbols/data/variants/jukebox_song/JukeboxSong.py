# Generated from symbols.json for ::java::data::variants::jukebox_song::JukeboxSong
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.data.util.SoundEventRef import SoundEventRef
    from generated_symbols.util.text.Text import Text


@dataclass(kw_only=True)
class JukeboxSong:
    description: Text  # Displayed in the HUD actionbar & item tooltip.
    comparator_output: Annotated[int, 'Range | `0`-`15` | both inclusive']
    length_in_seconds: Annotated[float, 'Range | Min `0` and above | inclusive']
    sound_event: SoundEventRef


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::variants::jukebox_song::JukeboxSong": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Displayed in the HUD actionbar & item tooltip.",
                "key": "description",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::text::Text"
                }
            },
            {
                "kind": "pair",
                "key": "comparator_output",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 15
                    }
                }
            },
            {
                "kind": "pair",
                "key": "length_in_seconds",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 2,
                        "min": 0
                    }
                }
            },
            {
                "kind": "pair",
                "key": "sound_event",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::util::SoundEventRef"
                }
            }
        ]
    }
}

