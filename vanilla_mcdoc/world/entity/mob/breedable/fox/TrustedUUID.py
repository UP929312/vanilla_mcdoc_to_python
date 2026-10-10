"""
Generated from symbols.json for ::java::world::entity::mob::breedable::fox::TrustedUUID
Local link to file: vanilla_mcdoc/world/entity/mob/breedable/fox/TrustedUUID.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel


class TrustedUUID(GeneratedModel):
    L: int | None = None  # Lower bits of the trusted player's UUID.
    M: int | None = None  # Upper bits of the trusted player's UUID.
