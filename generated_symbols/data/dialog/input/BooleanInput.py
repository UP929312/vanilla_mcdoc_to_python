# Generated from symbols.json for ::java::data::dialog::input::BooleanInput
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.util.text.Text import Text


@dataclass(kw_only=True)
class BooleanInput:
    label: Text  # Label displayed to the right of control.
    initial: bool | None = None  # Initial value of the control. Defaults to `false` (unchecked).
    on_true: str | None = None  # String to send when the control is checked. Defaults to `"true"`.
    on_false: str | None = None  # String to send when the control is unchecked. Defaults to `"false"`.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::dialog::input::BooleanInput": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Label displayed to the right of control.",
                "key": "label",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::text::Text"
                }
            },
            {
                "kind": "pair",
                "desc": "Initial value of the control.\nDefaults to `False` (unchecked).",
                "key": "initial",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "String to send when the control is checked.\nDefaults to `\"True\"`.",
                "key": "on_True",
                "type": {
                    "kind": "string"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "String to send when the control is unchecked.\nDefaults to `\"False\"`.",
                "key": "on_False",
                "type": {
                    "kind": "string"
                },
                "optional": True
            }
        ]
    }
}

