# Generated from symbols.json for ::java::data::dialog::Dialog
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Literal

from generated_symbols.data.dialog.ButtonListDialogBase import ButtonListDialogBase
from generated_symbols.data.dialog.DialogBase import DialogBase
from generated_symbols.data.dialog.ListDialogBase import ListDialogBase

if TYPE_CHECKING:
    from generated_symbols.data.dialog.Button import Button
    from generated_symbols.data.dialog.DialogListRef import DialogListRef


@dataclass(kw_only=True)
class DialogConfirmation(DialogBase):
    type: Literal['minecraft:confirmation']
    yes: Button
    no: Button  # This action is also used for ESC-triggered exit.


@dataclass(kw_only=True)
class DialogDialogList(ButtonListDialogBase):
    type: Literal['minecraft:dialog_list']
    dialogs: DialogListRef


@dataclass(kw_only=True)
class DialogMultiAction(ListDialogBase):
    type: Literal['minecraft:multi_action']
    actions: Annotated[list[Button], 'Length = 1 (inclusive) and above']


@dataclass(kw_only=True)
class DialogNotice(DialogBase):
    type: Literal['minecraft:notice']
    action: Button | None = None  # The only action in footer. Defaults to `gui.ok` label with no action or tooltip.


@dataclass(kw_only=True)
class DialogServerLinks(ButtonListDialogBase):
    type: Literal['minecraft:server_links']


type Dialog = DialogConfirmation | DialogDialogList | DialogMultiAction | DialogNotice | DialogServerLinks


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::dialog::Dialog": {
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
                                    "value": "dialog_type"
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
                    "registry": "minecraft:dialog"
                }
            }
        ]
    }
}

