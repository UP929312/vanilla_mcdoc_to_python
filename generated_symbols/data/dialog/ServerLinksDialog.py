"""
Generated from symbols.json for ::java::data::dialog::ServerLinksDialog
Local link to file: generated_symbols/data/dialog/ServerLinksDialog.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass

from generated_symbols.data.dialog.ButtonListDialogBase import ButtonListDialogBase


@dataclass(kw_only=True)
class ServerLinksDialog(ButtonListDialogBase):
    pass


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::dialog::ServerLinksDialog": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::dialog::ButtonListDialogBase"
                }
            }
        ]
    }
}

