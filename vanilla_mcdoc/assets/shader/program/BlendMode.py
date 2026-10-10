"""
Generated from symbols.json for ::java::assets::shader::program::BlendMode
Local link to file: vanilla_mcdoc/assets/shader/program/BlendMode.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.assets.shader.program.BlendFactor import BlendFactor
    from vanilla_mcdoc.assets.shader.program.BlendFunc import BlendFunc


class BlendMode(GeneratedModel):
    func: BlendFunc | None = None
    srcrgb: BlendFactor | None = None
    dstrgb: BlendFactor | None = None
    srcalpha: BlendFactor | None = None
    dstalpha: BlendFactor | None = None
