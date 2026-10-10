"""
Generated from symbols.json for ::java::assets::model::Model
Local link to file: vanilla_mcdoc/assets/model/Model.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar, Literal

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.assets.model.CustomizableItemDisplayContext import CustomizableItemDisplayContext
    from vanilla_mcdoc.assets.model.ModelElement import ModelElement
    from vanilla_mcdoc.assets.model.TextureMaterial import TextureMaterial


class DisplayStructValueStruct(GeneratedModel):
    rotation: tuple[float, float, float] | None = None
    translation: tuple[Annotated[float, Field(ge=-80, le=80)], Annotated[float, Field(ge=-80, le=80)], Annotated[float, Field(ge=-80, le=80)]] | None = None
    scale: tuple[Annotated[float, Field(ge=-4, le=4)], Annotated[float, Field(ge=-4, le=4)], Annotated[float, Field(ge=-4, le=4)]] | None = None


class Model(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'model'

    parent: Annotated[str, IdSpec(registry='model')] | None = None
    ambientocclusion: bool | None = None
    gui_light: Literal['front'] | Literal['side'] | None = None
    textures: dict[str, str | TextureMaterial] | None = None
    elements: list[ModelElement] | None = None
    display: dict[CustomizableItemDisplayContext, DisplayStructValueStruct] | None = None
