"""
Generated from symbols.json for ::java::data::dialog::DialogBase
Local link to file: generated_symbols/data/dialog/DialogBase.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Literal

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.dialog.AfterAction import AfterAction
    from generated_symbols.data.dialog.body.DialogBody import DialogBody
    from generated_symbols.data.dialog.input.InputControl import InputControl
    from generated_symbols.util.text.Text import Text


class DialogBaseNone(GeneratedModel):
    title: Text
    external_title: Text | None = None  # Name to be used for a button leading to this dialog. If not present, `title` will be used instead.
    body: DialogBody | list[DialogBody] | None = None
    inputs: list[InputControl] | None = None
    can_close_with_escape: bool | None = None  # Whether the dialog can be closed with ESC key. Defaults to `true`.
    after_action: AfterAction | None = None  # An additional operation performed on dialog after click or submit actions. Defaults to `close`.  Value `none` requires `pause` set to `false`.
    pause: bool | None = None  # Whether the dialog should pause the game in single-player mode. Defaults to `true`.


class DialogBaseClose(GeneratedModel):
    title: Text
    external_title: Text | None = None  # Name to be used for a button leading to this dialog. If not present, `title` will be used instead.
    body: DialogBody | list[DialogBody] | None = None
    inputs: list[InputControl] | None = None
    can_close_with_escape: bool | None = None  # Whether the dialog can be closed with ESC key. Defaults to `true`.
    after_action: Literal['minecraft:close', 'close'] | None = 'minecraft:close'  # An additional operation performed on dialog after click or submit actions. Defaults to `close`.  Value `none` requires `pause` set to `false`.
    pause: bool | None = None  # Whether the dialog should pause the game in single-player mode. Defaults to `true`.


class DialogBaseNone2(GeneratedModel):
    title: Text
    external_title: Text | None = None  # Name to be used for a button leading to this dialog. If not present, `title` will be used instead.
    body: DialogBody | list[DialogBody] | None = None
    inputs: list[InputControl] | None = None
    can_close_with_escape: bool | None = None  # Whether the dialog can be closed with ESC key. Defaults to `true`.
    after_action: Literal['minecraft:none', 'none'] | None = 'minecraft:none'  # An additional operation performed on dialog after click or submit actions. Defaults to `close`.  Value `none` requires `pause` set to `false`.
    pause: Literal[False] = False  # Whether the dialog should pause the game in single-player mode. Defaults to `true`.  The currently selected `after_action` only supports the value `false`


class DialogBaseWaitForResponse(GeneratedModel):
    title: Text
    external_title: Text | None = None  # Name to be used for a button leading to this dialog. If not present, `title` will be used instead.
    body: DialogBody | list[DialogBody] | None = None
    inputs: list[InputControl] | None = None
    can_close_with_escape: bool | None = None  # Whether the dialog can be closed with ESC key. Defaults to `true`.
    after_action: Literal['minecraft:wait_for_response', 'wait_for_response'] | None = 'minecraft:wait_for_response'  # An additional operation performed on dialog after click or submit actions. Defaults to `close`.  Value `none` requires `pause` set to `false`.
    pause: bool | None = None  # Whether the dialog should pause the game in single-player mode. Defaults to `true`.


type DialogBase = DialogBaseNone | DialogBaseClose | DialogBaseNone2 | DialogBaseWaitForResponse


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::dialog::DialogBase": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "title",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::text::Text"
                }
            },
            {
                "kind": "pair",
                "desc": "Name to be used for a button leading to this dialog.\nIf not present, `title` will be used instead.",
                "key": "external_title",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::text::Text"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "body",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "reference",
                            "path": "::java::data::dialog::body::DialogBody"
                        },
                        {
                            "kind": "list",
                            "item": {
                                "kind": "reference",
                                "path": "::java::data::dialog::body::DialogBody"
                            }
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "inputs",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::data::dialog::input::InputControl"
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether the dialog can be closed with ESC key.\nDefaults to `True`.",
                "key": "can_close_with_escape",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "An additional operation performed on dialog after click or submit actions.\nDefaults to `close`. \\\nValue `none` requires `pause` set to `False`.",
                "key": "after_action",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::dialog::AfterAction"
                },
                "optional": True
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "dynamic",
                            "accessor": [
                                "after_action"
                            ]
                        }
                    ],
                    "registry": "mcdoc:dialog_after_action"
                }
            }
        ]
    }
}
