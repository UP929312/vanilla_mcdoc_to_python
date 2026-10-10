"""
Generated from symbols.json for ::java::assets::item_definition::SelectCase
Local link to file: vanilla_mcdoc/assets/item_definition/SelectCase.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Generic, TypeVar

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.assets.item_definition.ItemModel import ItemModel


T = TypeVar('T')


class SelectCase(GeneratedModel, Generic[T]):
    when: T | list[T]
    model: ItemModel
