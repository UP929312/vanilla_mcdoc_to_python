"""
Generated from symbols.json for ::java::world::component::item::blocks_attacks
Local link to file: vanilla_mcdoc/world/component/item/blocks_attacks.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.util.SoundEventRef import SoundEventRef
    from vanilla_mcdoc.world.component.item.DamageReduction import DamageReduction
    from vanilla_mcdoc.world.component.item.ItemDamageFunction import ItemDamageFunction


class blocks_attacks(GeneratedModel):
    block_delay_seconds: Annotated[float, Field(ge=0)] | None = None  # Number of seconds that right-click must be held before successfully blocking attacks. Defaults to `0`.
    disable_cooldown_scale: Annotated[float, Field(ge=0)] | None = None  # Multiplier applied to the number of seconds that the item will be on cooldown for when attacked by a disabling attack (`disable_blocking_for_seconds` on the `weapon` component). Defaults to `1`. If `0`, this item can never be disabled by attacks.
    damage_reductions: list[DamageReduction] | None = None  # Controls how much damage should be blocked in a given attack. If not specified, all damage is blocked. Each entry in the list contributes an amount of damage to be blocked, optionally filtered by a damage type. Each entry adds to blocked damage, determined by `clamp(base + factor * dealt_damage, 0, dealt_damage)`. The final damage applied in the attack to the entity is determined by `dealt_damage - clamp(blocked_damage, 0, dealt_damage)`.
    item_damage: ItemDamageFunction | None = None  # Controls how much damage should be applied to the item from a given attack. If not specified, a point of durability is removed for every point of damage dealt. The final damage applied to the item is determined by `floor(base + factor * dealt_damage)`. The final value may be negative, causing the item to be repaired.
    block_sound: SoundEventRef | None = None  # Sound played when an attack is successfully blocked.
    disabled_sound: SoundEventRef | None = None  # Sound played when the item goes on its disabled cooldown due to an attack.
    bypassed_by: Annotated[str, IdSpec(registry='damage_type', tags='allowed')] | list[Annotated[str, IdSpec(registry='damage_type')]] | None = None  # Damage types in this tag are bypassing the blocking
