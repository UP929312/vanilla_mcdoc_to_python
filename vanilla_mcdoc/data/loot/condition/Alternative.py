"""
Generated from symbols.json for ::java::data::loot::condition::Alternative
Local link to file: vanilla_mcdoc/data/loot/condition/Alternative.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.loot.condition.LootCondition import LootCondition


class Alternative(GeneratedModel):
    terms: list[LootCondition]
