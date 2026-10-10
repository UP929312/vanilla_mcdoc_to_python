"""
Generated from symbols.json for ::java::world::component::item::DeathProtection
Local link to file: vanilla_mcdoc/world/component/item/DeathProtection.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.world.component.item.ConsumeEffect import ConsumeEffect


class DeathProtection(GeneratedModel):
    death_effects: list[ConsumeEffect] | None = None  # Effects applied when the item protects the holder.
