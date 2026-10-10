"""
Generated from symbols.json for ::java::assets::particle::Particle
Local link to file: vanilla_mcdoc/assets/particle/Particle.py
"""
# ~~~ CODE ~~~
from typing import Annotated, ClassVar

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec


class Particle(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'particle'

    textures: list[Annotated[str, IdSpec(registry='texture', path='particle/')]]
