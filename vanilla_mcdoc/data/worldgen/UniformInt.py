"""
Generated from symbols.json for ::java::data::worldgen::UniformInt
Local link to file: vanilla_mcdoc/data/worldgen/UniformInt.py
"""
# ~~~ CODE ~~~
from typing import Generic, TypeVar

from vanilla_mcdoc.base import GeneratedModel


Base = TypeVar('Base')
Spread = TypeVar('Spread')


class UniformInt(GeneratedModel, Generic[Base, Spread]):
    base: Base
    spread: Spread
