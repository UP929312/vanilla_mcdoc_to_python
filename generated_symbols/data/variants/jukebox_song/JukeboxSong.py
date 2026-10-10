"""
Generated from symbols.json for ::java::data::variants::jukebox_song::JukeboxSong
Local link to file: generated_symbols/data/variants/jukebox_song/JukeboxSong.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar

from pydantic import Field

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.util.SoundEventRef import SoundEventRef
    from generated_symbols.util.text.Text import Text


class JukeboxSong(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'jukebox_song'

    description: Text  # Displayed in the HUD actionbar & item tooltip.
    comparator_output: Annotated[int, Field(ge=0, le=15)]
    length_in_seconds: Annotated[float, Field(gt=0)]
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
