"""
Generated from symbols.json for ::java::world::entity::evoker_fangs::Owner
Local link to file: vanilla_mcdoc/world/entity/evoker_fangs/Owner.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel


class Owner(GeneratedModel):
    OwnerUUIDMost: int | None = None  # Upper bits of the owner's UUID.
    OwnerUUIDLeast: int | None = None  # Lower bits of the owner's UUID.
