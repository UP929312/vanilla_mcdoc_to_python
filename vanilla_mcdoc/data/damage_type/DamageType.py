"""
Generated from symbols.json for ::java::data::damage_type::DamageType
Local link to file: vanilla_mcdoc/data/damage_type/DamageType.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.damage_type.DamageEffects import DamageEffects
    from vanilla_mcdoc.data.damage_type.DamageScaling import DamageScaling
    from vanilla_mcdoc.data.damage_type.DeathMessageType import DeathMessageType


class DamageType(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'damage_type'

    message_id: str  # The message id used for deaths caused by this damage type. Is combined with the result of `death_message_type` to form a translation key.
    exhaustion: Annotated[float, Field(ge=0)]  # Amount of hunger exhaustion to cause.
    scaling: DamageScaling  # Whether to scale damage with difficulty levels.
    effects: DamageEffects | None = None  # Controls how damage manifests when inflicted on players. Defaults to `hurt`.
    death_message_type: DeathMessageType | None = None  # Controls if special death message variants are used. Defaults to `default`.  For more info see: https://minecraft.wiki/w/Damage_type#Death_messages
