"""
Generated from symbols.json for ::java::world::block::jigsaw::Jigsaw
Local link to file: vanilla_mcdoc/world/block/jigsaw/Jigsaw.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.world.block.jigsaw.JointType import JointType


class Jigsaw(GeneratedModel):
    joint: JointType | None = None  # How the resultant structure can be transformed.
    pool: Annotated[str, IdSpec(registry='worldgen/template_pool')] | None = None  # Structure pool this will "spawn" in.
    name: str | None = None  # ID this will "spawn" in.
    target: str | None = None  # ID of the type of jigsaw this will be "spawned" from.
    final_state: str | None = None  # Final block state of the jigsaw.
