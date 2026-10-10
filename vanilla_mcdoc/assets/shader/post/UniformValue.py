"""
Generated from symbols.json for ::java::assets::shader::post::UniformValue
Local link to file: vanilla_mcdoc/assets/shader/post/UniformValue.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.assets.shader.post.UniformValueType import UniformValueType


class UniformValue(GeneratedModel):
    name: str | None = None  # Unused by the game, but good to set in practice.
    type: UniformValueType
    value: float | int | tuple[int, int, int] | tuple[float, float, float, float, float, float, float, float, float, float, float, float, float, float, float, float] | tuple[float, float] | tuple[float, float, float] | tuple[float, float, float, float]
