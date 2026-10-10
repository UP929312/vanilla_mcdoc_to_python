"""
Generated from symbols.json for ::java::data::worldgen::attribute::modifier::OverrideModifier
Local link to file: vanilla_mcdoc/data/worldgen/attribute/modifier/OverrideModifier.py
"""
# ~~~ CODE ~~~
from typing import Generic, Literal, TypeVar

from vanilla_mcdoc.base import GeneratedModel


T = TypeVar('T')


class OverrideModifier(GeneratedModel, Generic[T]):
    modifier: Literal['override'] = 'override'
    argument: T
