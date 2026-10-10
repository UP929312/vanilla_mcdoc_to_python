"""
Generated from symbols.json for ::java::world::item::ItemStackOfComponent
Local link to file: vanilla_mcdoc/world/item/ItemStackOfComponent.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Generic, TypeVar

from pydantic import Field

from vanilla_mcdoc.world.item.SingleItemOfComponent import SingleItemOfComponent


T = TypeVar('T')


class ItemStackOfComponent(SingleItemOfComponent[T], Generic[T]):
    count: Annotated[int, Field(ge=1, le=99)] | None = None  # Number of items in the stack. Defaults to `1`.
