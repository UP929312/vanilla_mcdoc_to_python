"""
Generated from symbols.json for ::java::data::dialog::NoticeDialog
Local link to file: generated_symbols/data/dialog/NoticeDialog.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from generated_symbols.data.dialog.AfterAction import AfterAction
    from generated_symbols.data.dialog.Button import Button
    from generated_symbols.data.dialog.body.DialogBody import DialogBody
    from generated_symbols.data.dialog.input.InputControl import InputControl
    from generated_symbols.util.text.Text import Text


@dataclass(kw_only=True)
class NoticeDialogNone:
    title: Text
    action: Button | None = None  # The only action in footer. Defaults to `gui.ok` label with no action or tooltip.
    external_title: Text | None = None  # Name to be used for a button leading to this dialog. If not present, `title` will be used instead.
    body: DialogBody | list[DialogBody] | None = None
    inputs: list[InputControl] | None = None
    can_close_with_escape: bool | None = None  # Whether the dialog can be closed with ESC key. Defaults to `true`.
    after_action: AfterAction | None = None  # An additional operation performed on dialog after click or submit actions. Defaults to `close`.  Value `none` requires `pause` set to `false`.
    pause: bool | None = None  # Whether the dialog should pause the game in single-player mode. Defaults to `true`.


@dataclass(kw_only=True)
class NoticeDialogClose:
    title: Text
    action: Button | None = None  # The only action in footer. Defaults to `gui.ok` label with no action or tooltip.
    external_title: Text | None = None  # Name to be used for a button leading to this dialog. If not present, `title` will be used instead.
    body: DialogBody | list[DialogBody] | None = None
    inputs: list[InputControl] | None = None
    can_close_with_escape: bool | None = None  # Whether the dialog can be closed with ESC key. Defaults to `true`.
    after_action: Literal['minecraft:close'] | None = None  # An additional operation performed on dialog after click or submit actions. Defaults to `close`.  Value `none` requires `pause` set to `false`.
    pause: bool | None = None  # Whether the dialog should pause the game in single-player mode. Defaults to `true`.


@dataclass(kw_only=True)
class NoticeDialogNone2:
    title: Text
    pause: Literal[False]  # Whether the dialog should pause the game in single-player mode. Defaults to `true`.  The currently selected `after_action` only supports the value `false`
    action: Button | None = None  # The only action in footer. Defaults to `gui.ok` label with no action or tooltip.
    external_title: Text | None = None  # Name to be used for a button leading to this dialog. If not present, `title` will be used instead.
    body: DialogBody | list[DialogBody] | None = None
    inputs: list[InputControl] | None = None
    can_close_with_escape: bool | None = None  # Whether the dialog can be closed with ESC key. Defaults to `true`.
    after_action: Literal['minecraft:none'] | None = None  # An additional operation performed on dialog after click or submit actions. Defaults to `close`.  Value `none` requires `pause` set to `false`.


@dataclass(kw_only=True)
class NoticeDialogWaitForResponse:
    title: Text
    action: Button | None = None  # The only action in footer. Defaults to `gui.ok` label with no action or tooltip.
    external_title: Text | None = None  # Name to be used for a button leading to this dialog. If not present, `title` will be used instead.
    body: DialogBody | list[DialogBody] | None = None
    inputs: list[InputControl] | None = None
    can_close_with_escape: bool | None = None  # Whether the dialog can be closed with ESC key. Defaults to `true`.
    after_action: Literal['minecraft:wait_for_response'] | None = None  # An additional operation performed on dialog after click or submit actions. Defaults to `close`.  Value `none` requires `pause` set to `false`.
    pause: bool | None = None  # Whether the dialog should pause the game in single-player mode. Defaults to `true`.


type NoticeDialog = NoticeDialogNone | NoticeDialogClose | NoticeDialogNone2 | NoticeDialogWaitForResponse


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::dialog::NoticeDialog": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::dialog::DialogBase"
                }
            },
            {
                "kind": "pair",
                "desc": "The only action in footer.\nDefaults to `gui.ok` label with no action or tooltip.",
                "key": "action",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::dialog::Button"
                },
                "optional": True
            }
        ]
    }
}

