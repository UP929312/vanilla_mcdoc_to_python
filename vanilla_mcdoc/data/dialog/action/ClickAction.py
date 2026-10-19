"""
Generated from symbols.json for ::java::data::dialog::action::ClickAction
Local link to file: vanilla_mcdoc/data/dialog/action/ClickAction.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from pydantic import Discriminator, Tag

from vanilla_mcdoc.base import tag_of
from vanilla_mcdoc.data.dialog.action.DynamicCustomAction import DynamicCustomAction
from vanilla_mcdoc.data.dialog.action.DynamicRunCommand import DynamicRunCommand
from vanilla_mcdoc.util.text.ChangePage import ChangePage
from vanilla_mcdoc.util.text.CopyToClipboard import CopyToClipboard
from vanilla_mcdoc.util.text.CustomAction import CustomAction
from vanilla_mcdoc.util.text.OpenUrl import OpenUrl
from vanilla_mcdoc.util.text.RunCommand import RunCommand
from vanilla_mcdoc.util.text.ShowDialog import ShowDialog
from vanilla_mcdoc.util.text.SuggestCommand import SuggestCommand


class ClickActionChangePage(ChangePage):
    type: Literal['minecraft:change_page', 'change_page'] = 'minecraft:change_page'


class ClickActionCopyToClipboard(CopyToClipboard):
    type: Literal['minecraft:copy_to_clipboard', 'copy_to_clipboard'] = 'minecraft:copy_to_clipboard'


class ClickActionCustom(CustomAction):
    type: Literal['minecraft:custom', 'custom'] = 'minecraft:custom'


class ClickActionDynamicCustom(DynamicCustomAction):
    type: Literal['minecraft:dynamic/custom', 'dynamic/custom'] = 'minecraft:dynamic/custom'


class ClickActionDynamicRunCommand(DynamicRunCommand):
    type: Literal['minecraft:dynamic/run_command', 'dynamic/run_command'] = 'minecraft:dynamic/run_command'


class ClickActionOpenUrl(OpenUrl):
    type: Literal['minecraft:open_url', 'open_url'] = 'minecraft:open_url'


class ClickActionRunCommand(RunCommand):
    type: Literal['minecraft:run_command', 'run_command'] = 'minecraft:run_command'


class ClickActionShowDialog(ShowDialog):
    type: Literal['minecraft:show_dialog', 'show_dialog'] = 'minecraft:show_dialog'


class ClickActionSuggestCommand(SuggestCommand):
    type: Literal['minecraft:suggest_command', 'suggest_command'] = 'minecraft:suggest_command'


type ClickAction = Annotated[
    Annotated[ClickActionChangePage, Tag('minecraft:change_page')]
    | Annotated[ClickActionCopyToClipboard, Tag('minecraft:copy_to_clipboard')]
    | Annotated[ClickActionCustom, Tag('minecraft:custom')]
    | Annotated[ClickActionDynamicCustom, Tag('minecraft:dynamic/custom')]
    | Annotated[ClickActionDynamicRunCommand, Tag('minecraft:dynamic/run_command')]
    | Annotated[ClickActionOpenUrl, Tag('minecraft:open_url')]
    | Annotated[ClickActionRunCommand, Tag('minecraft:run_command')]
    | Annotated[ClickActionShowDialog, Tag('minecraft:show_dialog')]
    | Annotated[ClickActionSuggestCommand, Tag('minecraft:suggest_command')],
    Discriminator(tag_of('type')),
]
