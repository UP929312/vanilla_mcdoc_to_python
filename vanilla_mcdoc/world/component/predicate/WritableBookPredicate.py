"""
Generated from symbols.json for ::java::world::component::predicate::WritableBookPredicate
Local link to file: vanilla_mcdoc/world/component/predicate/WritableBookPredicate.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.world.component.predicate.CollectionPredicate import CollectionPredicate


class WritableBookPredicate(GeneratedModel):
    pages: CollectionPredicate[str] | None = None  # Matches the raw text, instead of filtered.
