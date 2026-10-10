"""
Generated from symbols.json for ::java::world::component::predicate::TrimPredicate
Local link to file: vanilla_mcdoc/world/component/predicate/TrimPredicate.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec


class TrimPredicate(GeneratedModel):
    material: Annotated[str, IdSpec(registry='trim_material', tags='allowed')] | list[Annotated[str, IdSpec(registry='trim_material')]] | None = None
    pattern: Annotated[str, IdSpec(registry='trim_pattern', tags='allowed')] | list[Annotated[str, IdSpec(registry='trim_pattern')]] | None = None
