"""
Generated from symbols.json for ::java::world::entity::projectile::OwnerUuid
Local link to file: vanilla_mcdoc/world/entity/projectile/OwnerUuid.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel


class OwnerUuid(GeneratedModel):
    OwnerUUIDMost: int | None = None  # Upper bits of the owner's UUID.
    OwnerUUIDLeast: int | None = None  # Lower bits of the owner's UUID.
