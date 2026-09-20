"""
Generated from symbols.json for ::java::assets::texture_meta::TextureAnimationFrame
Local link to file: generated_symbols/assets/texture_meta/TextureAnimationFrame.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from generated_symbols.base import GeneratedModel
from pydantic import Field


class TextureAnimationFrame(GeneratedModel):
    index: Annotated[int, Field(ge=0)]  # A number corresponding to position of a frame from the top, with the top frame being 0.
    time: Annotated[int, Field(ge=1)] | None = None  # The time in ticks to show this frame, overriding `frametime` above.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::texture_meta::TextureAnimationFrame": {
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
    }
}

