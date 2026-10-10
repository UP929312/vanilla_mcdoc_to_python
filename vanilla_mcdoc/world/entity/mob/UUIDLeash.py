"""
Generated from symbols.json for ::java::world::entity::mob::UUIDLeash
Local link to file: vanilla_mcdoc/world/entity/mob/UUIDLeash.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel


class UUIDLeash(GeneratedModel):
    UUIDMost: int | None = None  # Upper bits of the other entity's UUID.
    UUIDLeast: int | None = None  # Lower bits of the other entity's UUID.
