"""
Generated from symbols.json for ::java::data::number_provider::EnvironmentAttributeProvider
Local link to file: vanilla_mcdoc/data/number_provider/EnvironmentAttributeProvider.py
"""
# ~~~ CODE ~~~
from typing import Generic, TypeVar

from vanilla_mcdoc.base import GeneratedModel


A = TypeVar('A')


class EnvironmentAttributeProvider(GeneratedModel, Generic[A]):
    attribute: A
