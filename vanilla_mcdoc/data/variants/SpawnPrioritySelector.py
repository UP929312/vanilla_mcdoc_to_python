"""
Generated from symbols.json for ::java::data::variants::SpawnPrioritySelector
Local link to file: vanilla_mcdoc/data/variants/SpawnPrioritySelector.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.variants.SpawnCondition import SpawnCondition


class SpawnPrioritySelector(GeneratedModel):
    condition: SpawnCondition | None = None  # The spawn condition to check. If not present, the condition always matches.
    priority: int  # The spawn priority to use.
