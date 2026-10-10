"""
Generated from symbols.json for ::java::data::advancement::predicate::SlimePredicate
Local link to file: vanilla_mcdoc/data/advancement/predicate/SlimePredicate.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.util.MinMaxBounds import MinMaxBounds


class SlimePredicate(GeneratedModel):
    size: MinMaxBounds[int] | int | None = None
