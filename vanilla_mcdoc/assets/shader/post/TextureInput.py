"""
Generated from symbols.json for ::java::assets::shader::post::TextureInput
Local link to file: vanilla_mcdoc/assets/shader/post/TextureInput.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec


class TextureInput(GeneratedModel):
    location: Annotated[str, IdSpec(registry='texture', path='effect/')]
    sampler_name: str
    width: Annotated[int, Field(ge=1)]
    height: Annotated[int, Field(ge=1)]
    bilinear: bool | None = None
