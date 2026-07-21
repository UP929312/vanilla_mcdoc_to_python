# Generated from symbols.json for ::java::data::dialog::ListDialogBase
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated
from generated_symbols.data.dialog.DialogBase import DialogBase

if TYPE_CHECKING:
    from generated_symbols.data.dialog.Button import Button


@dataclass(kw_only=True)
class ListDialogBase(DialogBase):
    exit_action: Button | None = None  # The button in footer. The action is also used for ESC-triggered exit.
    columns: Annotated[int, 'Range | Min `1` and above | inclusive'] | None = None  # The number of columns. Defaults to 2.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::dialog::ListDialogBase": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::dialog::DialogBase"
                }
            },
            {
                "kind": "pair",
                "desc": "The button in footer.\nThe action is also used for ESC-triggered exit.",
                "key": "exit_action",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::dialog::Button"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "The number of columns.\nDefaults to 2.",
                "key": "columns",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 1
                    }
                },
                "optional": True
            }
        ]
    }
}

