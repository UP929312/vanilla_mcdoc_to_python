"""
Generated from symbols.json for ::java::data::dialog::input::InputControl
Local link to file: generated_symbols/data/dialog/input/InputControl.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Literal

if TYPE_CHECKING:
    from generated_symbols.data.dialog.input.Option import Option
    from generated_symbols.util.text.Text import Text


@dataclass(kw_only=True)
class MultilineStruct:
    max_lines: Annotated[int, 'Range | Min `1` and above | inclusive'] | None = None
    height: Annotated[int, 'Range | `1`-`512` | both inclusive'] | None = None  # Height of the input. If this field is not present: - If `max_lines` is present, the height will be chosen to fit the maximum number of lines. The chosen height is capped at 512. - If `max_lines` is also not present, the height will be chosen to fit 4 lines.


@dataclass(kw_only=True)
class InputControlBoolean:
    type: Literal['minecraft:boolean']
    key: Annotated[str, 'Length = 1 (inclusive) and above'] | str  # The input key, which is used to build macro command and generate custom action payload.
    label: Text  # Label displayed to the right of control.
    initial: bool | None = None  # Initial value of the control. Defaults to `false` (unchecked).
    on_true: str | None = None  # String to send when the control is checked. Defaults to `"true"`.
    on_false: str | None = None  # String to send when the control is unchecked. Defaults to `"false"`.


@dataclass(kw_only=True)
class InputControlNumberRange:
    type: Literal['minecraft:number_range']
    key: Annotated[str, 'Length = 1 (inclusive) and above'] | str  # The input key, which is used to build macro command and generate custom action payload.
    label: Text  # Label displayed on the slider.
    start: float  # Start value, inclusive.
    end: float  # End value, inclusive.
    width: Annotated[int, 'Range | `1`-`1024` | both inclusive'] | None = None  # Defaults to 200.
    label_format: str | None = None  # The translation to be used for building label. `%1$s` is replaced by `label`; `%2$s` is replaced by current value of the slider. Defaults to `options.generic_value`.
    step: Annotated[float, 'Range | Min `0` and above | inclusive'] | None = None  # Step size of the input. If not present, any value from range is allowed.
    initial: float | None = None  # Initial value of the slider. Rounded down nearest step. Defaults to the middle of the range.


@dataclass(kw_only=True)
class InputControlSingleOption:
    type: Literal['minecraft:single_option']
    key: Annotated[str, 'Length = 1 (inclusive) and above'] | str  # The input key, which is used to build macro command and generate custom action payload.
    label: Text  # Label displayed on the button.
    options: Annotated[list[Option | str], 'Length = 1 (inclusive) and above']
    width: Annotated[int, 'Range | `1`-`1024` | both inclusive'] | None = None  # Defaults to 200.
    label_visible: bool | None = None  # Defaults to `true`.


@dataclass(kw_only=True)
class InputControlText:
    type: Literal['minecraft:text']
    key: Annotated[str, 'Length = 1 (inclusive) and above'] | str  # The input key, which is used to build macro command and generate custom action payload.
    label: Text  # Label displayed to the left of control.
    width: Annotated[int, 'Range | `1`-`1024` | both inclusive'] | None = None  # Defaults to 200.
    label_visible: bool | None = None  # Defaults to `true`.
    initial: str | None = None  # Initial contents of the text input. Defaults to `""` (empty string).
    max_length: Annotated[int, 'Range | Min `1` and above | inclusive'] | None = None  # Maximum length of input Defaults to 32.
    multiline: MultilineStruct | None = None  # If present, allows users to input multiple lines.


type InputControl = InputControlBoolean | InputControlNumberRange | InputControlSingleOption | InputControlText


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::dialog::input::InputControl": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "type",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "input_control_type"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "desc": "The input key, which is used to build macro command and generate custom action payload.",
                "key": "key",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "union",
                            "members": [
                                {
                                    "kind": "string",
                                    "lengthRange": {
                                        "kind": 0,
                                        "min": 1
                                    },
                                    "attributes": [
                                        {
                                            "name": "match_regex",
                                            "value": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "string",
                                                    "value": "^[A-Za-z0-9_]*$"
                                                }
                                            }
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "kind": "dispatcher",
                            "parallelIndices": [
                                {
                                    "kind": "static",
                                    "value": "%fallback"
                                }
                            ],
                            "registry": "mcdoc:custom_dynamic_event_keys"
                        }
                    ]
                }
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "dynamic",
                            "accessor": [
                                "type"
                            ]
                        }
                    ],
                    "registry": "minecraft:input_control"
                }
            }
        ]
    }
}

