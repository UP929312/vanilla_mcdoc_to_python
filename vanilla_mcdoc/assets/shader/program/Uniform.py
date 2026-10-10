"""
Generated from symbols.json for ::java::assets::shader::program::Uniform
Local link to file: vanilla_mcdoc/assets/shader/program/Uniform.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.assets.shader.program.UniformType import UniformType


class Uniform(GeneratedModel):
    name: str
    type: UniformType
    count: int
    values: list[float]
