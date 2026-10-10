"""
Generated from symbols.json for ::java::world::component::item::BucketEntityData
Local link to file: vanilla_mcdoc/world/component/item/BucketEntityData.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel


class BucketEntityData(GeneratedModel):
    NoAI: bool | None = None  # Whether it should have an AI.
    Silent: bool | None = None  # Whether the entity should make any sound.
    NoGravity: bool | None = None  # Whether the entity should be effected by gravity.
    Glowing: bool | None = None  # Whether the entity should glow.
    Invulnerable: bool | None = None  # Whether the entity should take damage.
    PersistenceRequired: bool | None = None  # Whether the entity should not despawn naturally.
    Health: float | None = None
    HuntingCooldown: int | None = None  # Turns into the expiry time of the memory module `has_hunting_cooldown` for axolotls.
    Age: int | None = None  # The age for axolotl and tadpole.
    AgeLocked: bool | None = None  # The age locked state for axolotl and tadpole.
    age: int | None = None  # The age for sulfur cube.
    age_locked: bool | None = None  # The age locked state for sulfur cube.
