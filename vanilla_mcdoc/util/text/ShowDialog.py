"""
Generated from symbols.json for ::java::util::text::ShowDialog
Local link to file: generated_symbols/util/text/ShowDialog.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from generated_symbols.base import GeneratedModel
from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.dialog.Dialog import Dialog
    from generated_symbols.registry.KnownDialogId import KnownDialogId


class ShowDialog(GeneratedModel):
    dialog: Annotated[str, IdSpec(registry='dialog')] | KnownDialogId | Dialog


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::text::ShowDialog": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "dialog",
                "type": {
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
            }
        ]
    }
}
