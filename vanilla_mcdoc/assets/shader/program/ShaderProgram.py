"""
Generated from symbols.json for ::java::assets::shader::program::ShaderProgram
Local link to file: vanilla_mcdoc/assets/shader/program/ShaderProgram.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.assets.shader.program.Defines import Defines
    from vanilla_mcdoc.assets.shader.program.Sampler import Sampler
    from vanilla_mcdoc.assets.shader.program.Uniform import Uniform


class ShaderProgram(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'shader'

    vertex: Annotated[str, IdSpec(registry='shader/vertex')]
    fragment: Annotated[str, IdSpec(registry='shader/fragment')]
    samplers: list[Sampler] | None = None
    uniforms: list[Uniform]
    defines: Defines | None = None  # Defines GLSL directives to be injected into the shader source.
