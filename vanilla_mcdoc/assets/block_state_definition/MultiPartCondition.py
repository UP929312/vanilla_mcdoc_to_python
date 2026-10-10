"""
Generated from symbols.json for ::java::assets::block_state_definition::MultiPartCondition
Local link to file: vanilla_mcdoc/assets/block_state_definition/MultiPartCondition.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel


class MultiPartConditionStruct1(GeneratedModel):
    OR: list[MultiPartCondition]


class MultiPartConditionStruct2(GeneratedModel):
    AND: list[MultiPartCondition]


type MultiPartConditionStruct3 = dict[str, str]


type MultiPartCondition = MultiPartConditionStruct1 | MultiPartConditionStruct2 | MultiPartConditionStruct3
