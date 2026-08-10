"""
Generated from symbols.json for ::java::data::dialog::DialogListRef
Local link to file: generated_symbols/data/dialog/DialogListRef.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from runtime_metadata import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.dialog.Dialog import Dialog


type DialogListRef = Dialog | Annotated[str, IdSpec(registry='dialog', tags='allowed')] | list[Annotated[str, IdSpec(registry='dialog')] | Dialog]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::dialog::DialogListRef": {
        "kind": "union",
        "members": [
            {
                "kind": "reference",
                "path": "::java::data::dialog::Dialog"
            },
            {
                "kind": "list",
                "item": {
                    "kind": "reference",
                    "path": "::java::data::dialog::Dialog"
                },
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.3"
                            }
                        }
                    }
                ]
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
                            "path": "::java::data::dialog::Dialog",
                            "attributes": [
                                {
                                    "name": "since",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "26.3"
                                        }
                                    }
                                }
                            ]
                        }
                    ]
                }
            }
        ]
    }
}

