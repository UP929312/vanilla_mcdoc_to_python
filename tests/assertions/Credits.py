# ~~~ WHAT ARE WE TESTING ~~~

# Structs nested in lists are materialized recursively before the list alias.

# ~~~ FILE CONTENT ~~~
"""
Generated from symbols.json for ::java::assets::credits::Credits
Local link to file: generated_symbols/assets/credits/Credits.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from generated_symbols.base import GeneratedModel
from pydantic import Field


class TitlesStruct(GeneratedModel):
    title: str
    names: list[str]  # Employees with the title.


class DisciplinesStruct(GeneratedModel):
    discipline: Annotated[str, 'Field(min_length=1)'] | Literal[""]
    titles: list[TitlesStruct]


class CreditsStruct(GeneratedModel):
    section: str  # Company segment.
    disciplines: list[DisciplinesStruct]


type Credits = list[CreditsStruct]
