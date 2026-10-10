"""
Generated from symbols.json for ::java::assets::model::ItemTransform
Local link to file: vanilla_mcdoc/assets/model/ItemTransform.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel


class ItemTransform(GeneratedModel):
    rotation: tuple[float, float, float] | None = None
    translation: tuple[Annotated[float, Field(ge=-80, le=80)], Annotated[float, Field(ge=-80, le=80)], Annotated[float, Field(ge=-80, le=80)]] | None = None
    scale: tuple[Annotated[float, Field(ge=-4, le=4)], Annotated[float, Field(ge=-4, le=4)], Annotated[float, Field(ge=-4, le=4)]] | None = None
