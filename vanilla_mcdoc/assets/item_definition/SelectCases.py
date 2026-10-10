"""
Generated from symbols.json for ::java::assets::item_definition::SelectCases
Local link to file: vanilla_mcdoc/assets/item_definition/SelectCases.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Generic, TypeVar

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.assets.item_definition.SelectCase import SelectCase


T = TypeVar('T')


class SelectCases(GeneratedModel, Generic[T]):
    cases: list[SelectCase[T]]
