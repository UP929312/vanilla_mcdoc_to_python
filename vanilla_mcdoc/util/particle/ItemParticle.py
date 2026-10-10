"""
Generated from symbols.json for ::java::util::particle::ItemParticle
Local link to file: vanilla_mcdoc/util/particle/ItemParticle.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.world.item.ItemStackTemplate import ItemStackTemplate


class ItemParticle(GeneratedModel):
    item: ItemStackTemplate
