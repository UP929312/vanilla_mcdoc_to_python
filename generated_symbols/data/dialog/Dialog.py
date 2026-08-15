"""
Generated from symbols.json for ::java::data::dialog::Dialog
Local link to file: generated_symbols/data/dialog/Dialog.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Literal

if TYPE_CHECKING:
    from generated_symbols.data.dialog.AfterAction import AfterAction
    from generated_symbols.data.dialog.Button import Button
    from generated_symbols.data.dialog.DialogListRef import DialogListRef
    from generated_symbols.data.dialog.body.DialogBody import DialogBody
    from generated_symbols.data.dialog.input.InputControl import InputControl
    from generated_symbols.util.text.Text import Text


@dataclass(kw_only=True)
class DialogConfirmationNone:
    type: Literal['minecraft:confirmation']
    yes: Button
    no: Button  # This action is also used for ESC-triggered exit.
    title: Text
    external_title: Text | None = None  # Name to be used for a button leading to this dialog. If not present, `title` will be used instead.
    body: DialogBody | list[DialogBody] | None = None
    inputs: list[InputControl] | None = None
    can_close_with_escape: bool | None = None  # Whether the dialog can be closed with ESC key. Defaults to `true`.
    after_action: AfterAction | None = None  # An additional operation performed on dialog after click or submit actions. Defaults to `close`.  Value `none` requires `pause` set to `false`.
    pause: bool | None = None  # Whether the dialog should pause the game in single-player mode. Defaults to `true`.


@dataclass(kw_only=True)
class DialogConfirmationClose:
    type: Literal['minecraft:confirmation']
    yes: Button
    no: Button  # This action is also used for ESC-triggered exit.
    title: Text
    external_title: Text | None = None  # Name to be used for a button leading to this dialog. If not present, `title` will be used instead.
    body: DialogBody | list[DialogBody] | None = None
    inputs: list[InputControl] | None = None
    can_close_with_escape: bool | None = None  # Whether the dialog can be closed with ESC key. Defaults to `true`.
    after_action: Literal['minecraft:close'] | None = None  # An additional operation performed on dialog after click or submit actions. Defaults to `close`.  Value `none` requires `pause` set to `false`.
    pause: bool | None = None  # Whether the dialog should pause the game in single-player mode. Defaults to `true`.


@dataclass(kw_only=True)
class DialogConfirmationNone2:
    type: Literal['minecraft:confirmation']
    yes: Button
    no: Button  # This action is also used for ESC-triggered exit.
    title: Text
    pause: Literal[False]  # Whether the dialog should pause the game in single-player mode. Defaults to `true`.  The currently selected `after_action` only supports the value `false`
    external_title: Text | None = None  # Name to be used for a button leading to this dialog. If not present, `title` will be used instead.
    body: DialogBody | list[DialogBody] | None = None
    inputs: list[InputControl] | None = None
    can_close_with_escape: bool | None = None  # Whether the dialog can be closed with ESC key. Defaults to `true`.
    after_action: Literal['minecraft:none'] | None = None  # An additional operation performed on dialog after click or submit actions. Defaults to `close`.  Value `none` requires `pause` set to `false`.


@dataclass(kw_only=True)
class DialogConfirmationWaitForResponse:
    type: Literal['minecraft:confirmation']
    yes: Button
    no: Button  # This action is also used for ESC-triggered exit.
    title: Text
    external_title: Text | None = None  # Name to be used for a button leading to this dialog. If not present, `title` will be used instead.
    body: DialogBody | list[DialogBody] | None = None
    inputs: list[InputControl] | None = None
    can_close_with_escape: bool | None = None  # Whether the dialog can be closed with ESC key. Defaults to `true`.
    after_action: Literal['minecraft:wait_for_response'] | None = None  # An additional operation performed on dialog after click or submit actions. Defaults to `close`.  Value `none` requires `pause` set to `false`.
    pause: bool | None = None  # Whether the dialog should pause the game in single-player mode. Defaults to `true`.


type DialogConfirmation = DialogConfirmationNone | DialogConfirmationClose | DialogConfirmationNone2 | DialogConfirmationWaitForResponse

@dataclass(kw_only=True)
class DialogDialogListNone:
    type: Literal['minecraft:dialog_list']
    dialogs: DialogListRef
    title: Text
    button_width: Annotated[int, 'Range | Min `1` and above | inclusive'] | None = None  # Width of buttons in the list. Defaults to 150.
    exit_action: Button | None = None  # The button in footer. The action is also used for ESC-triggered exit.
    columns: Annotated[int, 'Range | Min `1` and above | inclusive'] | None = None  # The number of columns. Defaults to 2.
    external_title: Text | None = None  # Name to be used for a button leading to this dialog. If not present, `title` will be used instead.
    body: DialogBody | list[DialogBody] | None = None
    inputs: list[InputControl] | None = None
    can_close_with_escape: bool | None = None  # Whether the dialog can be closed with ESC key. Defaults to `true`.
    after_action: AfterAction | None = None  # An additional operation performed on dialog after click or submit actions. Defaults to `close`.  Value `none` requires `pause` set to `false`.
    pause: bool | None = None  # Whether the dialog should pause the game in single-player mode. Defaults to `true`.


@dataclass(kw_only=True)
class DialogDialogListClose:
    type: Literal['minecraft:dialog_list']
    dialogs: DialogListRef
    title: Text
    button_width: Annotated[int, 'Range | Min `1` and above | inclusive'] | None = None  # Width of buttons in the list. Defaults to 150.
    exit_action: Button | None = None  # The button in footer. The action is also used for ESC-triggered exit.
    columns: Annotated[int, 'Range | Min `1` and above | inclusive'] | None = None  # The number of columns. Defaults to 2.
    external_title: Text | None = None  # Name to be used for a button leading to this dialog. If not present, `title` will be used instead.
    body: DialogBody | list[DialogBody] | None = None
    inputs: list[InputControl] | None = None
    can_close_with_escape: bool | None = None  # Whether the dialog can be closed with ESC key. Defaults to `true`.
    after_action: Literal['minecraft:close'] | None = None  # An additional operation performed on dialog after click or submit actions. Defaults to `close`.  Value `none` requires `pause` set to `false`.
    pause: bool | None = None  # Whether the dialog should pause the game in single-player mode. Defaults to `true`.


@dataclass(kw_only=True)
class DialogDialogListNone2:
    type: Literal['minecraft:dialog_list']
    dialogs: DialogListRef
    title: Text
    pause: Literal[False]  # Whether the dialog should pause the game in single-player mode. Defaults to `true`.  The currently selected `after_action` only supports the value `false`
    button_width: Annotated[int, 'Range | Min `1` and above | inclusive'] | None = None  # Width of buttons in the list. Defaults to 150.
    exit_action: Button | None = None  # The button in footer. The action is also used for ESC-triggered exit.
    columns: Annotated[int, 'Range | Min `1` and above | inclusive'] | None = None  # The number of columns. Defaults to 2.
    external_title: Text | None = None  # Name to be used for a button leading to this dialog. If not present, `title` will be used instead.
    body: DialogBody | list[DialogBody] | None = None
    inputs: list[InputControl] | None = None
    can_close_with_escape: bool | None = None  # Whether the dialog can be closed with ESC key. Defaults to `true`.
    after_action: Literal['minecraft:none'] | None = None  # An additional operation performed on dialog after click or submit actions. Defaults to `close`.  Value `none` requires `pause` set to `false`.


@dataclass(kw_only=True)
class DialogDialogListWaitForResponse:
    type: Literal['minecraft:dialog_list']
    dialogs: DialogListRef
    title: Text
    button_width: Annotated[int, 'Range | Min `1` and above | inclusive'] | None = None  # Width of buttons in the list. Defaults to 150.
    exit_action: Button | None = None  # The button in footer. The action is also used for ESC-triggered exit.
    columns: Annotated[int, 'Range | Min `1` and above | inclusive'] | None = None  # The number of columns. Defaults to 2.
    external_title: Text | None = None  # Name to be used for a button leading to this dialog. If not present, `title` will be used instead.
    body: DialogBody | list[DialogBody] | None = None
    inputs: list[InputControl] | None = None
    can_close_with_escape: bool | None = None  # Whether the dialog can be closed with ESC key. Defaults to `true`.
    after_action: Literal['minecraft:wait_for_response'] | None = None  # An additional operation performed on dialog after click or submit actions. Defaults to `close`.  Value `none` requires `pause` set to `false`.
    pause: bool | None = None  # Whether the dialog should pause the game in single-player mode. Defaults to `true`.


type DialogDialogList = DialogDialogListNone | DialogDialogListClose | DialogDialogListNone2 | DialogDialogListWaitForResponse

@dataclass(kw_only=True)
class DialogMultiActionNone:
    type: Literal['minecraft:multi_action']
    actions: Annotated[list[Button], 'Length = 1 (inclusive) and above']
    title: Text
    exit_action: Button | None = None  # The button in footer. The action is also used for ESC-triggered exit.
    columns: Annotated[int, 'Range | Min `1` and above | inclusive'] | None = None  # The number of columns. Defaults to 2.
    external_title: Text | None = None  # Name to be used for a button leading to this dialog. If not present, `title` will be used instead.
    body: DialogBody | list[DialogBody] | None = None
    inputs: list[InputControl] | None = None
    can_close_with_escape: bool | None = None  # Whether the dialog can be closed with ESC key. Defaults to `true`.
    after_action: AfterAction | None = None  # An additional operation performed on dialog after click or submit actions. Defaults to `close`.  Value `none` requires `pause` set to `false`.
    pause: bool | None = None  # Whether the dialog should pause the game in single-player mode. Defaults to `true`.


@dataclass(kw_only=True)
class DialogMultiActionClose:
    type: Literal['minecraft:multi_action']
    actions: Annotated[list[Button], 'Length = 1 (inclusive) and above']
    title: Text
    exit_action: Button | None = None  # The button in footer. The action is also used for ESC-triggered exit.
    columns: Annotated[int, 'Range | Min `1` and above | inclusive'] | None = None  # The number of columns. Defaults to 2.
    external_title: Text | None = None  # Name to be used for a button leading to this dialog. If not present, `title` will be used instead.
    body: DialogBody | list[DialogBody] | None = None
    inputs: list[InputControl] | None = None
    can_close_with_escape: bool | None = None  # Whether the dialog can be closed with ESC key. Defaults to `true`.
    after_action: Literal['minecraft:close'] | None = None  # An additional operation performed on dialog after click or submit actions. Defaults to `close`.  Value `none` requires `pause` set to `false`.
    pause: bool | None = None  # Whether the dialog should pause the game in single-player mode. Defaults to `true`.


@dataclass(kw_only=True)
class DialogMultiActionNone2:
    type: Literal['minecraft:multi_action']
    actions: Annotated[list[Button], 'Length = 1 (inclusive) and above']
    title: Text
    pause: Literal[False]  # Whether the dialog should pause the game in single-player mode. Defaults to `true`.  The currently selected `after_action` only supports the value `false`
    exit_action: Button | None = None  # The button in footer. The action is also used for ESC-triggered exit.
    columns: Annotated[int, 'Range | Min `1` and above | inclusive'] | None = None  # The number of columns. Defaults to 2.
    external_title: Text | None = None  # Name to be used for a button leading to this dialog. If not present, `title` will be used instead.
    body: DialogBody | list[DialogBody] | None = None
    inputs: list[InputControl] | None = None
    can_close_with_escape: bool | None = None  # Whether the dialog can be closed with ESC key. Defaults to `true`.
    after_action: Literal['minecraft:none'] | None = None  # An additional operation performed on dialog after click or submit actions. Defaults to `close`.  Value `none` requires `pause` set to `false`.


@dataclass(kw_only=True)
class DialogMultiActionWaitForResponse:
    type: Literal['minecraft:multi_action']
    actions: Annotated[list[Button], 'Length = 1 (inclusive) and above']
    title: Text
    exit_action: Button | None = None  # The button in footer. The action is also used for ESC-triggered exit.
    columns: Annotated[int, 'Range | Min `1` and above | inclusive'] | None = None  # The number of columns. Defaults to 2.
    external_title: Text | None = None  # Name to be used for a button leading to this dialog. If not present, `title` will be used instead.
    body: DialogBody | list[DialogBody] | None = None
    inputs: list[InputControl] | None = None
    can_close_with_escape: bool | None = None  # Whether the dialog can be closed with ESC key. Defaults to `true`.
    after_action: Literal['minecraft:wait_for_response'] | None = None  # An additional operation performed on dialog after click or submit actions. Defaults to `close`.  Value `none` requires `pause` set to `false`.
    pause: bool | None = None  # Whether the dialog should pause the game in single-player mode. Defaults to `true`.


type DialogMultiAction = DialogMultiActionNone | DialogMultiActionClose | DialogMultiActionNone2 | DialogMultiActionWaitForResponse

@dataclass(kw_only=True)
class DialogNoticeNone:
    type: Literal['minecraft:notice']
    title: Text
    action: Button | None = None  # The only action in footer. Defaults to `gui.ok` label with no action or tooltip.
    external_title: Text | None = None  # Name to be used for a button leading to this dialog. If not present, `title` will be used instead.
    body: DialogBody | list[DialogBody] | None = None
    inputs: list[InputControl] | None = None
    can_close_with_escape: bool | None = None  # Whether the dialog can be closed with ESC key. Defaults to `true`.
    after_action: AfterAction | None = None  # An additional operation performed on dialog after click or submit actions. Defaults to `close`.  Value `none` requires `pause` set to `false`.
    pause: bool | None = None  # Whether the dialog should pause the game in single-player mode. Defaults to `true`.


@dataclass(kw_only=True)
class DialogNoticeClose:
    type: Literal['minecraft:notice']
    title: Text
    action: Button | None = None  # The only action in footer. Defaults to `gui.ok` label with no action or tooltip.
    external_title: Text | None = None  # Name to be used for a button leading to this dialog. If not present, `title` will be used instead.
    body: DialogBody | list[DialogBody] | None = None
    inputs: list[InputControl] | None = None
    can_close_with_escape: bool | None = None  # Whether the dialog can be closed with ESC key. Defaults to `true`.
    after_action: Literal['minecraft:close'] | None = None  # An additional operation performed on dialog after click or submit actions. Defaults to `close`.  Value `none` requires `pause` set to `false`.
    pause: bool | None = None  # Whether the dialog should pause the game in single-player mode. Defaults to `true`.


@dataclass(kw_only=True)
class DialogNoticeNone2:
    type: Literal['minecraft:notice']
    title: Text
    pause: Literal[False]  # Whether the dialog should pause the game in single-player mode. Defaults to `true`.  The currently selected `after_action` only supports the value `false`
    action: Button | None = None  # The only action in footer. Defaults to `gui.ok` label with no action or tooltip.
    external_title: Text | None = None  # Name to be used for a button leading to this dialog. If not present, `title` will be used instead.
    body: DialogBody | list[DialogBody] | None = None
    inputs: list[InputControl] | None = None
    can_close_with_escape: bool | None = None  # Whether the dialog can be closed with ESC key. Defaults to `true`.
    after_action: Literal['minecraft:none'] | None = None  # An additional operation performed on dialog after click or submit actions. Defaults to `close`.  Value `none` requires `pause` set to `false`.


@dataclass(kw_only=True)
class DialogNoticeWaitForResponse:
    type: Literal['minecraft:notice']
    title: Text
    action: Button | None = None  # The only action in footer. Defaults to `gui.ok` label with no action or tooltip.
    external_title: Text | None = None  # Name to be used for a button leading to this dialog. If not present, `title` will be used instead.
    body: DialogBody | list[DialogBody] | None = None
    inputs: list[InputControl] | None = None
    can_close_with_escape: bool | None = None  # Whether the dialog can be closed with ESC key. Defaults to `true`.
    after_action: Literal['minecraft:wait_for_response'] | None = None  # An additional operation performed on dialog after click or submit actions. Defaults to `close`.  Value `none` requires `pause` set to `false`.
    pause: bool | None = None  # Whether the dialog should pause the game in single-player mode. Defaults to `true`.


type DialogNotice = DialogNoticeNone | DialogNoticeClose | DialogNoticeNone2 | DialogNoticeWaitForResponse

@dataclass(kw_only=True)
class DialogServerLinksNone:
    type: Literal['minecraft:server_links']
    title: Text
    button_width: Annotated[int, 'Range | Min `1` and above | inclusive'] | None = None  # Width of buttons in the list. Defaults to 150.
    exit_action: Button | None = None  # The button in footer. The action is also used for ESC-triggered exit.
    columns: Annotated[int, 'Range | Min `1` and above | inclusive'] | None = None  # The number of columns. Defaults to 2.
    external_title: Text | None = None  # Name to be used for a button leading to this dialog. If not present, `title` will be used instead.
    body: DialogBody | list[DialogBody] | None = None
    inputs: list[InputControl] | None = None
    can_close_with_escape: bool | None = None  # Whether the dialog can be closed with ESC key. Defaults to `true`.
    after_action: AfterAction | None = None  # An additional operation performed on dialog after click or submit actions. Defaults to `close`.  Value `none` requires `pause` set to `false`.
    pause: bool | None = None  # Whether the dialog should pause the game in single-player mode. Defaults to `true`.


@dataclass(kw_only=True)
class DialogServerLinksClose:
    type: Literal['minecraft:server_links']
    title: Text
    button_width: Annotated[int, 'Range | Min `1` and above | inclusive'] | None = None  # Width of buttons in the list. Defaults to 150.
    exit_action: Button | None = None  # The button in footer. The action is also used for ESC-triggered exit.
    columns: Annotated[int, 'Range | Min `1` and above | inclusive'] | None = None  # The number of columns. Defaults to 2.
    external_title: Text | None = None  # Name to be used for a button leading to this dialog. If not present, `title` will be used instead.
    body: DialogBody | list[DialogBody] | None = None
    inputs: list[InputControl] | None = None
    can_close_with_escape: bool | None = None  # Whether the dialog can be closed with ESC key. Defaults to `true`.
    after_action: Literal['minecraft:close'] | None = None  # An additional operation performed on dialog after click or submit actions. Defaults to `close`.  Value `none` requires `pause` set to `false`.
    pause: bool | None = None  # Whether the dialog should pause the game in single-player mode. Defaults to `true`.


@dataclass(kw_only=True)
class DialogServerLinksNone2:
    type: Literal['minecraft:server_links']
    title: Text
    pause: Literal[False]  # Whether the dialog should pause the game in single-player mode. Defaults to `true`.  The currently selected `after_action` only supports the value `false`
    button_width: Annotated[int, 'Range | Min `1` and above | inclusive'] | None = None  # Width of buttons in the list. Defaults to 150.
    exit_action: Button | None = None  # The button in footer. The action is also used for ESC-triggered exit.
    columns: Annotated[int, 'Range | Min `1` and above | inclusive'] | None = None  # The number of columns. Defaults to 2.
    external_title: Text | None = None  # Name to be used for a button leading to this dialog. If not present, `title` will be used instead.
    body: DialogBody | list[DialogBody] | None = None
    inputs: list[InputControl] | None = None
    can_close_with_escape: bool | None = None  # Whether the dialog can be closed with ESC key. Defaults to `true`.
    after_action: Literal['minecraft:none'] | None = None  # An additional operation performed on dialog after click or submit actions. Defaults to `close`.  Value `none` requires `pause` set to `false`.


@dataclass(kw_only=True)
class DialogServerLinksWaitForResponse:
    type: Literal['minecraft:server_links']
    title: Text
    button_width: Annotated[int, 'Range | Min `1` and above | inclusive'] | None = None  # Width of buttons in the list. Defaults to 150.
    exit_action: Button | None = None  # The button in footer. The action is also used for ESC-triggered exit.
    columns: Annotated[int, 'Range | Min `1` and above | inclusive'] | None = None  # The number of columns. Defaults to 2.
    external_title: Text | None = None  # Name to be used for a button leading to this dialog. If not present, `title` will be used instead.
    body: DialogBody | list[DialogBody] | None = None
    inputs: list[InputControl] | None = None
    can_close_with_escape: bool | None = None  # Whether the dialog can be closed with ESC key. Defaults to `true`.
    after_action: Literal['minecraft:wait_for_response'] | None = None  # An additional operation performed on dialog after click or submit actions. Defaults to `close`.  Value `none` requires `pause` set to `false`.
    pause: bool | None = None  # Whether the dialog should pause the game in single-player mode. Defaults to `true`.


type DialogServerLinks = DialogServerLinksNone | DialogServerLinksClose | DialogServerLinksNone2 | DialogServerLinksWaitForResponse

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

