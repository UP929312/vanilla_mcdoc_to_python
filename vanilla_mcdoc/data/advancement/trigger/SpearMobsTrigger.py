"""
Generated from symbols.json for ::java::data::advancement::trigger::SpearMobsTrigger
Local link to file: vanilla_mcdoc/data/advancement/trigger/SpearMobsTrigger.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.data.advancement.trigger.AllOptional import AllOptional
from vanilla_mcdoc.data.advancement.trigger.PlayerConditions import PlayerConditions


class SpearMobsTriggerTypeArg(PlayerConditions):
    count: Annotated[int, Field(ge=1)] | None = None  # Minimum mob count required.


SpearMobsTrigger = AllOptional[SpearMobsTriggerTypeArg]
