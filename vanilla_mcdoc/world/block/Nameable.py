"""
Generated from symbols.json for ::java::world::block::Nameable
Local link to file: vanilla_mcdoc/world/block/Nameable.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.util.text.Text import Text


class Nameable(GeneratedModel):
    CustomName: Text | None = None  # The custom name of this block.
