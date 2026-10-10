"""
Generated from symbols.json for ::java::assets::credits::CreditsDiscipline
Local link to file: vanilla_mcdoc/assets/credits/CreditsDiscipline.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel


class TitlesStruct(GeneratedModel):
    title: str
    names: list[str]  # Employees with the title.


class CreditsDiscipline(GeneratedModel):
    discipline: Annotated[str, Field(min_length=1)] | Literal[""]
    titles: list[TitlesStruct]
