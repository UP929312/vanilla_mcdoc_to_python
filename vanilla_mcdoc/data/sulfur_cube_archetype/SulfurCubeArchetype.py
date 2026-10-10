"""
Generated from symbols.json for ::java::data::sulfur_cube_archetype::SulfurCubeArchetype
Local link to file: vanilla_mcdoc/data/sulfur_cube_archetype/SulfurCubeArchetype.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.sulfur_cube_archetype.AttributeEntry import AttributeEntry
    from vanilla_mcdoc.data.sulfur_cube_archetype.ContactDamage import ContactDamage
    from vanilla_mcdoc.data.sulfur_cube_archetype.ExplosionData import ExplosionData
    from vanilla_mcdoc.data.sulfur_cube_archetype.KnockbackModifiers import KnockbackModifiers
    from vanilla_mcdoc.data.sulfur_cube_archetype.SoundSettings import SoundSettings
    from vanilla_mcdoc.registry.KnownItemId import KnownItemId


class SulfurCubeArchetype(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'sulfur_cube_archetype'

    items: Annotated[str, IdSpec(registry='item', tags='allowed')] | KnownItemId | list[Annotated[str, IdSpec(registry='item')] | KnownItemId]
    buoyant: bool | None = None  # Defaults to `false`.
    explosion: ExplosionData | None = None  # When present, sulfur cube with this archetype will explode when ignited.
    contact_damage: ContactDamage | None = None
    knockback_modifiers: KnockbackModifiers
    attribute_modifiers: list[AttributeEntry]
    sound_settings: SoundSettings
