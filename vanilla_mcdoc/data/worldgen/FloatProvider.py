"""
Generated from symbols.json for ::java::data::worldgen::FloatProvider
Local link to file: vanilla_mcdoc/data/worldgen/FloatProvider.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Any, Generic, TypeVar

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec


T = TypeVar('T', default=Any)


class FloatProvider(GeneratedModel, Generic[T]):
    type: Annotated[str, IdSpec(registry='float_provider_type')]
