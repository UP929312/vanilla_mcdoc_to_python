"""
Generated from symbols.json for ::java::world::entity::mob::breedable::turtle::Turtle
Local link to file: vanilla_mcdoc/world/entity/mob/breedable/turtle/Turtle.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.world.entity.mob.breedable.Breedable import Breedable


class Turtle(Breedable):
    has_egg: bool | None = None  # Whether it has an egg.
    home_pos: tuple[int, int, int] | None = None
