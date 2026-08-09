# Generated from symbols.json for ::java::data::dialog::body::DialogBody
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Literal

if TYPE_CHECKING:
    from generated_symbols.data.dialog.body.PlainMessage import PlainMessage
    from generated_symbols.util.text.Text import Text
    from generated_symbols.world.item.ItemStackTemplate import ItemStackTemplate


@dataclass(kw_only=True)
class DialogBodyItem:
    type: Literal['minecraft:item']
    item: ItemStackTemplate
    description: PlainMessage | Text | None = None  # The description text rendered to the right of item.
    show_decorations: bool | None = None  # Whether count and damage bar are rendered over the item. Defaults to `true`.
    show_tooltip: bool | None = None  # Whether item tooltip shows up when the item is hovered. Defaults to `true`.
    width: Annotated[int, 'Range | `1`-`256` | both inclusive'] | None = None  # Width of the item. Defaults to 16.
    height: Annotated[int, 'Range | `1`-`256` | both inclusive'] | None = None  # Height of the item. Defaults to 16.


@dataclass(kw_only=True)
class DialogBodyPlainMessage:
    type: Literal['minecraft:plain_message']
    contents: Text  # A multiline label. Click events in the text trigger `after_action` like any other action.
    width: Annotated[int, 'Range | `1`-`1024` | both inclusive'] | None = None  # Maximum width of message. Defaults to 200.


type DialogBody = DialogBodyItem | DialogBodyPlainMessage


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::dialog::body::DialogBody": {
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
                                    "value": "dialog_body_type"
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
                    "registry": "minecraft:dialog_body"
                }
            }
        ]
    }
}

