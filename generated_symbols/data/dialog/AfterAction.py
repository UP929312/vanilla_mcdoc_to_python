# Generated from symbols.json for ::java::data::dialog::AfterAction
from enum import Enum


class AfterAction(Enum):
    CLOSE = "close"  # Closes the dialog. Returns to the previous non-dialog screen, if any.
    NONE = "none"  # Does nothing. Only available if `pause` is set to `false`.
    WAITFORRESPONSE = "wait_for_response"  # Replaces the dialog with a "Waiting for Response" screen. The waiting screen unpauses the game in single-player mode.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::dialog::AfterAction": {
        "kind": "enum",
        "enumKind": "string",
        "values": [
            {
                "desc": "Closes the dialog.\nReturns to the previous non-dialog screen, if any.",
                "identifier": "Close",
                "value": "close"
            },
            {
                "desc": "Does nothing.\nOnly available if `pause` is set to `False`.",
                "identifier": "None",
                "value": "none"
            },
            {
                "desc": "Replaces the dialog with a \"Waiting for Response\" screen.\nThe waiting screen unpauses the game in single-player mode.",
                "identifier": "WaitForResponse",
                "value": "wait_for_response"
            }
        ]
    }
}

