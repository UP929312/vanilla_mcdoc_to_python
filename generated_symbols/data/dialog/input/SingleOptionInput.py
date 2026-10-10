"""
Generated from symbols.json for ::java::data::dialog::input::SingleOptionInput
Local link to file: generated_symbols/data/dialog/input/SingleOptionInput.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.dialog.input.Option import Option
    from generated_symbols.util.text.Text import Text


class SingleOptionInput(GeneratedModel):
    width: Annotated[int, Field(ge=1, le=1024)] | None = None  # Defaults to 200.
    label: Text  # Label displayed on the button.
    label_visible: bool | None = None  # Defaults to `true`.
    options: Annotated[list[Option | str], Field(min_length=1)]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::dialog::input::SingleOptionInput": {
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
                "desc": "Label displayed on the button.",
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
                "key": "options",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "union",
                        "members": [
                            {
                                "kind": "reference",
                                "path": "::java::data::dialog::input::Option"
                            },
                            {
                                "kind": "string"
                            }
                        ]
                    },
                    "lengthRange": {
                        "kind": 0,
                        "min": 1
                    }
                }
            }
        ]
    }
}
