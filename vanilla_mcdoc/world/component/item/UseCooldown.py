"""
Generated from symbols.json for ::java::world::component::item::UseCooldown
Local link to file: vanilla_mcdoc/world/component/item/UseCooldown.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec


class UseCooldown(GeneratedModel):
    seconds: Annotated[float, Field(gt=0)]  # Time the cooldown will last.
    cooldown_group: Annotated[str, IdSpec(registry='cooldown_group', definition=True)] | None = None  # Cooldowns applied to this item will only be shared with any other items that are part of the same cooldown group.  Defaults to the ID of this item.
