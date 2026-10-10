"""
Generated from symbols.json for ::java::data::advancement::predicate::LocationPredicateLight
Local link to file: vanilla_mcdoc/data/advancement/predicate/LocationPredicateLight.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.util.MinMaxBounds import MinMaxBounds


class LocationPredicateLight(GeneratedModel):
    light: MinMaxBounds[Annotated[int, Field(ge=0, le=15)]] | Annotated[int, Field(ge=0, le=15)] | None = None
