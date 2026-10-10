"""
Generated from symbols.json for ::java::world::entity::projectile::throwable::Owner
Local link to file: vanilla_mcdoc/world/entity/projectile/throwable/Owner.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel


class Owner(GeneratedModel):
    M: int | None = None  # Upper bits of the owner's UUID.
    L: int | None = None  # Lower bits of the owner's UUID.
