"""
Generated from symbols.json for ::java::data::loot::function::SetBookCover
Local link to file: vanilla_mcdoc/data/loot/function/SetBookCover.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.data.loot.function.Conditions import Conditions

if TYPE_CHECKING:
    from vanilla_mcdoc.util.Filterable import Filterable


class SetBookCover(Conditions):
    title: Filterable[Annotated[str, Field(min_length=0, max_length=32)]] | None = None  # If omitted, the original title is kept (or an empty string is used if there was no component)
    author: str | None = None  # If omitted, the original author is kept (or an empty string is used if there was no component)
    generation: Annotated[int, Field(ge=0, le=3)] | None = None  # If omitted, the original generation is kept (or 0 is used if there was no component)
