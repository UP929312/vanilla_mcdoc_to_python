# Generated from symbols.json for ::java::data::dialog::RedirectDialog
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.data.dialog.ButtonListDialogBase import ButtonListDialogBase

if TYPE_CHECKING:
    from generated_symbols.data.dialog.Dialog import Dialog


@dataclass(kw_only=True)
class RedirectDialog(ButtonListDialogBase):
    dialogs: list[str | Dialog] | str | Dialog


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
                    "kind": "union",
                    "members": [
                        {
                            "kind": "list",
                            "item": {
                                "kind": "union",
                                "members": [
                                    {
                                        "kind": "string",
                                        "attributes": [
                                            {
                                                "name": "id",
                                                "value": {
                                                    "kind": "literal",
                                                    "value": {
                                                        "kind": "string",
                                                        "value": "dialog"
                                                    }
                                                }
                                            }
                                        ]
                                    },
                                    {
                                        "kind": "reference",
                                        "path": "::java::data::dialog::Dialog"
                                    }
                                ]
                            }
                        },
                        {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "tree",
                                        "values": {
                                            "registry": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "string",
                                                    "value": "dialog"
                                                }
                                            },
                                            "tags": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "string",
                                                    "value": "allowed"
                                                }
                                            }
                                        }
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "reference",
                            "path": "::java::data::dialog::Dialog"
                        }
                    ]
                }
            }
        ]
    }
}

