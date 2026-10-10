"""
Generated from symbols.json for ::java::data::number_provider::DistributionProvider
Local link to file: vanilla_mcdoc/data/number_provider/DistributionProvider.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Generic, TypeVar

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.util.NonEmptyWeightedList import NonEmptyWeightedList


T = TypeVar('T')


class DistributionProvider(GeneratedModel, Generic[T]):
    distribution: NonEmptyWeightedList[T]
