"""
Generated from symbols.json for ::java::data::predicate::PredicateRef
Local link to file: vanilla_mcdoc/data/predicate/PredicateRef.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.predicate.Predicate import Predicate


type PredicateRef = Predicate | Annotated[str, IdSpec(registry='predicate')]
