"""
Generated from symbols.json for ::java::assets::item_definition::CustomModelDataFlags
Local link to file: vanilla_mcdoc/assets/item_definition/CustomModelDataFlags.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel


class CustomModelDataFlags(GeneratedModel):
    index: Annotated[int, Field(ge=0)] | None = None  # The index of the `flags` list in the `custom_model_data` component. Defaults to 0.
