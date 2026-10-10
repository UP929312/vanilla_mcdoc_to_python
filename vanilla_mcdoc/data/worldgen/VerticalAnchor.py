"""
Generated from symbols.json for ::java::data::worldgen::VerticalAnchor
Local link to file: vanilla_mcdoc/data/worldgen/VerticalAnchor.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel


class VerticalAnchorStruct1(GeneratedModel):
    absolute: int


class VerticalAnchorStruct2(GeneratedModel):
    above_bottom: int


class VerticalAnchorStruct3(GeneratedModel):
    below_top: int


class VerticalAnchorStruct4(GeneratedModel):
    relative_to_sea_level: int


type VerticalAnchor = VerticalAnchorStruct1 | VerticalAnchorStruct2 | VerticalAnchorStruct3 | VerticalAnchorStruct4
