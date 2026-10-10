"""
Generated from symbols.json for ::java::util::text::ClickEvent
Local link to file: vanilla_mcdoc/util/text/ClickEvent.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from pydantic import Field

from vanilla_mcdoc.util.text.ChangePage import ChangePage
from vanilla_mcdoc.util.text.CopyToClipboard import CopyToClipboard
from vanilla_mcdoc.util.text.CustomAction import CustomAction
from vanilla_mcdoc.util.text.OpenUrl import OpenUrl
from vanilla_mcdoc.util.text.RunCommand import RunCommand
from vanilla_mcdoc.util.text.ShowDialog import ShowDialog
from vanilla_mcdoc.util.text.SuggestCommand import SuggestCommand


class ClickEventChangePage(ChangePage):
    action: Literal['minecraft:change_page', 'change_page'] = 'minecraft:change_page'


class ClickEventCopyToClipboard(CopyToClipboard):
    action: Literal['minecraft:copy_to_clipboard', 'copy_to_clipboard'] = 'minecraft:copy_to_clipboard'


class ClickEventCustom(CustomAction):
    action: Literal['minecraft:custom', 'custom'] = 'minecraft:custom'


class ClickEventOpenUrl(OpenUrl):
    action: Literal['minecraft:open_url', 'open_url'] = 'minecraft:open_url'


class ClickEventRunCommand(RunCommand):
    action: Literal['minecraft:run_command', 'run_command'] = 'minecraft:run_command'


class ClickEventShowDialog(ShowDialog):
    action: Literal['minecraft:show_dialog', 'show_dialog'] = 'minecraft:show_dialog'


class ClickEventSuggestCommand(SuggestCommand):
    action: Literal['minecraft:suggest_command', 'suggest_command'] = 'minecraft:suggest_command'


type ClickEvent = Annotated[
    ClickEventChangePage | ClickEventCopyToClipboard | ClickEventCustom | ClickEventOpenUrl | ClickEventRunCommand | ClickEventShowDialog | ClickEventSuggestCommand,
    Field(discriminator='action'),
]
