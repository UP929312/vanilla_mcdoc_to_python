"""
Generated from symbols.json for ::java::world::component::item::Equippable
Local link to file: vanilla_mcdoc/world/component/item/Equippable.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.util.SoundEventRef import SoundEventRef
    from vanilla_mcdoc.util.slot.EquipmentSlot import EquipmentSlot


class Equippable(GeneratedModel):
    slot: EquipmentSlot
    equip_sound: SoundEventRef | None = None  # Sound event to play when the item is equipped. If not specified, the default armor equip sound will be played.
    asset_id: Annotated[str, IdSpec(registry='equipment')] | None = None
    camera_overlay: Annotated[str, IdSpec(registry='texture')] | None = None  # The overlay texture that should render in first person when equipped.
    allowed_entities: Annotated[str, IdSpec(registry='entity_type', tags='allowed')] | list[Annotated[str, IdSpec(registry='entity_type')]] | None = None  # Limits which entities can equip this item.
    dispensable: bool | None = None  # Whether the item can be equipped by using a dispenser. Defaults to `true`.
    swappable: bool | None = None  # Whether the item can be equipped by right-clicking. Defaults to `true`.
    damage_on_hurt: bool | None = None  # Whether the item will be damaged when the wearer is damaged. Defaults to `true`.
    equip_on_interact: bool | None = None  # Whether players can equip this item onto a target mob by right-clicking it (as long as this item can be equipped on the target at all). The item will not be equipped if the target already has an item in the relevant slot. Defaults to `false`.
    can_be_sheared: bool | None = None  # Whether players can use shears to remove this item from a mob by right-clicking it (as long as other shearing conditions are satisfied). Defaults to `false`.
    shearing_sound: SoundEventRef | None = None  # Sound event to play when the item is sheared from a mob. If not specified, the default shearing sound (`item.shears.snip`) will be played.
