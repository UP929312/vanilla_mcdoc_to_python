# Generated from symbols.json for ::java::data::dialog::input::Option
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.util.text.Text import Text


@dataclass(kw_only=True)
class Option:
    id: str  # String to send on submit.
    display: Text | None = None  # Label displayed on the button. When not present, `id` will be used instead.
    initial: bool | None = None  # Whether this option is the initial value. Only one option can have this field set to `true`.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::dialog::input::Option": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "String to send on submit.",
                "key": "id",
                "type": {
                    "kind": "string"
                }
            },
            {
                "kind": "pair",
                "desc": "Label displayed on the button.\nWhen not present, `id` will be used instead.",
                "key": "display",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::text::Text"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether this option is the initial value.\nOnly one option can have this field set to `True`.",
                "key": "initial",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}

