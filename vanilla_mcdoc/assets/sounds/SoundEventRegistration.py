"""
Generated from symbols.json for ::java::assets::sounds::SoundEventRegistration
Local link to file: vanilla_mcdoc/assets/sounds/SoundEventRegistration.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.assets.sounds.Sound import Sound


class SoundEventRegistration(GeneratedModel):
    sounds: list[Annotated[str, IdSpec(registry='sound')] | Sound] | None = None  # The sound files this sound event uses. One sound is randomly selected to play when the event is triggered. Defaults to assumed path.
    replace: bool | None = None  # If true the sounds listed should replace the ones listed in the minecraft sounds.json for this sound event. False if the sounds listed should be added. If undefined. Defaults to false.
    subtitle: str | None = None  # Translated as the subtitle when Show Subtitles is enabled. Section sign formatting codes are supported.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::sounds::SoundEventRegistration": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "The sound files this sound event uses. One sound is randomly selected to play when the event is triggered. Defaults to assumed path.",
                "key": "sounds",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "union",
                        "members": [
                            {
                                "kind": "string",
                                "attributes": [
                                    {
                                        "name": "id",
                                        "value": {
                                            "kind": "literal",
                                            "value": {
                                                "kind": "string",
                                                "value": "sound"
                                            }
                                        }
                                    }
                                ]
                            },
                            {
                                "kind": "reference",
                                "path": "::java::assets::sounds::Sound"
                            }
                        ]
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "If True the sounds listed should replace the ones listed in the minecraft sounds.json for this sound event.\nFalse if the sounds listed should be added. If undefined. Defaults to False.",
                "key": "replace",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Translated as the subtitle when Show Subtitles is enabled. Section sign formatting codes are supported.",
                "key": "subtitle",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "translation_key"
                        }
                    ]
                },
                "optional": True
            }
        ]
    }
}
