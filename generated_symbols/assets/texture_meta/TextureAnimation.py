"""
Generated from symbols.json for ::java::assets::texture_meta::TextureAnimation
Local link to file: generated_symbols/assets/texture_meta/TextureAnimation.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from generated_symbols.base import GeneratedModel


class FramesStruct(GeneratedModel):
    index: Annotated[int, Field(ge=0)]  # A number corresponding to position of a frame from the top, with the top frame being 0.
    time: Annotated[int, Field(ge=1)] | None = None  # The time in ticks to show this frame, overriding `frametime` above.


class TextureAnimation(GeneratedModel):
    interpolate: bool | None = None  # If true, additional frames will be generated between frames with a frame time greater than 1 between them. Defaults to false.
    width: Annotated[int, Field(ge=1)] | None = None  # The width of the tile, as a direct ratio rather than in pixels. Can be used by resource packs to have frames that are not perfect squares.
    height: Annotated[int, Field(ge=1)] | None = None  # The height of the tile, as a direct ratio rather than in pixels. Can be used by resource packs to have frames that are not perfect squares.
    frametime: Annotated[int, Field(ge=1)] | None = None  # Sets the default time for each frame in increments of one game tick. Defaults to 1.
    frames: list[FramesStruct | Annotated[int, Field(ge=0)]] | None = None  # Defaults to displaying all the frames from top to bottom.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::texture_meta::TextureAnimation": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "If True, additional frames will be generated between frames with a frame time greater than 1 between them. Defaults to False.",
                "key": "interpolate",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "The width of the tile, as a direct ratio rather than in pixels. Can be used by resource packs to have frames that are not perfect squares.",
                "key": "width",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 1
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "The height of the tile, as a direct ratio rather than in pixels. Can be used by resource packs to have frames that are not perfect squares.",
                "key": "height",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 1
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Sets the default time for each frame in increments of one game tick. Defaults to 1.",
                "key": "frametime",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 1
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Defaults to displaying all the frames from top to bottom.",
                "key": "frames",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "union",
                        "members": [
                            {
                                "kind": "struct",
                                "fields": [
                                    {
                                        "kind": "pair",
                                        "desc": "A number corresponding to position of a frame from the top, with the top frame being 0.",
                                        "key": "index",
                                        "type": {
                                            "kind": "int",
                                            "valueRange": {
                                                "kind": 0,
                                                "min": 0
                                            }
                                        }
                                    },
                                    {
                                        "kind": "pair",
                                        "desc": "The time in ticks to show this frame, overriding `frametime` above.",
                                        "key": "time",
                                        "type": {
                                            "kind": "int",
                                            "valueRange": {
                                                "kind": 0,
                                                "min": 1
                                            }
                                        },
                                        "optional": True
                                    }
                                ]
                            },
                            {
                                "kind": "int",
                                "valueRange": {
                                    "kind": 0,
                                    "min": 0
                                }
                            }
                        ]
                    }
                },
                "optional": True
            }
        ]
    }
}

