"""Vanilla's data/dialog/ files"""
from vanilla_mcdoc.data.dialog.Button import Button
from vanilla_mcdoc.data.dialog.Dialog import DialogDialogListDefault, DialogServerLinksDefault
from vanilla_mcdoc.util.text.TextObject import TextObjectStruct2

CUSTOM_OPTIONS = DialogDialogListDefault(
    type='minecraft:dialog_list',
    dialogs='#minecraft:pause_screen_additions',
    button_width=310,
    exit_action=Button(label=TextObjectStruct2(translate='gui.back'), width=200),
    columns=1,
    title=TextObjectStruct2(translate='menu.custom_options.title'),
    external_title=TextObjectStruct2(translate='menu.custom_options'),
)

QUICK_ACTIONS = DialogDialogListDefault(
    type='minecraft:dialog_list',
    dialogs='#minecraft:quick_actions',
    button_width=310,
    exit_action=Button(label=TextObjectStruct2(translate='gui.back'), width=200),
    columns=1,
    title=TextObjectStruct2(translate='menu.quick_actions.title'),
    external_title=TextObjectStruct2(translate='menu.quick_actions'),
)

SERVER_LINKS = DialogServerLinksDefault(
    type='minecraft:server_links',
    button_width=310,
    exit_action=Button(label=TextObjectStruct2(translate='gui.back'), width=200),
    columns=1,
    title=TextObjectStruct2(translate='menu.server_links.title'),
    external_title=TextObjectStruct2(translate='menu.server_links'),
)
