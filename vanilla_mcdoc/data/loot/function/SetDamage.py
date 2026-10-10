"""
Generated from symbols.json for ::java::data::loot::function::SetDamage
Local link to file: vanilla_mcdoc/data/loot/function/SetDamage.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.data.loot.function.Conditions import Conditions

if TYPE_CHECKING:
    from vanilla_mcdoc.data.number_provider.FloatNumberProviderRef import FloatNumberProviderRef


class SetDamage(Conditions):
    damage: FloatNumberProviderRef  # Decimal percentage. Can be negative when used in combination with `add`.  Accepts a value between `-1` & `1` (inclusive).
    add: bool | None = None  # Whether to add to the existing damage of the item. Defaults to `false`.
