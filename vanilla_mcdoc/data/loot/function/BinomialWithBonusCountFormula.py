"""
Generated from symbols.json for ::java::data::loot::function::BinomialWithBonusCountFormula
Local link to file: vanilla_mcdoc/data/loot/function/BinomialWithBonusCountFormula.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel


class ParametersStruct(GeneratedModel):
    extra: int
    probability: Annotated[float, Field(ge=0, le=1)]


class BinomialWithBonusCountFormula(GeneratedModel):
    parameters: ParametersStruct
