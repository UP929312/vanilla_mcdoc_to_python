"""
Generated from symbols.json for ::java::data::util::RandomValueBounds
Local link to file: vanilla_mcdoc/data/util/RandomValueBounds.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel


class RandomValueBoundsStruct(GeneratedModel):
    min: float
    max: float


type RandomValueBounds = float | RandomValueBoundsStruct
