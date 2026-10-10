"""
Generated from symbols.json for ::java::world::component::item::MobVisibility
Local link to file: vanilla_mcdoc/world/component/item/MobVisibility.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec


class MobVisibility(GeneratedModel):
    targeting_entity_types: Annotated[str, IdSpec(registry='entity_type', tags='allowed')] | list[Annotated[str, IdSpec(registry='entity_type')]]  # Entities to match.
    visibility: Annotated[float, Field(ge=0, le=10)]  # Visibility factor, with `0.0` reducing the range at which mobs detects the entity to `2`, while `10.0` increases the detection range tenfold. While multiple items with this component stack, the maximum vision will still never exceed `10.0`.
