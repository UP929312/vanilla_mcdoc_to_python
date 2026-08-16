"""
Generated from symbols.json for ::java::data::dialog::MultiActionDialog
Local link to file: generated_symbols/data/dialog/MultiActionDialog.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, ClassVar, Literal

if TYPE_CHECKING:
    from generated_symbols.data.dialog.AfterAction import AfterAction
    from generated_symbols.data.dialog.Button import Button
    from generated_symbols.data.dialog.body.DialogBody import DialogBody
    from generated_symbols.data.dialog.input.InputControl import InputControl
    from generated_symbols.util.text.Text import Text


@dataclass(kw_only=True)
class MultiActionDialogNone:
    __resource_dir__: ClassVar[str] = 'dialog'

    actions: Annotated[list[Button], 'Length = 1 (inclusive) and above']
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
class MultiActionDialogClose:
    actions: Annotated[list[Button], 'Length = 1 (inclusive) and above']
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
class MultiActionDialogNone2:
    actions: Annotated[list[Button], 'Length = 1 (inclusive) and above']
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
class MultiActionDialogWaitForResponse:
    actions: Annotated[list[Button], 'Length = 1 (inclusive) and above']
    exit_action: Button | None = None  # The button in footer. The action is also used for ESC-triggered exit.
    columns: Annotated[int, 'Range | Min `1` and above | inclusive'] | None = None  # The number of columns. Defaults to 2.
    title: Text
    external_title: Text | None = None  # Name to be used for a button leading to this dialog. If not present, `title` will be used instead.
    body: DialogBody | list[DialogBody] | None = None
    inputs: list[InputControl] | None = None
    can_close_with_escape: bool | None = None  # Whether the dialog can be closed with ESC key. Defaults to `true`.
    after_action: Literal['minecraft:wait_for_response'] | None = None  # An additional operation performed on dialog after click or submit actions. Defaults to `close`.  Value `none` requires `pause` set to `false`.
    pause: bool | None = None  # Whether the dialog should pause the game in single-player mode. Defaults to `true`.


type MultiActionDialog = MultiActionDialogNone | MultiActionDialogClose | MultiActionDialogNone2 | MultiActionDialogWaitForResponse


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::dialog::MultiActionDialog": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::dialog::ListDialogBase"
                }
            },
            {
                "kind": "pair",
                "key": "actions",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::data::dialog::Button"
                    },
                    "lengthRange": {
                        "kind": 0,
                        "min": 1
                    }
                }
            }
        ]
    }
}

