"""
Generated from symbols.json for ::java::data::advancement::trigger::AllOptional
Local link to file: vanilla_mcdoc/data/advancement/trigger/AllOptional.py
"""
# ~~~ CODE ~~~
from typing import Generic, TypeVar

from vanilla_mcdoc.base import GeneratedModel


C = TypeVar('C')


class AllOptional(GeneratedModel, Generic[C]):
    conditions: C | None = None
