"""
Generated from symbols.json for ::java::data::variants::SoundVariant
Local link to file: vanilla_mcdoc/data/variants/SoundVariant.py
"""
# ~~~ CODE ~~~
from typing import Generic, TypeVar

from vanilla_mcdoc.base import GeneratedModel


T = TypeVar('T')


class SoundVariant(GeneratedModel, Generic[T]):
    adult_sounds: T
    baby_sounds: T
