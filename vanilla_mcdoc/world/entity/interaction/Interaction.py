"""
Generated from symbols.json for ::java::world::entity::interaction::Interaction
Local link to file: vanilla_mcdoc/world/entity/interaction/Interaction.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.world.entity.EntityBase import EntityBase

if TYPE_CHECKING:
    from vanilla_mcdoc.world.entity.interaction.Action import Action


class Interaction(EntityBase):
    width: float | None = None  # Cube hitbox width centered on the entity. Negative values are effectively `| x |`.
    height: float | None = None  # Cube hitbox height stretching up from the entity position. Negative values stretch the hitbox down.
    response: bool | None = None  # Whether an action should trigger a response. Defaults to false. Response: Attack - When true, the default attack sound is played. Interaction - When true, the player's arm swings.
    attack: Action | None = None  # Record of last attack (left click) event, can be updated every tick (no invulnerability frames).
    interaction: Action | None = None  # Record of last interaction (use; right click) event, can be updated every tick, if the player is holding the key it updates every 3 ticks.
