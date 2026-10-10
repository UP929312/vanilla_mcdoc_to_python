"""
Generated from symbols.json for ::java::world::component::item::AdventureModePredicate
Local link to file: vanilla_mcdoc/world/component/item/AdventureModePredicate.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

if TYPE_CHECKING:
    from vanilla_mcdoc.data.advancement.predicate.BlockPredicate import BlockPredicate


type AdventureModePredicate = Annotated[list[BlockPredicate], Field(min_length=1)] | BlockPredicate
