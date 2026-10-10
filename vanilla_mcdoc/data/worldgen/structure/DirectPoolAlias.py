"""
Generated from symbols.json for ::java::data::worldgen::structure::DirectPoolAlias
Local link to file: vanilla_mcdoc/data/worldgen/structure/DirectPoolAlias.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec


class DirectPoolAlias(GeneratedModel):
    alias: Annotated[str, IdSpec()]
    target: Annotated[str, IdSpec(registry='worldgen/template_pool')]
