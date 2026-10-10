"""
Generated from symbols.json for ::java::assets::item_definition::CustomModelDataFloats
Local link to file: vanilla_mcdoc/assets/item_definition/CustomModelDataFloats.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel


class CustomModelDataFloats(GeneratedModel):
    index: Annotated[int, Field(ge=0)] | None = None  # The index of the `floats` list in the `custom_model_data` component. Defaults to 0.
