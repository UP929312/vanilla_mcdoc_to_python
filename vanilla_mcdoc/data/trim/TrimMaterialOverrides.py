"""
Generated from symbols.json for ::java::data::trim::TrimMaterialOverrides
Local link to file: vanilla_mcdoc/data/trim/TrimMaterialOverrides.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.minecraft_types import IdSpec


type TrimMaterialOverrides = dict[Annotated[str, IdSpec(registry='equipment')], str]
