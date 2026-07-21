# Generated from symbols.json for ::java::data::dialog::ButtonListDialogBase
from dataclasses import dataclass
from typing import Annotated
from generated_symbols.data.dialog.ListDialogBase import ListDialogBase


@dataclass(kw_only=True)
class ButtonListDialogBase(ListDialogBase):
    button_width: Annotated[int, 'Range | Min `1` and above | inclusive'] | None = None  # Width of buttons in the list. Defaults to 150.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::dialog::ButtonListDialogBase": {
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
                "desc": "Width of buttons in the list.\nDefaults to 150.",
                "key": "button_width",
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

