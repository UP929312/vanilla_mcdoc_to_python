# Generated from symbols.json for ::java::data::dialog::MultiActionDialog
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated
from generated_symbols.data.dialog.ListDialogBase import ListDialogBase

if TYPE_CHECKING:
    from generated_symbols.data.dialog.Button import Button


@dataclass(kw_only=True)
class MultiActionDialog(ListDialogBase):
    actions: Annotated[list[Button], 'Length = 1 (inclusive) and above']


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::dialog::MultiActionDialog": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::dialog::ListDialogBase"
                }
            },
            {
                "kind": "pair",
                "key": "actions",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::data::dialog::Button"
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

