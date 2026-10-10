"""
Generated from symbols.json for ::java::data::number_provider::DataStorageProvider
Local link to file: vanilla_mcdoc/data/number_provider/DataStorageProvider.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Generic, TypeVar

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec


T = TypeVar('T')


class DataStorageProvider(GeneratedModel, Generic[T]):
    storage: Annotated[str, IdSpec(registry='storage')]
    path: str
    fallback: T | None = None  # Defaults to constant 0.
