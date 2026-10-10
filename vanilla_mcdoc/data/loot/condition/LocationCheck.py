"""
Generated from symbols.json for ::java::data::loot::condition::LocationCheck
Local link to file: vanilla_mcdoc/data/loot/condition/LocationCheck.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.advancement.predicate.LocationPredicate import LocationPredicate


class LocationCheck(GeneratedModel):
    offsetX: int | None = None
    offsetY: int | None = None
    offsetZ: int | None = None
    predicate: LocationPredicate
