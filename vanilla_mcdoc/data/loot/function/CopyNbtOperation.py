"""
Generated from symbols.json for ::java::data::loot::function::CopyNbtOperation
Local link to file: vanilla_mcdoc/data/loot/function/CopyNbtOperation.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.loot.function.CopyNbtStrategy import CopyNbtStrategy


class CopyNbtOperation(GeneratedModel):
    source: str
    target: str
    op: CopyNbtStrategy
