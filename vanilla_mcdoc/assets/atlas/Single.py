"""
Generated from symbols.json for ::java::assets::atlas::Single
Local link to file: vanilla_mcdoc/assets/atlas/Single.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec


class Single(GeneratedModel):
    resource: Annotated[str, IdSpec(registry='texture')]  # A single texture location of the source.
    sprite: Annotated[str, IdSpec(registry='texture', definition=True)] | None = None  # The identifier of the sprite that can referenced. If not specified, matches `resource`.
