"""
Generated from symbols.json for ::java::assets::credits::CreditsCompanySegment
Local link to file: vanilla_mcdoc/assets/credits/CreditsCompanySegment.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel


class TitlesStruct(GeneratedModel):
    title: str
    names: list[str]  # Employees with the title.


class DisciplinesStruct(GeneratedModel):
    discipline: Annotated[str, Field(min_length=1)] | Literal[""]
    titles: list[TitlesStruct]


class CreditsCompanySegment(GeneratedModel):
    section: str  # Company segment.
    disciplines: list[DisciplinesStruct]
