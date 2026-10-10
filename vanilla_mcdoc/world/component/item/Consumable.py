"""
Generated from symbols.json for ::java::world::component::item::Consumable
Local link to file: vanilla_mcdoc/world/component/item/Consumable.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.util.SoundEventRef import SoundEventRef
    from vanilla_mcdoc.world.component.item.ConsumeEffect import ConsumeEffect
    from vanilla_mcdoc.world.component.item.ItemUseAnimation import ItemUseAnimation


class Consumable(GeneratedModel):
    consume_seconds: Annotated[float, Field(ge=0)] | None = None  # Time taken for a player to consume the item. Defaults to 1.6.
    animation: ItemUseAnimation | None = None  # View model/arms animation used during consumption of the item. Defaults to `eat`.
    sound: SoundEventRef | None = None  # Sound played during and on completion of item consumption.
    has_consume_particles: bool | None = None  # Whether the `item` particle is emitted while consuming the item. Defaults to `true`.
    on_consume_effects: list[ConsumeEffect] | None = None  # Side effects which take place after consuming the item.
