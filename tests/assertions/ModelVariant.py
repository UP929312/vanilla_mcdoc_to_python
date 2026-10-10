# ~~~ WHAT ARE WE TESTING ~~~

# Union members that are lists of structs need a named item class.

# ~~~ FILE CONTENT ~~~
"""
Generated from symbols.json for ::java::assets::block_state_definition::ModelVariant
Local link to file: generated_symbols/assets/block_state_definition/ModelVariant.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from generated_symbols.assets.block_state_definition.ModelVariantBase import ModelVariantBase


class ModelVariantStruct(ModelVariantBase):
    weight: Annotated[int, Field(ge=1)] | None = None


type ModelVariant = ModelVariantBase | list[ModelVariantStruct]
