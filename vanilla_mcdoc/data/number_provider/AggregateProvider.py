"""
Generated from symbols.json for ::java::data::number_provider::AggregateProvider
Local link to file: vanilla_mcdoc/data/number_provider/AggregateProvider.py
"""
# ~~~ CODE ~~~
from typing import Generic, TypeVar

from vanilla_mcdoc.base import GeneratedModel


S = TypeVar('S')


class AggregateProvider(GeneratedModel, Generic[S]):
    inputs: S
