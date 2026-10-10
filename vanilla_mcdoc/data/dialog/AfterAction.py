"""
Generated from symbols.json for ::java::data::dialog::AfterAction
Local link to file: vanilla_mcdoc/data/dialog/AfterAction.py
"""
# ~~~ CODE ~~~
from enum import StrEnum


class AfterAction(StrEnum):
    CLOSE = "close"  # Closes the dialog. Returns to the previous non-dialog screen, if any.
    NONE = "none"  # Does nothing. Only available if `pause` is set to `false`.
    WAITFORRESPONSE = "wait_for_response"  # Replaces the dialog with a "Waiting for Response" screen. The waiting screen unpauses the game in single-player mode.
