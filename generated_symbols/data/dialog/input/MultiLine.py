# Generated from symbols.json for ::java::data::dialog::input::MultiLine
from dataclasses import dataclass
from typing import Annotated


@dataclass(kw_only=True)
class MultiLine:
    max_lines: Annotated[int, 'Range | Min `1` and above | inclusive'] | None = None
    height: Annotated[int, 'Range | `1`-`512` | both inclusive'] | None = None  # Height of the input. If this field is not present: - If `max_lines` is present, the height will be chosen to fit the maximum number of lines. The chosen height is capped at 512. - If `max_lines` is also not present, the height will be chosen to fit 4 lines.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::dialog::input::MultiLine": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "max_lines",
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
                "desc": "Height of the input.\nIf this field is not present:\n- If `max_lines` is present, the height will be chosen to fit the maximum number of lines. The chosen height is capped at 512.\n- If `max_lines` is also not present, the height will be chosen to fit 4 lines.",
                "key": "height",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 1,
                        "max": 512
                    }
                },
                "optional": True
            }
        ]
    }
}

