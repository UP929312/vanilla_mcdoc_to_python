# Generated from symbols.json for ::java::data::dialog::RedirectDialog
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.data.dialog.ButtonListDialogBase import ButtonListDialogBase

if TYPE_CHECKING:
    from generated_symbols.data.dialog.DialogListRef import DialogListRef


@dataclass(kw_only=True)
class RedirectDialog(ButtonListDialogBase):
    dialogs: DialogListRef


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::dialog::RedirectDialog": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::dialog::ButtonListDialogBase"
                }
            },
            {
                "kind": "pair",
                "key": "dialogs",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::dialog::DialogListRef"
                }
            }
        ]
    }
}

