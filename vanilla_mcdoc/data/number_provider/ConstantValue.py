"""
Generated from symbols.json for ::java::data::number_provider::ConstantValue
Local link to file: vanilla_mcdoc/data/number_provider/ConstantValue.py
"""
# ~~~ CODE ~~~
from typing import Any, Generic, TypeVar

from vanilla_mcdoc.base import GeneratedModel


V = TypeVar('V', default=Any)


class ConstantValue(GeneratedModel, Generic[V]):
    value: V
