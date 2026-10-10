"""
Generated from symbols.json for ::java::assets::shader::post::TargetInput
Local link to file: vanilla_mcdoc/assets/shader/post/TargetInput.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec


class TargetInput(GeneratedModel):
    target: Annotated[str, IdSpec(registry='shader_target')]
    sampler_name: str
    use_depth_buffer: bool | None = None
    bilinear: bool | None = None
