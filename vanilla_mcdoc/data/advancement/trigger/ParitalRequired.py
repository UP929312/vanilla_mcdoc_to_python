"""
Generated from symbols.json for ::java::data::advancement::trigger::ParitalRequired
Local link to file: vanilla_mcdoc/data/advancement/trigger/ParitalRequired.py
"""
# ~~~ CODE ~~~
from typing import Any, Generic, TypeVar

from vanilla_mcdoc.base import GeneratedModel


C = TypeVar('C', default=Any)


class ParitalRequired(GeneratedModel, Generic[C]):
    conditions: C
