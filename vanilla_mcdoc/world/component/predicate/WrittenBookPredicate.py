"""
Generated from symbols.json for ::java::world::component::predicate::WrittenBookPredicate
Local link to file: vanilla_mcdoc/world/component/predicate/WrittenBookPredicate.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.util.MinMaxBounds import MinMaxBounds
    from vanilla_mcdoc.util.text.Text import Text
    from vanilla_mcdoc.world.component.predicate.CollectionPredicate import CollectionPredicate


class WrittenBookPredicate(GeneratedModel):
    pages: CollectionPredicate[Text] | None = None  # Matches the raw text, instead of filtered.
    author: str | None = None
    title: str | None = None
    generation: MinMaxBounds[int] | int | None = None
    resolved: bool | None = None
