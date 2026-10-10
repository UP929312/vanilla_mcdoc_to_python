"""
Generated from symbols.json for ::java::data::loot::function::CopyNbt
Local link to file: vanilla_mcdoc/data/loot/function/CopyNbt.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.data.loot.function.Conditions import Conditions

if TYPE_CHECKING:
    from vanilla_mcdoc.data.loot.function.CopyNbtStrategy import CopyNbtStrategy
    from vanilla_mcdoc.data.util.NbtProvider import NbtProvider


class OpsStruct(GeneratedModel):
    source: str
    target: str
    op: CopyNbtStrategy


class CopyNbt(Conditions):
    source: NbtProvider
    ops: list[OpsStruct]
