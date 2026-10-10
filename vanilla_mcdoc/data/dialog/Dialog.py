"""
Generated from symbols.json for ::java::data::dialog::Dialog
Local link to file: vanilla_mcdoc/data/dialog/Dialog.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar, Literal

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.dialog.AfterAction import AfterAction
    from vanilla_mcdoc.data.dialog.Button import Button
    from vanilla_mcdoc.data.dialog.DialogListRef import DialogListRef
    from vanilla_mcdoc.data.dialog.body.DialogBody import DialogBody
    from vanilla_mcdoc.data.dialog.input.InputControl import InputControl
    from vanilla_mcdoc.util.text.Text import Text


class DialogConfirmationDefault(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'dialog'

    type: Literal['minecraft:confirmation', 'confirmation'] = 'minecraft:confirmation'
    yes: Button
    no: Button  # This action is also used for ESC-triggered exit.
    title: Text
    external_title: Text | None = None  # Name to be used for a button leading to this dialog. If not present, `title` will be used instead.
    body: DialogBody | list[DialogBody] | None = None
    inputs: list[InputControl] | None = None
    can_close_with_escape: bool | None = None  # Whether the dialog can be closed with ESC key. Defaults to `true`.
    after_action: AfterAction | None = None  # An additional operation performed on dialog after click or submit actions. Defaults to `close`.  Value `none` requires `pause` set to `false`.
    pause: bool | None = None  # Whether the dialog should pause the game in single-player mode. Defaults to `true`.


class DialogConfirmationClose(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'dialog'

    type: Literal['minecraft:confirmation', 'confirmation'] = 'minecraft:confirmation'
    yes: Button
    no: Button  # This action is also used for ESC-triggered exit.
    title: Text
    external_title: Text | None = None  # Name to be used for a button leading to this dialog. If not present, `title` will be used instead.
    body: DialogBody | list[DialogBody] | None = None
    inputs: list[InputControl] | None = None
    can_close_with_escape: bool | None = None  # Whether the dialog can be closed with ESC key. Defaults to `true`.
    after_action: Literal['minecraft:close', 'close'] | None = 'minecraft:close'  # An additional operation performed on dialog after click or submit actions. Defaults to `close`.  Value `none` requires `pause` set to `false`.
    pause: bool | None = None  # Whether the dialog should pause the game in single-player mode. Defaults to `true`.


class DialogConfirmationNone(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'dialog'

    type: Literal['minecraft:confirmation', 'confirmation'] = 'minecraft:confirmation'
    yes: Button
    no: Button  # This action is also used for ESC-triggered exit.
    title: Text
    external_title: Text | None = None  # Name to be used for a button leading to this dialog. If not present, `title` will be used instead.
    body: DialogBody | list[DialogBody] | None = None
    inputs: list[InputControl] | None = None
    can_close_with_escape: bool | None = None  # Whether the dialog can be closed with ESC key. Defaults to `true`.
    after_action: Literal['minecraft:none', 'none'] | None = 'minecraft:none'  # An additional operation performed on dialog after click or submit actions. Defaults to `close`.  Value `none` requires `pause` set to `false`.
    pause: Literal[False] = False  # Whether the dialog should pause the game in single-player mode. Defaults to `true`.  The currently selected `after_action` only supports the value `false`


class DialogConfirmationWaitForResponse(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'dialog'

    type: Literal['minecraft:confirmation', 'confirmation'] = 'minecraft:confirmation'
    yes: Button
    no: Button  # This action is also used for ESC-triggered exit.
    title: Text
    external_title: Text | None = None  # Name to be used for a button leading to this dialog. If not present, `title` will be used instead.
    body: DialogBody | list[DialogBody] | None = None
    inputs: list[InputControl] | None = None
    can_close_with_escape: bool | None = None  # Whether the dialog can be closed with ESC key. Defaults to `true`.
    after_action: Literal['minecraft:wait_for_response', 'wait_for_response'] | None = 'minecraft:wait_for_response'  # An additional operation performed on dialog after click or submit actions. Defaults to `close`.  Value `none` requires `pause` set to `false`.
    pause: bool | None = None  # Whether the dialog should pause the game in single-player mode. Defaults to `true`.


type DialogConfirmation = DialogConfirmationDefault | DialogConfirmationClose | DialogConfirmationNone | DialogConfirmationWaitForResponse


class DialogDialogListDefault(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'dialog'

    type: Literal['minecraft:dialog_list', 'dialog_list'] = 'minecraft:dialog_list'
    dialogs: DialogListRef
    button_width: Annotated[int, Field(ge=1)] | None = None  # Width of buttons in the list. Defaults to 150.
    exit_action: Button | None = None  # The button in footer. The action is also used for ESC-triggered exit.
    columns: Annotated[int, Field(ge=1)] | None = None  # The number of columns. Defaults to 2.
    title: Text
    external_title: Text | None = None  # Name to be used for a button leading to this dialog. If not present, `title` will be used instead.
    body: DialogBody | list[DialogBody] | None = None
    inputs: list[InputControl] | None = None
    can_close_with_escape: bool | None = None  # Whether the dialog can be closed with ESC key. Defaults to `true`.
    after_action: AfterAction | None = None  # An additional operation performed on dialog after click or submit actions. Defaults to `close`.  Value `none` requires `pause` set to `false`.
    pause: bool | None = None  # Whether the dialog should pause the game in single-player mode. Defaults to `true`.


class DialogDialogListClose(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'dialog'

    type: Literal['minecraft:dialog_list', 'dialog_list'] = 'minecraft:dialog_list'
    dialogs: DialogListRef
    button_width: Annotated[int, Field(ge=1)] | None = None  # Width of buttons in the list. Defaults to 150.
    exit_action: Button | None = None  # The button in footer. The action is also used for ESC-triggered exit.
    columns: Annotated[int, Field(ge=1)] | None = None  # The number of columns. Defaults to 2.
    title: Text
    external_title: Text | None = None  # Name to be used for a button leading to this dialog. If not present, `title` will be used instead.
    body: DialogBody | list[DialogBody] | None = None
    inputs: list[InputControl] | None = None
    can_close_with_escape: bool | None = None  # Whether the dialog can be closed with ESC key. Defaults to `true`.
    after_action: Literal['minecraft:close', 'close'] | None = 'minecraft:close'  # An additional operation performed on dialog after click or submit actions. Defaults to `close`.  Value `none` requires `pause` set to `false`.
    pause: bool | None = None  # Whether the dialog should pause the game in single-player mode. Defaults to `true`.


class DialogDialogListNone(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'dialog'

    type: Literal['minecraft:dialog_list', 'dialog_list'] = 'minecraft:dialog_list'
    dialogs: DialogListRef
    button_width: Annotated[int, Field(ge=1)] | None = None  # Width of buttons in the list. Defaults to 150.
    exit_action: Button | None = None  # The button in footer. The action is also used for ESC-triggered exit.
    columns: Annotated[int, Field(ge=1)] | None = None  # The number of columns. Defaults to 2.
    title: Text
    external_title: Text | None = None  # Name to be used for a button leading to this dialog. If not present, `title` will be used instead.
    body: DialogBody | list[DialogBody] | None = None
    inputs: list[InputControl] | None = None
    can_close_with_escape: bool | None = None  # Whether the dialog can be closed with ESC key. Defaults to `true`.
    after_action: Literal['minecraft:none', 'none'] | None = 'minecraft:none'  # An additional operation performed on dialog after click or submit actions. Defaults to `close`.  Value `none` requires `pause` set to `false`.
    pause: Literal[False] = False  # Whether the dialog should pause the game in single-player mode. Defaults to `true`.  The currently selected `after_action` only supports the value `false`


class DialogDialogListWaitForResponse(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'dialog'

    type: Literal['minecraft:dialog_list', 'dialog_list'] = 'minecraft:dialog_list'
    dialogs: DialogListRef
    button_width: Annotated[int, Field(ge=1)] | None = None  # Width of buttons in the list. Defaults to 150.
    exit_action: Button | None = None  # The button in footer. The action is also used for ESC-triggered exit.
    columns: Annotated[int, Field(ge=1)] | None = None  # The number of columns. Defaults to 2.
    title: Text
    external_title: Text | None = None  # Name to be used for a button leading to this dialog. If not present, `title` will be used instead.
    body: DialogBody | list[DialogBody] | None = None
    inputs: list[InputControl] | None = None
    can_close_with_escape: bool | None = None  # Whether the dialog can be closed with ESC key. Defaults to `true`.
    after_action: Literal['minecraft:wait_for_response', 'wait_for_response'] | None = 'minecraft:wait_for_response'  # An additional operation performed on dialog after click or submit actions. Defaults to `close`.  Value `none` requires `pause` set to `false`.
    pause: bool | None = None  # Whether the dialog should pause the game in single-player mode. Defaults to `true`.


type DialogDialogList = DialogDialogListDefault | DialogDialogListClose | DialogDialogListNone | DialogDialogListWaitForResponse


class DialogMultiActionDefault(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'dialog'

    type: Literal['minecraft:multi_action', 'multi_action'] = 'minecraft:multi_action'
    actions: Annotated[list[Button], Field(min_length=1)]
    exit_action: Button | None = None  # The button in footer. The action is also used for ESC-triggered exit.
    columns: Annotated[int, Field(ge=1)] | None = None  # The number of columns. Defaults to 2.
    title: Text
    external_title: Text | None = None  # Name to be used for a button leading to this dialog. If not present, `title` will be used instead.
    body: DialogBody | list[DialogBody] | None = None
    inputs: list[InputControl] | None = None
    can_close_with_escape: bool | None = None  # Whether the dialog can be closed with ESC key. Defaults to `true`.
    after_action: AfterAction | None = None  # An additional operation performed on dialog after click or submit actions. Defaults to `close`.  Value `none` requires `pause` set to `false`.
    pause: bool | None = None  # Whether the dialog should pause the game in single-player mode. Defaults to `true`.


class DialogMultiActionClose(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'dialog'

    type: Literal['minecraft:multi_action', 'multi_action'] = 'minecraft:multi_action'
    actions: Annotated[list[Button], Field(min_length=1)]
    exit_action: Button | None = None  # The button in footer. The action is also used for ESC-triggered exit.
    columns: Annotated[int, Field(ge=1)] | None = None  # The number of columns. Defaults to 2.
    title: Text
    external_title: Text | None = None  # Name to be used for a button leading to this dialog. If not present, `title` will be used instead.
    body: DialogBody | list[DialogBody] | None = None
    inputs: list[InputControl] | None = None
    can_close_with_escape: bool | None = None  # Whether the dialog can be closed with ESC key. Defaults to `true`.
    after_action: Literal['minecraft:close', 'close'] | None = 'minecraft:close'  # An additional operation performed on dialog after click or submit actions. Defaults to `close`.  Value `none` requires `pause` set to `false`.
    pause: bool | None = None  # Whether the dialog should pause the game in single-player mode. Defaults to `true`.


class DialogMultiActionNone(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'dialog'

    type: Literal['minecraft:multi_action', 'multi_action'] = 'minecraft:multi_action'
    actions: Annotated[list[Button], Field(min_length=1)]
    exit_action: Button | None = None  # The button in footer. The action is also used for ESC-triggered exit.
    columns: Annotated[int, Field(ge=1)] | None = None  # The number of columns. Defaults to 2.
    title: Text
    external_title: Text | None = None  # Name to be used for a button leading to this dialog. If not present, `title` will be used instead.
    body: DialogBody | list[DialogBody] | None = None
    inputs: list[InputControl] | None = None
    can_close_with_escape: bool | None = None  # Whether the dialog can be closed with ESC key. Defaults to `true`.
    after_action: Literal['minecraft:none', 'none'] | None = 'minecraft:none'  # An additional operation performed on dialog after click or submit actions. Defaults to `close`.  Value `none` requires `pause` set to `false`.
    pause: Literal[False] = False  # Whether the dialog should pause the game in single-player mode. Defaults to `true`.  The currently selected `after_action` only supports the value `false`


class DialogMultiActionWaitForResponse(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'dialog'

    type: Literal['minecraft:multi_action', 'multi_action'] = 'minecraft:multi_action'
    actions: Annotated[list[Button], Field(min_length=1)]
    exit_action: Button | None = None  # The button in footer. The action is also used for ESC-triggered exit.
    columns: Annotated[int, Field(ge=1)] | None = None  # The number of columns. Defaults to 2.
    title: Text
    external_title: Text | None = None  # Name to be used for a button leading to this dialog. If not present, `title` will be used instead.
    body: DialogBody | list[DialogBody] | None = None
    inputs: list[InputControl] | None = None
    can_close_with_escape: bool | None = None  # Whether the dialog can be closed with ESC key. Defaults to `true`.
    after_action: Literal['minecraft:wait_for_response', 'wait_for_response'] | None = 'minecraft:wait_for_response'  # An additional operation performed on dialog after click or submit actions. Defaults to `close`.  Value `none` requires `pause` set to `false`.
    pause: bool | None = None  # Whether the dialog should pause the game in single-player mode. Defaults to `true`.


type DialogMultiAction = DialogMultiActionDefault | DialogMultiActionClose | DialogMultiActionNone | DialogMultiActionWaitForResponse


class DialogNoticeDefault(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'dialog'

    type: Literal['minecraft:notice', 'notice'] = 'minecraft:notice'
    action: Button | None = None  # The only action in footer. Defaults to `gui.ok` label with no action or tooltip.
    title: Text
    external_title: Text | None = None  # Name to be used for a button leading to this dialog. If not present, `title` will be used instead.
    body: DialogBody | list[DialogBody] | None = None
    inputs: list[InputControl] | None = None
    can_close_with_escape: bool | None = None  # Whether the dialog can be closed with ESC key. Defaults to `true`.
    after_action: AfterAction | None = None  # An additional operation performed on dialog after click or submit actions. Defaults to `close`.  Value `none` requires `pause` set to `false`.
    pause: bool | None = None  # Whether the dialog should pause the game in single-player mode. Defaults to `true`.


class DialogNoticeClose(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'dialog'

    type: Literal['minecraft:notice', 'notice'] = 'minecraft:notice'
    action: Button | None = None  # The only action in footer. Defaults to `gui.ok` label with no action or tooltip.
    title: Text
    external_title: Text | None = None  # Name to be used for a button leading to this dialog. If not present, `title` will be used instead.
    body: DialogBody | list[DialogBody] | None = None
    inputs: list[InputControl] | None = None
    can_close_with_escape: bool | None = None  # Whether the dialog can be closed with ESC key. Defaults to `true`.
    after_action: Literal['minecraft:close', 'close'] | None = 'minecraft:close'  # An additional operation performed on dialog after click or submit actions. Defaults to `close`.  Value `none` requires `pause` set to `false`.
    pause: bool | None = None  # Whether the dialog should pause the game in single-player mode. Defaults to `true`.


class DialogNoticeNone(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'dialog'

    type: Literal['minecraft:notice', 'notice'] = 'minecraft:notice'
    action: Button | None = None  # The only action in footer. Defaults to `gui.ok` label with no action or tooltip.
    title: Text
    external_title: Text | None = None  # Name to be used for a button leading to this dialog. If not present, `title` will be used instead.
    body: DialogBody | list[DialogBody] | None = None
    inputs: list[InputControl] | None = None
    can_close_with_escape: bool | None = None  # Whether the dialog can be closed with ESC key. Defaults to `true`.
    after_action: Literal['minecraft:none', 'none'] | None = 'minecraft:none'  # An additional operation performed on dialog after click or submit actions. Defaults to `close`.  Value `none` requires `pause` set to `false`.
    pause: Literal[False] = False  # Whether the dialog should pause the game in single-player mode. Defaults to `true`.  The currently selected `after_action` only supports the value `false`


class DialogNoticeWaitForResponse(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'dialog'

    type: Literal['minecraft:notice', 'notice'] = 'minecraft:notice'
    action: Button | None = None  # The only action in footer. Defaults to `gui.ok` label with no action or tooltip.
    title: Text
    external_title: Text | None = None  # Name to be used for a button leading to this dialog. If not present, `title` will be used instead.
    body: DialogBody | list[DialogBody] | None = None
    inputs: list[InputControl] | None = None
    can_close_with_escape: bool | None = None  # Whether the dialog can be closed with ESC key. Defaults to `true`.
    after_action: Literal['minecraft:wait_for_response', 'wait_for_response'] | None = 'minecraft:wait_for_response'  # An additional operation performed on dialog after click or submit actions. Defaults to `close`.  Value `none` requires `pause` set to `false`.
    pause: bool | None = None  # Whether the dialog should pause the game in single-player mode. Defaults to `true`.


type DialogNotice = DialogNoticeDefault | DialogNoticeClose | DialogNoticeNone | DialogNoticeWaitForResponse


class DialogServerLinksDefault(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'dialog'

    type: Literal['minecraft:server_links', 'server_links'] = 'minecraft:server_links'
    button_width: Annotated[int, Field(ge=1)] | None = None  # Width of buttons in the list. Defaults to 150.
    exit_action: Button | None = None  # The button in footer. The action is also used for ESC-triggered exit.
    columns: Annotated[int, Field(ge=1)] | None = None  # The number of columns. Defaults to 2.
    title: Text
    external_title: Text | None = None  # Name to be used for a button leading to this dialog. If not present, `title` will be used instead.
    body: DialogBody | list[DialogBody] | None = None
    inputs: list[InputControl] | None = None
    can_close_with_escape: bool | None = None  # Whether the dialog can be closed with ESC key. Defaults to `true`.
    after_action: AfterAction | None = None  # An additional operation performed on dialog after click or submit actions. Defaults to `close`.  Value `none` requires `pause` set to `false`.
    pause: bool | None = None  # Whether the dialog should pause the game in single-player mode. Defaults to `true`.


class DialogServerLinksClose(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'dialog'

    type: Literal['minecraft:server_links', 'server_links'] = 'minecraft:server_links'
    button_width: Annotated[int, Field(ge=1)] | None = None  # Width of buttons in the list. Defaults to 150.
    exit_action: Button | None = None  # The button in footer. The action is also used for ESC-triggered exit.
    columns: Annotated[int, Field(ge=1)] | None = None  # The number of columns. Defaults to 2.
    title: Text
    external_title: Text | None = None  # Name to be used for a button leading to this dialog. If not present, `title` will be used instead.
    body: DialogBody | list[DialogBody] | None = None
    inputs: list[InputControl] | None = None
    can_close_with_escape: bool | None = None  # Whether the dialog can be closed with ESC key. Defaults to `true`.
    after_action: Literal['minecraft:close', 'close'] | None = 'minecraft:close'  # An additional operation performed on dialog after click or submit actions. Defaults to `close`.  Value `none` requires `pause` set to `false`.
    pause: bool | None = None  # Whether the dialog should pause the game in single-player mode. Defaults to `true`.


class DialogServerLinksNone(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'dialog'

    type: Literal['minecraft:server_links', 'server_links'] = 'minecraft:server_links'
    button_width: Annotated[int, Field(ge=1)] | None = None  # Width of buttons in the list. Defaults to 150.
    exit_action: Button | None = None  # The button in footer. The action is also used for ESC-triggered exit.
    columns: Annotated[int, Field(ge=1)] | None = None  # The number of columns. Defaults to 2.
    title: Text
    external_title: Text | None = None  # Name to be used for a button leading to this dialog. If not present, `title` will be used instead.
    body: DialogBody | list[DialogBody] | None = None
    inputs: list[InputControl] | None = None
    can_close_with_escape: bool | None = None  # Whether the dialog can be closed with ESC key. Defaults to `true`.
    after_action: Literal['minecraft:none', 'none'] | None = 'minecraft:none'  # An additional operation performed on dialog after click or submit actions. Defaults to `close`.  Value `none` requires `pause` set to `false`.
    pause: Literal[False] = False  # Whether the dialog should pause the game in single-player mode. Defaults to `true`.  The currently selected `after_action` only supports the value `false`


class DialogServerLinksWaitForResponse(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'dialog'

    type: Literal['minecraft:server_links', 'server_links'] = 'minecraft:server_links'
    button_width: Annotated[int, Field(ge=1)] | None = None  # Width of buttons in the list. Defaults to 150.
    exit_action: Button | None = None  # The button in footer. The action is also used for ESC-triggered exit.
    columns: Annotated[int, Field(ge=1)] | None = None  # The number of columns. Defaults to 2.
    title: Text
    external_title: Text | None = None  # Name to be used for a button leading to this dialog. If not present, `title` will be used instead.
    body: DialogBody | list[DialogBody] | None = None
    inputs: list[InputControl] | None = None
    can_close_with_escape: bool | None = None  # Whether the dialog can be closed with ESC key. Defaults to `true`.
    after_action: Literal['minecraft:wait_for_response', 'wait_for_response'] | None = 'minecraft:wait_for_response'  # An additional operation performed on dialog after click or submit actions. Defaults to `close`.  Value `none` requires `pause` set to `false`.
    pause: bool | None = None  # Whether the dialog should pause the game in single-player mode. Defaults to `true`.


type DialogServerLinks = DialogServerLinksDefault | DialogServerLinksClose | DialogServerLinksNone | DialogServerLinksWaitForResponse


type Dialog = DialogConfirmation | DialogDialogList | DialogMultiAction | DialogNotice | DialogServerLinks
