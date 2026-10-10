"""
Generated from symbols.json for ::java::assets::shader::post::Pass
Local link to file: vanilla_mcdoc/assets/shader/post/Pass.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.assets.shader.post.TargetInput import TargetInput
    from vanilla_mcdoc.assets.shader.post.TextureInput import TextureInput
    from vanilla_mcdoc.assets.shader.post.UniformBlocks import UniformBlocks


class Pass(GeneratedModel):
    vertex_shader: Annotated[str, IdSpec(registry='shader/vertex')]
    fragment_shader: Annotated[str, IdSpec(registry='shader/fragment')]
    inputs: list[TargetInput | TextureInput] | None = None
    output: Annotated[str, IdSpec(registry='shader_target')]
    uniforms: UniformBlocks | None = None
