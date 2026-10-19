"""
Generated from symbols.json for ::java::assets::shader::post::UniformValue
Local link to file: vanilla_mcdoc/assets/shader/post/UniformValue.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from pydantic import Discriminator, Tag

from vanilla_mcdoc.base import GeneratedModel, tag_of


class UniformValueFloat(GeneratedModel):
    name: str | None = None  # Unused by the game, but good to set in practice.
    type: Literal['minecraft:float', 'float'] = 'minecraft:float'
    value: float


class UniformValueInt(GeneratedModel):
    name: str | None = None  # Unused by the game, but good to set in practice.
    type: Literal['minecraft:int', 'int'] = 'minecraft:int'
    value: int


class UniformValueIvec3(GeneratedModel):
    name: str | None = None  # Unused by the game, but good to set in practice.
    type: Literal['minecraft:ivec3', 'ivec3'] = 'minecraft:ivec3'
    value: tuple[int, int, int]


class UniformValueMatrix4x4(GeneratedModel):
    name: str | None = None  # Unused by the game, but good to set in practice.
    type: Literal['minecraft:matrix4x4', 'matrix4x4'] = 'minecraft:matrix4x4'
    value: tuple[float, float, float, float, float, float, float, float, float, float, float, float, float, float, float, float]


class UniformValueVec2(GeneratedModel):
    name: str | None = None  # Unused by the game, but good to set in practice.
    type: Literal['minecraft:vec2', 'vec2'] = 'minecraft:vec2'
    value: tuple[float, float]


class UniformValueVec3(GeneratedModel):
    name: str | None = None  # Unused by the game, but good to set in practice.
    type: Literal['minecraft:vec3', 'vec3'] = 'minecraft:vec3'
    value: tuple[float, float, float]


class UniformValueVec4(GeneratedModel):
    name: str | None = None  # Unused by the game, but good to set in practice.
    type: Literal['minecraft:vec4', 'vec4'] = 'minecraft:vec4'
    value: tuple[float, float, float, float]


type UniformValue = Annotated[
    Annotated[UniformValueFloat, Tag('minecraft:float')]
    | Annotated[UniformValueInt, Tag('minecraft:int')]
    | Annotated[UniformValueIvec3, Tag('minecraft:ivec3')]
    | Annotated[UniformValueMatrix4x4, Tag('minecraft:matrix4x4')]
    | Annotated[UniformValueVec2, Tag('minecraft:vec2')]
    | Annotated[UniformValueVec3, Tag('minecraft:vec3')]
    | Annotated[UniformValueVec4, Tag('minecraft:vec4')],
    Discriminator(tag_of('type')),
]
