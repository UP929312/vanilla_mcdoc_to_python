"""
Generated from symbols.json for ::java::util::text::ClickEventAction
Local link to file: vanilla_mcdoc/util/text/ClickEventAction.py
"""
# ~~~ CODE ~~~
from enum import StrEnum


class ClickEventAction(StrEnum):
    OPENURL = "open_url"
    RUNCOMMAND = "run_command"
    SUGGESTCOMMAND = "suggest_command"
    CHANGEPAGE = "change_page"
    COPYTOCLIPBOARD = "copy_to_clipboard"
    SHOWDIALOG = "show_dialog"
    CUSTOM = "custom"
