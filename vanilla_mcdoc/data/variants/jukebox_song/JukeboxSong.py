"""
Generated from symbols.json for ::java::data::variants::jukebox_song::JukeboxSong
Local link to file: vanilla_mcdoc/data/variants/jukebox_song/JukeboxSong.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.util.SoundEventRef import SoundEventRef
    from vanilla_mcdoc.util.text.Text import Text


class JukeboxSong(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'jukebox_song'

    description: Text  # Displayed in the HUD actionbar & item tooltip.
    comparator_output: Annotated[int, Field(ge=0, le=15)]
    length_in_seconds: Annotated[float, Field(gt=0)]
    sound_event: SoundEventRef
