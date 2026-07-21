# Generated from symbols.json for ::java::data::timeline::CubicBezierEase
from dataclasses import dataclass
from typing import Annotated


@dataclass(kw_only=True)
class CubicBezierEase:
    cubic_bezier: tuple[Annotated[float, 'Range | `0`-`1` | both inclusive'], float, Annotated[float, 'Range | `0`-`1` | both inclusive'], float]  # `[x1, y1, x2, y2]` For an easy GUI, check out: https://cubic-bezier.com/


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

