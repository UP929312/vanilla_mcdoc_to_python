"""
Generated from symbols.json for ::java::data::dialog::action::ClickAction
Local link to file: generated_symbols/data/dialog/action/ClickAction.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Literal

from generated_symbols.data.dialog.action.DynamicCustomAction import DynamicCustomAction
from generated_symbols.data.dialog.action.DynamicRunCommand import DynamicRunCommand
from generated_symbols.util.text.ChangePage import ChangePage
from generated_symbols.util.text.CopyToClipboard import CopyToClipboard
from generated_symbols.util.text.CustomAction import CustomAction
from generated_symbols.util.text.OpenUrl import OpenUrl
from generated_symbols.util.text.RunCommand import RunCommand
from generated_symbols.util.text.ShowDialog import ShowDialog
from generated_symbols.util.text.SuggestCommand import SuggestCommand


@dataclass(kw_only=True)
class ClickActionChangePage(ChangePage):
    type: Literal['minecraft:change_page']


@dataclass(kw_only=True)
class ClickActionCopyToClipboard(CopyToClipboard):
    type: Literal['minecraft:copy_to_clipboard']


@dataclass(kw_only=True)
class ClickActionCustom(CustomAction):
    type: Literal['minecraft:custom']


@dataclass(kw_only=True)
class ClickActionDynamicCustom(DynamicCustomAction):
    type: Literal['minecraft:dynamic/custom']


@dataclass(kw_only=True)
class ClickActionDynamicRunCommand(DynamicRunCommand):
    type: Literal['minecraft:dynamic/run_command']


@dataclass(kw_only=True)
class ClickActionOpenUrl(OpenUrl):
    type: Literal['minecraft:open_url']


@dataclass(kw_only=True)
class ClickActionRunCommand(RunCommand):
    type: Literal['minecraft:run_command']


@dataclass(kw_only=True)
class ClickActionShowDialog(ShowDialog):
    type: Literal['minecraft:show_dialog']


@dataclass(kw_only=True)
class ClickActionSuggestCommand(SuggestCommand):
    type: Literal['minecraft:suggest_command']


type ClickAction = ClickActionChangePage | ClickActionCopyToClipboard | ClickActionCustom | ClickActionDynamicCustom | ClickActionDynamicRunCommand | ClickActionOpenUrl | ClickActionRunCommand | ClickActionShowDialog | ClickActionSuggestCommand


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::dialog::action::ClickAction": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "type",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "dialog_action_type"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "dynamic",
                            "accessor": [
                                "type"
                            ]
                        }
                    ],
                    "registry": "minecraft:dialog_action"
                }
            }
        ]
    }
}

