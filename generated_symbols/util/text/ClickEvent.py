"""
Generated from symbols.json for ::java::util::text::ClickEvent
Local link to file: generated_symbols/util/text/ClickEvent.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Literal

from generated_symbols.util.text.ChangePage import ChangePage
from generated_symbols.util.text.CopyToClipboard import CopyToClipboard
from generated_symbols.util.text.CustomAction import CustomAction
from generated_symbols.util.text.OpenUrl import OpenUrl
from generated_symbols.util.text.RunCommand import RunCommand
from generated_symbols.util.text.ShowDialog import ShowDialog
from generated_symbols.util.text.SuggestCommand import SuggestCommand


@dataclass(kw_only=True)
class ClickEventChangePage(ChangePage):
    action: Literal['minecraft:change_page']


@dataclass(kw_only=True)
class ClickEventCopyToClipboard(CopyToClipboard):
    action: Literal['minecraft:copy_to_clipboard']


@dataclass(kw_only=True)
class ClickEventCustom(CustomAction):
    action: Literal['minecraft:custom']


@dataclass(kw_only=True)
class ClickEventOpenUrl(OpenUrl):
    action: Literal['minecraft:open_url']


@dataclass(kw_only=True)
class ClickEventRunCommand(RunCommand):
    action: Literal['minecraft:run_command']


@dataclass(kw_only=True)
class ClickEventShowDialog(ShowDialog):
    action: Literal['minecraft:show_dialog']


@dataclass(kw_only=True)
class ClickEventSuggestCommand(SuggestCommand):
    action: Literal['minecraft:suggest_command']


type ClickEvent = ClickEventChangePage | ClickEventCopyToClipboard | ClickEventCustom | ClickEventOpenUrl | ClickEventRunCommand | ClickEventShowDialog | ClickEventSuggestCommand


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::text::ClickEvent": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "action",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::text::ClickEventAction"
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
                                "action"
                            ]
                        }
                    ],
                    "registry": "minecraft:click_event"
                }
            }
        ]
    }
}

