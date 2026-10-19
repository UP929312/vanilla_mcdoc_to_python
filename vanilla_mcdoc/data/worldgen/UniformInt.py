"""
Generated from symbols.json for ::java::data::worldgen::UniformInt
Local link to file: vanilla_mcdoc/data/worldgen/UniformInt.py
"""
# ~~~ CODE ~~~
from typing import Any, Generic, TypeVar

from vanilla_mcdoc.base import GeneratedModel


Base = TypeVar('Base', default=Any)
Spread = TypeVar('Spread', default=Any)


class UniformInt(GeneratedModel, Generic[Base, Spread]):
    base: Base
    spread: Spread
