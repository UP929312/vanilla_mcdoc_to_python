"""
Generated from symbols.json for ::java::assets::atlas::PaletteRef
Local link to file: vanilla_mcdoc/assets/atlas/PaletteRef.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.minecraft_types import IdSpec


type PaletteRef = Annotated[str, IdSpec(registry='texture', path='palettes/')]
