"""
Generated from symbols.json for ::java::pack::PackOverlays
Local link to file: vanilla_mcdoc/pack/PackOverlays.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.pack.PackOverlay import PackOverlay


class PackOverlays(GeneratedModel):
    entries: list[PackOverlay]
