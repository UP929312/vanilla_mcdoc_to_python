# ~~~ WHAT ARE WE TESTING ~~~

# Structs nested in lists are materialized recursively before the list alias.

# ~~~ FILE CONTENT ~~~
"""
Generated from symbols.json for ::java::assets::credits::Credits
Local link to file: generated_symbols/assets/credits/Credits.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Annotated, Literal


@dataclass(kw_only=True)
class TitlesStruct:
    title: str
    names: list[str]  # Employees with the title.


@dataclass(kw_only=True)
class DisciplinesStruct:
    discipline: Annotated[str, 'Length = 1 (inclusive) and above'] | Literal[""]
    titles: list[TitlesStruct]


@dataclass(kw_only=True)
class CreditsStruct:
    section: str  # Company segment.
    disciplines: list[DisciplinesStruct]


type Credits = list[CreditsStruct]
