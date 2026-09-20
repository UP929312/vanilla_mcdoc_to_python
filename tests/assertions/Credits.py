# ~~~ WHAT ARE WE TESTING ~~~

# Structs nested in lists are materialized recursively before the list alias.

# ~~~ FILE CONTENT ~~~
"""
Generated from symbols.json for ::java::assets::credits::Credits
Local link to file: generated_symbols/assets/credits/Credits.py
"""
# ~~~ CODE ~~~
from pydantic import BaseModel
from typing import Annotated, Literal


class TitlesStruct(BaseModel):
    title: str
    names: list[str]  # Employees with the title.


class DisciplinesStruct(BaseModel):
    discipline: Annotated[str, 'Length = 1 (inclusive) and above'] | Literal[""]
    titles: list[TitlesStruct]


class CreditsStruct(BaseModel):
    section: str  # Company segment.
    disciplines: list[DisciplinesStruct]


type Credits = list[CreditsStruct]


