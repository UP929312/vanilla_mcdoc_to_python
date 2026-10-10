"""
Generated from symbols.json for ::java::pack::PackFilter
Local link to file: vanilla_mcdoc/pack/PackFilter.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.pack.BlockPattern import BlockPattern


class PackFilter(GeneratedModel):
    block: list[BlockPattern]
