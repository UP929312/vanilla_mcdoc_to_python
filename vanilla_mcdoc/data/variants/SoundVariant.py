"""
Generated from symbols.json for ::java::data::variants::SoundVariant
Local link to file: vanilla_mcdoc/data/variants/SoundVariant.py
"""
# ~~~ CODE ~~~
from typing import Any, Generic, TypeVar

from vanilla_mcdoc.base import GeneratedModel


T = TypeVar('T', default=Any)


class SoundVariant(GeneratedModel, Generic[T]):
    adult_sounds: T
    baby_sounds: T
