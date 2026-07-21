# Generated from symbols.json for ::java::data::dialog::input::TextInput
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Any

if TYPE_CHECKING:
    from generated_symbols.util.text.Text import Text


@dataclass(kw_only=True)
class TextInput:
    label: Text  # Label displayed to the left of control.
    width: Annotated[int, 'Range | `1`-`1024` | both inclusive'] | None = None  # Defaults to 200.
    label_visible: bool | None = None  # Defaults to `true`.
    initial: str | None = None  # Initial contents of the text input. Defaults to `""` (empty string).
    max_length: Annotated[int, 'Range | Min `1` and above | inclusive'] | None = None  # Maximum length of input Defaults to 32.
    multiline: Any | None = None  # If present, allows users to input multiple lines.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::dialog::input::TextInput": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Defaults to 200.",
                "key": "width",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 1,
                        "max": 1024
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Label displayed to the left of control.",
                "key": "label",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::text::Text"
                }
            },
            {
                "kind": "pair",
                "desc": "Defaults to `True`.",
                "key": "label_visible",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Initial contents of the text input.\nDefaults to `\"\"` (empty string).",
                "key": "initial",
                "type": {
                    "kind": "string"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Maximum length of input\nDefaults to 32.",
                "key": "max_length",
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
                "desc": "If present, allows users to input multiple lines.",
                "key": "multiline",
                "type": {
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
                },
                "optional": True
            }
        ]
    }
}

