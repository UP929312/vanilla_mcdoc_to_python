"""
Generated from symbols.json for ::java::data::dialog::body::ItemBody
Local link to file: vanilla_mcdoc/data/dialog/body/ItemBody.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.dialog.body.PlainMessage import PlainMessage
    from vanilla_mcdoc.util.text.Text import Text
    from vanilla_mcdoc.world.item.ItemStackTemplate import ItemStackTemplate


class ItemBody(GeneratedModel):
    item: ItemStackTemplate
    description: PlainMessage | Text | None = None  # The description text rendered to the right of item.
    show_decorations: bool | None = None  # Whether count and damage bar are rendered over the item. Defaults to `true`.
    show_tooltip: bool | None = None  # Whether item tooltip shows up when the item is hovered. Defaults to `true`.
    width: Annotated[int, Field(ge=1, le=256)] | None = None  # Width of the item. Defaults to 16.
    height: Annotated[int, Field(ge=1, le=256)] | None = None  # Height of the item. Defaults to 16.
