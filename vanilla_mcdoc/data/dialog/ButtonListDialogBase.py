"""
Generated from symbols.json for ::java::data::dialog::ButtonListDialogBase
Local link to file: vanilla_mcdoc/data/dialog/ButtonListDialogBase.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, Literal

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.dialog.AfterAction import AfterAction
    from vanilla_mcdoc.data.dialog.Button import Button
    from vanilla_mcdoc.data.dialog.body.DialogBody import DialogBody
    from vanilla_mcdoc.data.dialog.input.InputControl import InputControl
    from vanilla_mcdoc.util.text.Text import Text


class ButtonListDialogBaseDefault(GeneratedModel):
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


class ButtonListDialogBaseClose(GeneratedModel):
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


class ButtonListDialogBaseNone(GeneratedModel):
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


class ButtonListDialogBaseWaitForResponse(GeneratedModel):
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


type ButtonListDialogBase = ButtonListDialogBaseDefault | ButtonListDialogBaseClose | ButtonListDialogBaseNone | ButtonListDialogBaseWaitForResponse
