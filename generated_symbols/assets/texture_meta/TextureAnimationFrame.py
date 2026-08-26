"""
Generated from symbols.json for ::java::assets::texture_meta::TextureAnimationFrame
Local link to file: generated_symbols/assets/texture_meta/TextureAnimationFrame.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Annotated


@dataclass(kw_only=True)
class TextureAnimationFrame:
    index: Annotated[int, 'Range | `0` and above | inclusive']  # A number corresponding to position of a frame from the top, with the top frame being 0.
    time: Annotated[int, 'Range | `1` and above | inclusive'] | None = None  # The time in ticks to show this frame, overriding `frametime` above.


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

