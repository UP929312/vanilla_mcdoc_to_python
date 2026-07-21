# Generated from symbols.json for ::java::data::dialog::input::SingleOptionInput
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.data.dialog.input.Option import Option
    from generated_symbols.util.text.Text import Text


@dataclass(kw_only=True)
class SingleOptionInput:
    label: Text  # Label displayed on the button.
    options: Annotated[list[Option | str], 'Length = 1 (inclusive) and above']
    width: Annotated[int, 'Range | `1`-`1024` | both inclusive'] | None = None  # Defaults to 200.
    label_visible: bool | None = None  # Defaults to `true`.


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

