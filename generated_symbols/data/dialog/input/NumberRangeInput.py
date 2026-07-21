# Generated from symbols.json for ::java::data::dialog::input::NumberRangeInput
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.util.text.Text import Text


@dataclass(kw_only=True)
class NumberRangeInput:
    label: Text  # Label displayed on the slider.
    start: float  # Start value, inclusive.
    end: float  # End value, inclusive.
    width: Annotated[int, 'Range | `1`-`1024` | both inclusive'] | None = None  # Defaults to 200.
    label_format: str | None = None  # The translation to be used for building label. `%1$s` is replaced by `label`; `%2$s` is replaced by current value of the slider. Defaults to `options.generic_value`.
    step: Annotated[float, 'Range | Min `0` and above | inclusive'] | None = None  # Step size of the input. If not present, any value from range is allowed.
    initial: float | None = None  # Initial value of the slider. Rounded down nearest step. Defaults to the middle of the range.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::dialog::input::NumberRangeInput": {
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
                "desc": "Label displayed on the slider.",
                "key": "label",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::text::Text"
                }
            },
            {
                "kind": "pair",
                "desc": "The translation to be used for building label.\n`%1$s` is replaced by `label`; `%2$s` is replaced by current value of the slider.\nDefaults to `options.generic_value`.",
                "key": "label_format",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "translation_key"
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Start value, inclusive.",
                "key": "start",
                "type": {
                    "kind": "float"
                }
            },
            {
                "kind": "pair",
                "desc": "End value, inclusive.",
                "key": "end",
                "type": {
                    "kind": "float"
                }
            },
            {
                "kind": "pair",
                "desc": "Step size of the input.\nIf not present, any value from range is allowed.",
                "key": "step",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 2,
                        "min": 0
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Initial value of the slider. Rounded down nearest step.\nDefaults to the middle of the range.",
                "key": "initial",
                "type": {
                    "kind": "float"
                },
                "optional": True
            }
        ]
    }
}

