"""
Generated from symbols.json for ::java::assets::atlas::Filter
Local link to file: vanilla_mcdoc/assets/atlas/Filter.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.assets.atlas.FilterPattern import FilterPattern


class Filter(GeneratedModel):
    pattern: FilterPattern  # Pattern to remove sprite identifiers already in the atlas. The order of sprite sources is important.
