# Generated from symbols.json for ::java::world::entity::interaction::Interaction
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.world.entity.EntityBase import EntityBase

if TYPE_CHECKING:
    from generated_symbols.world.entity.interaction.Action import Action


@dataclass(kw_only=True)
class Interaction(EntityBase):
    width: float | None = None  # Cube hitbox width centered on the entity. Negative values are effectively `| x |`.
    height: float | None = None  # Cube hitbox height stretching up from the entity position. Negative values stretch the hitbox down.
    response: bool | None = None  # Whether an action should trigger a response. Defaults to false. Response: Attack - When true, the default attack sound is played. Interaction - When true, the player's arm swings.
    attack: Action | None = None  # Record of last attack (left click) event, can be updated every tick (no invulnerability frames).
    interaction: Action | None = None  # Record of last interaction (use; right click) event, can be updated every tick, if the player is holding the key it updates every 3 ticks.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::interaction::Interaction": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::EntityBase"
                }
            },
            {
                "kind": "pair",
                "desc": "Cube hitbox width centered on the entity. Negative values are effectively `| x |`.",
                "key": "width",
                "type": {
                    "kind": "float"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Cube hitbox height stretching up from the entity position. Negative values stretch the hitbox down.",
                "key": "height",
                "type": {
                    "kind": "float"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether an action should trigger a response. Defaults to False.\nResponse:\nAttack - When True, the default attack sound is played.\nInteraction - When True, the player's arm swings.",
                "key": "response",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Record of last attack (left click) event, can be updated every tick (no invulnerability frames).",
                "key": "attack",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::interaction::Action"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Record of last interaction (use; right click) event, can be updated every tick, if the player is holding the key it updates every 3 ticks.",
                "key": "interaction",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::interaction::Action"
                },
                "optional": True
            }
        ]
    }
}

