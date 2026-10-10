"""
Generated from symbols.json for ::java::assets::item_definition::CustomModelDataStrings
Local link to file: vanilla_mcdoc/assets/item_definition/CustomModelDataStrings.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.assets.item_definition.SelectCases import SelectCases


class CustomModelDataStrings(SelectCases[str]):
    index: Annotated[int, Field(ge=0)] | None = None  # The index of the `strings` list in the `custom_model_data` component. Defaults to 0.
