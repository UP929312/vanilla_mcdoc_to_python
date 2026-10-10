"""
Generated from symbols.json for ::java::assets::model::ModelElement
Local link to file: vanilla_mcdoc/assets/model/ModelElement.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, Literal

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.assets.model.ModelElementRotation import ModelElementRotation
    from vanilla_mcdoc.util.direction.Direction import Direction


class FacesStructValueStruct(GeneratedModel):
    texture: str
    uv: tuple[float, float, float, float] | None = None
    cullface: Direction | None = None
    rotation: Literal[0] | Literal[90] | Literal[180] | Literal[270] | None = None
    tintindex: int | None = None


class ModelElement(GeneratedModel):
    from_: tuple[Annotated[float, Field(ge=-16, le=32)], Annotated[float, Field(ge=-16, le=32)], Annotated[float, Field(ge=-16, le=32)]] = Field(alias='from')
    to: tuple[Annotated[float, Field(ge=-16, le=32)], Annotated[float, Field(ge=-16, le=32)], Annotated[float, Field(ge=-16, le=32)]]
    faces: dict[Direction, FacesStructValueStruct]
    rotation: ModelElementRotation | None = None
    shade_direction_override: Direction | None = None
    light_emission: Annotated[int, Field(ge=0, le=15)] | None = None
