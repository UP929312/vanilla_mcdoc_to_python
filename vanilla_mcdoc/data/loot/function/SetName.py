"""
Generated from symbols.json for ::java::data::loot::function::SetName
Local link to file: vanilla_mcdoc/data/loot/function/SetName.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.data.loot.function.Conditions import Conditions

if TYPE_CHECKING:
    from vanilla_mcdoc.data.loot.EntityTarget import EntityTarget
    from vanilla_mcdoc.data.loot.function.SetNameTarget import SetNameTarget
    from vanilla_mcdoc.util.text.Text import Text


class SetName(Conditions):
    entity: EntityTarget | None = None  # Specifies the entity to act as the target `@s` in the JSON text component.
    name: Text
    target: SetNameTarget | None = None  # Which name component to set. Defaults to `custom_name`.
