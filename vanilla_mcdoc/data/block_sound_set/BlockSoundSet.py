"""
Generated from symbols.json for ::java::data::block_sound_set::BlockSoundSet
Local link to file: vanilla_mcdoc/data/block_sound_set/BlockSoundSet.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.util.SoundEventRef import SoundEventRef


class BlockSoundSet(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'block_sound_set'

    volume: Annotated[float, Field(ge=1e-05, le=10)] | None = None  # Defaults to 1.
    pitch: Annotated[float, Field(ge=1e-05, le=2)] | None = None  # Defauls to 1.
    break_sound: SoundEventRef | None = None
    step_sound: SoundEventRef | None = None
    place_sound: SoundEventRef | None = None
    hit_sound: SoundEventRef | None = None
    fall_sound: SoundEventRef | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::block_sound_set::BlockSoundSet": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Defaults to 1.",
                "key": "volume",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 1e-05,
                        "max": 10
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Defauls to 1.",
                "key": "pitch",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 1e-05,
                        "max": 2
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "break_sound",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::util::SoundEventRef"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "step_sound",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::util::SoundEventRef"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "place_sound",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::util::SoundEventRef"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "hit_sound",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::util::SoundEventRef"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "fall_sound",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::util::SoundEventRef"
                },
                "optional": True
            }
        ]
    }
}
