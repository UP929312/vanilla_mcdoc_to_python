"""
Generated from symbols.json for ::java::data::loot::function::UniformBonusFormula
Local link to file: vanilla_mcdoc/data/loot/function/UniformBonusFormula.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel


class ParametersStruct(GeneratedModel):
    bonusMultiplier: int


class UniformBonusFormula(GeneratedModel):
    parameters: ParametersStruct
