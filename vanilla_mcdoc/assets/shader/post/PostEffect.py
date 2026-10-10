"""
Generated from symbols.json for ::java::assets::shader::post::PostEffect
Local link to file: vanilla_mcdoc/assets/shader/post/PostEffect.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.assets.shader.post.Pass import Pass
    from vanilla_mcdoc.assets.shader.post.Targets import Targets


class PostEffect(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'post_effect'

    targets: Targets | None = None
    passes: list[Pass] | None = None
