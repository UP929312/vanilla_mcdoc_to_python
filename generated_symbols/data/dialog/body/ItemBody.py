"""
Generated from symbols.json for ::java::data::dialog::body::ItemBody
Local link to file: generated_symbols/data/dialog/body/ItemBody.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from generated_symbols.base import GeneratedModel
from pydantic import Field

if TYPE_CHECKING:
    from generated_symbols.data.dialog.body.PlainMessage import PlainMessage
    from generated_symbols.util.text.Text import Text
    from generated_symbols.world.item.ItemStackTemplate import ItemStackTemplate


class ItemBody(GeneratedModel):
    item: ItemStackTemplate
    description: PlainMessage | Text | None = None  # The description text rendered to the right of item.
    show_decorations: bool | None = None  # Whether count and damage bar are rendered over the item. Defaults to `true`.
    show_tooltip: bool | None = None  # Whether item tooltip shows up when the item is hovered. Defaults to `true`.
    width: Annotated[int, Field(ge=1, le=256)] | None = None  # Width of the item. Defaults to 16.
    height: Annotated[int, Field(ge=1, le=256)] | None = None  # Height of the item. Defaults to 16.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::dialog::body::ItemBody": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "item",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::item::ItemStackTemplate"
                }
            },
            {
                "kind": "pair",
                "desc": "The description text rendered to the right of item.",
                "key": "description",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "reference",
                            "path": "::java::data::dialog::body::PlainMessage"
                        },
                        {
                            "kind": "reference",
                            "path": "::java::util::text::Text"
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether count and damage bar are rendered over the item.\nDefaults to `True`.",
                "key": "show_decorations",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether item tooltip shows up when the item is hovered.\nDefaults to `True`.",
                "key": "show_tooltip",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Width of the item.\nDefaults to 16.",
                "key": "width",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 1,
                        "max": 256
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Height of the item.\nDefaults to 16.",
                "key": "height",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 1,
                        "max": 256
                    }
                },
                "optional": True
            }
        ]
    }
}

