# Generated from symbols.json for ::java::data::dialog::ConfirmationDialog
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.data.dialog.DialogBase import DialogBase

if TYPE_CHECKING:
    from generated_symbols.data.dialog.Button import Button


@dataclass(kw_only=True)
class ConfirmationDialog(DialogBase):
    yes: Button
    no: Button  # This action is also used for ESC-triggered exit.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::dialog::ConfirmationDialog": {
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
                "key": "yes",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::dialog::Button"
                }
            },
            {
                "kind": "pair",
                "desc": "This action is also used for ESC-triggered exit.",
                "key": "no",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::dialog::Button"
                }
            }
        ]
    }
}

