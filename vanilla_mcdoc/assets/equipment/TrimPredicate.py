"""
Generated from symbols.json for ::java::assets::equipment::TrimPredicate
Local link to file: vanilla_mcdoc/assets/equipment/TrimPredicate.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec


class TrimPredicate(GeneratedModel):
    pattern: Annotated[str, IdSpec(registry='trim_pattern')] | None = None
    material: Annotated[str, IdSpec(registry='trim_material')] | None = None
