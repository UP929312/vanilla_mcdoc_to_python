"""
Generated from symbols.json for ::java::world::item::SingleItemOfComponent
Local link to file: vanilla_mcdoc/world/item/SingleItemOfComponent.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Generic, TypeVar

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec


T = TypeVar('T')


class SingleItemOfComponent(GeneratedModel, Generic[T]):
    id: Annotated[str, IdSpec(registry='item', exclude=('air',))]  # ID of the item.
    components: T | None = None
