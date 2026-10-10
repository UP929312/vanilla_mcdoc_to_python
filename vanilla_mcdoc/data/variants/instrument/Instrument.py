"""
Generated from symbols.json for ::java::data::variants::instrument::Instrument
Local link to file: vanilla_mcdoc/data/variants/instrument/Instrument.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.util.SoundEventRef import SoundEventRef
    from vanilla_mcdoc.util.text.Text import Text


class Instrument(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'instrument'

    sound_event: SoundEventRef
    range: Annotated[float, Field(gt=0)]  # Maximum range in blocks that the sound can be heard
    use_duration: Annotated[float, Field(ge=0)]  # Duration of use in seconds, used as item cooldown
    durability_damage: Annotated[int, Field(ge=0)] | None = None
    description: Text
