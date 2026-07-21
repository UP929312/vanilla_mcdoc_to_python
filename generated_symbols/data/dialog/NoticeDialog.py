# Generated from symbols.json for ::java::data::dialog::NoticeDialog
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.data.dialog.DialogBase import DialogBase

if TYPE_CHECKING:
    from generated_symbols.data.dialog.Button import Button


@dataclass(kw_only=True)
class NoticeDialog(DialogBase):
    action: Button | None = None  # The only action in footer. Defaults to `gui.ok` label with no action or tooltip.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::dialog::NoticeDialog": {
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
                "desc": "The only action in footer.\nDefaults to `gui.ok` label with no action or tooltip.",
                "key": "action",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::dialog::Button"
                },
                "optional": True
            }
        ]
    }
}

