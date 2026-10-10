"""
Generated from symbols.json for ::java::assets::shader::post::Targets
Local link to file: vanilla_mcdoc/assets/shader/post/Targets.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.assets.shader.post.InternalTarget import InternalTarget


type Targets = dict[Annotated[str, IdSpec(registry='shader_target')], InternalTarget]
