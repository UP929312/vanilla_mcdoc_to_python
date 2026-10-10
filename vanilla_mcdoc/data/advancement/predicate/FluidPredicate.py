"""
Generated from symbols.json for ::java::data::advancement::predicate::FluidPredicate
Local link to file: vanilla_mcdoc/data/advancement/predicate/FluidPredicate.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.util.MinMaxBounds import MinMaxBounds


class FluidPredicate(GeneratedModel):
    fluids: Annotated[str, IdSpec(registry='fluid', tags='allowed')] | list[Annotated[str, IdSpec(registry='fluid')]] | None = None
    state: dict[str, MinMaxBounds[int] | int | bool | str] | None = None
