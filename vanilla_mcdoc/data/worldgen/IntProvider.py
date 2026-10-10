"""
Generated from symbols.json for ::java::data::worldgen::IntProvider
Local link to file: vanilla_mcdoc/data/worldgen/IntProvider.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Generic, TypeVar

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec


T = TypeVar('T')


class IntProvider(GeneratedModel, Generic[T]):
    type: Annotated[str, IdSpec(registry='int_provider_type')]
