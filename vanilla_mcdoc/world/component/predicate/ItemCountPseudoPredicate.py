"""
Generated from symbols.json for ::java::world::component::predicate::ItemCountPseudoPredicate
Local link to file: vanilla_mcdoc/world/component/predicate/ItemCountPseudoPredicate.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.data.util.MinMaxBounds import MinMaxBounds


ItemCountPseudoPredicate = MinMaxBounds[Annotated[int, Field(ge=1, le=99)]] | Annotated[int, Field(ge=1, le=99)]
