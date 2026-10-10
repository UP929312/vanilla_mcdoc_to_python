"""
Generated from symbols.json for ::java::world::entity::end_crystal::EndCrystal
Local link to file: vanilla_mcdoc/world/entity/end_crystal/EndCrystal.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.world.entity.EntityBase import EntityBase


class EndCrystal(EntityBase):
    ShowBottom: bool | None = None  # Whether to show the base of the end crystal.
    beam_target: tuple[int, int, int] | None = None  # Coordinates that the beam is pointing to
