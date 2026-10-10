"""
Generated from symbols.json for ::java::data::advancement::predicate::LlamaPredicate
Local link to file: vanilla_mcdoc/data/advancement/predicate/LlamaPredicate.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.world.component.entity.LlamaVariant import LlamaVariant


class LlamaPredicate(GeneratedModel):
    variant: LlamaVariant
