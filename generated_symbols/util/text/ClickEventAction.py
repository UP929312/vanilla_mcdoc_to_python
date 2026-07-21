# Generated from symbols.json for ::java::util::text::ClickEventAction
from enum import Enum


class ClickEventAction(Enum):
    OPENURL = "open_url"
    RUNCOMMAND = "run_command"
    SUGGESTCOMMAND = "suggest_command"
    CHANGEPAGE = "change_page"
    COPYTOCLIPBOARD = "copy_to_clipboard"
    SHOWDIALOG = "show_dialog"
    CUSTOM = "custom"


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::text::ClickEventAction": {
        "kind": "enum",
        "enumKind": "string",
        "values": [
            {
                "identifier": "OpenUrl",
                "value": "open_url"
            },
            {
                "identifier": "RunCommand",
                "value": "run_command"
            },
            {
                "identifier": "SuggestCommand",
                "value": "suggest_command"
            },
            {
                "identifier": "ChangePage",
                "value": "change_page"
            },
            {
                "identifier": "CopyToClipboard",
                "value": "copy_to_clipboard"
            },
            {
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.6"
                            }
                        }
                    }
                ],
                "identifier": "ShowDialog",
                "value": "show_dialog"
            },
            {
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.6"
                            }
                        }
                    }
                ],
                "identifier": "Custom",
                "value": "custom"
            }
        ]
    }
}

