"""
Generated from symbols.json for ::java::data::dialog::ServerLinksDialog
Local link to file: generated_symbols/data/dialog/ServerLinksDialog.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Literal

if TYPE_CHECKING:
    from generated_symbols.data.dialog.AfterAction import AfterAction
    from generated_symbols.data.dialog.Button import Button
    from generated_symbols.data.dialog.body.DialogBody import DialogBody
    from generated_symbols.data.dialog.input.InputControl import InputControl
    from generated_symbols.util.text.Text import Text


@dataclass(kw_only=True)
class ServerLinksDialogNone:
    button_width: Annotated[int, 'Range | Min `1` and above | inclusive'] | None = None  # Width of buttons in the list. Defaults to 150.
    exit_action: Button | None = None  # The button in footer. The action is also used for ESC-triggered exit.
    columns: Annotated[int, 'Range | Min `1` and above | inclusive'] | None = None  # The number of columns. Defaults to 2.
    title: Text
    external_title: Text | None = None  # Name to be used for a button leading to this dialog. If not present, `title` will be used instead.
    body: DialogBody | list[DialogBody] | None = None
    inputs: list[InputControl] | None = None
    can_close_with_escape: bool | None = None  # Whether the dialog can be closed with ESC key. Defaults to `true`.
    after_action: AfterAction | None = None  # An additional operation performed on dialog after click or submit actions. Defaults to `close`.  Value `none` requires `pause` set to `false`.
    pause: bool | None = None  # Whether the dialog should pause the game in single-player mode. Defaults to `true`.


@dataclass(kw_only=True)
class ServerLinksDialogClose:
    button_width: Annotated[int, 'Range | Min `1` and above | inclusive'] | None = None  # Width of buttons in the list. Defaults to 150.
    exit_action: Button | None = None  # The button in footer. The action is also used for ESC-triggered exit.
    columns: Annotated[int, 'Range | Min `1` and above | inclusive'] | None = None  # The number of columns. Defaults to 2.
    title: Text
    external_title: Text | None = None  # Name to be used for a button leading to this dialog. If not present, `title` will be used instead.
    body: DialogBody | list[DialogBody] | None = None
    inputs: list[InputControl] | None = None
    can_close_with_escape: bool | None = None  # Whether the dialog can be closed with ESC key. Defaults to `true`.
    after_action: Literal['minecraft:close'] | None = None  # An additional operation performed on dialog after click or submit actions. Defaults to `close`.  Value `none` requires `pause` set to `false`.
    pause: bool | None = None  # Whether the dialog should pause the game in single-player mode. Defaults to `true`.


@dataclass(kw_only=True)
class ServerLinksDialogNone2:
    button_width: Annotated[int, 'Range | Min `1` and above | inclusive'] | None = None  # Width of buttons in the list. Defaults to 150.
    exit_action: Button | None = None  # The button in footer. The action is also used for ESC-triggered exit.
    columns: Annotated[int, 'Range | Min `1` and above | inclusive'] | None = None  # The number of columns. Defaults to 2.
    title: Text
    external_title: Text | None = None  # Name to be used for a button leading to this dialog. If not present, `title` will be used instead.
    body: DialogBody | list[DialogBody] | None = None
    inputs: list[InputControl] | None = None
    can_close_with_escape: bool | None = None  # Whether the dialog can be closed with ESC key. Defaults to `true`.
    after_action: Literal['minecraft:none'] | None = None  # An additional operation performed on dialog after click or submit actions. Defaults to `close`.  Value `none` requires `pause` set to `false`.
    pause: Literal[False]  # Whether the dialog should pause the game in single-player mode. Defaults to `true`.  The currently selected `after_action` only supports the value `false`


@dataclass(kw_only=True)
class ServerLinksDialogWaitForResponse:
    button_width: Annotated[int, 'Range | Min `1` and above | inclusive'] | None = None  # Width of buttons in the list. Defaults to 150.
    exit_action: Button | None = None  # The button in footer. The action is also used for ESC-triggered exit.
    columns: Annotated[int, 'Range | Min `1` and above | inclusive'] | None = None  # The number of columns. Defaults to 2.
    title: Text
    external_title: Text | None = None  # Name to be used for a button leading to this dialog. If not present, `title` will be used instead.
    body: DialogBody | list[DialogBody] | None = None
    inputs: list[InputControl] | None = None
    can_close_with_escape: bool | None = None  # Whether the dialog can be closed with ESC key. Defaults to `true`.
    after_action: Literal['minecraft:wait_for_response'] | None = None  # An additional operation performed on dialog after click or submit actions. Defaults to `close`.  Value `none` requires `pause` set to `false`.
    pause: bool | None = None  # Whether the dialog should pause the game in single-player mode. Defaults to `true`.


type ServerLinksDialog = ServerLinksDialogNone | ServerLinksDialogClose | ServerLinksDialogNone2 | ServerLinksDialogWaitForResponse


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::dialog::ServerLinksDialog": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::dialog::ButtonListDialogBase"
                }
            }
        ]
    }
}

