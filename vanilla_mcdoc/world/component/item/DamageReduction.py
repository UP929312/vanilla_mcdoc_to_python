"""
Generated from symbols.json for ::java::world::component::item::DamageReduction
Local link to file: vanilla_mcdoc/world/component/item/DamageReduction.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec


class DamageReduction(GeneratedModel):
    type: Annotated[str, IdSpec(registry='damage_type', tags='allowed')] | list[Annotated[str, IdSpec(registry='damage_type')]] | None = None  # An optional damage type to filter this reduction by. If not specified, any damage type is accepted for this reduction.
    base: float  # Constant amount of damage to be blocked.
    factor: float  # Fraction of the dealt damage that should be blocked.
    horizontal_blocking_angle: Annotated[float, Field(gt=0)] | None = None  # Maximum angle between facing direction and incoming attack direction for the blocking to be effective
