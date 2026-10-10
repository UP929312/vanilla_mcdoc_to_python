"""
Generated from symbols.json for ::java::world::entity::item::Uuid
Local link to file: vanilla_mcdoc/world/entity/item/Uuid.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel


class Uuid(GeneratedModel):
    L: int | None = None  # Lower bits of the target player's UUID
    M: int | None = None  # Upper bits of the target player's UUID
