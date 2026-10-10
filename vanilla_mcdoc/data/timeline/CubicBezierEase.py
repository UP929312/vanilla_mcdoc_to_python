"""
Generated from symbols.json for ::java::data::timeline::CubicBezierEase
Local link to file: generated_symbols/data/timeline/CubicBezierEase.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from generated_symbols.base import GeneratedModel


class CubicBezierEase(GeneratedModel):
    cubic_bezier: tuple[Annotated[float, Field(ge=0, le=1)], float, Annotated[float, Field(ge=0, le=1)], float]  # `[x1, y1, x2, y2]` For an easy GUI, check out: https://cubic-bezier.com/


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::timeline::CubicBezierEase": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "`[x1, y1, x2, y2]`\nFor an easy GUI, check out: https://cubic-bezier.com/",
                "key": "cubic_bezier",
                "type": {
                    "kind": "tuple",
                    "items": [
                        {
                            "kind": "float",
                            "valueRange": {
                                "kind": 0,
                                "min": 0,
                                "max": 1
                            }
                        },
                        {
                            "kind": "float"
                        },
                        {
                            "kind": "float",
                            "valueRange": {
                                "kind": 0,
                                "min": 0,
                                "max": 1
                            }
                        },
                        {
                            "kind": "float"
                        }
                    ]
                }
            }
        ]
    }
}
