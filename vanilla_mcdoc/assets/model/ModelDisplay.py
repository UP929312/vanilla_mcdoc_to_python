"""
Generated from symbols.json for ::java::assets::model::ModelDisplay
Local link to file: vanilla_mcdoc/assets/model/ModelDisplay.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.assets.model.CustomizableItemDisplayContext import CustomizableItemDisplayContext


class ModelDisplayValueStruct(GeneratedModel):
    rotation: tuple[float, float, float] | None = None
    translation: tuple[Annotated[float, Field(ge=-80, le=80)], Annotated[float, Field(ge=-80, le=80)], Annotated[float, Field(ge=-80, le=80)]] | None = None
    scale: tuple[Annotated[float, Field(ge=-4, le=4)], Annotated[float, Field(ge=-4, le=4)], Annotated[float, Field(ge=-4, le=4)]] | None = None


type ModelDisplay = dict[CustomizableItemDisplayContext, ModelDisplayValueStruct]
