# Generated from symbols.json for ::java::util::text::ShowDialog
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

from runtime_metadata import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.dialog.Dialog import Dialog


@dataclass(kw_only=True)
class ShowDialog:
    dialog: Annotated[str, IdSpec(registry='dialog')] | Dialog


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

