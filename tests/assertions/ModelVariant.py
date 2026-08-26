# ~~~ WHAT ARE WE TESTING ~~~

# Union members that are lists of structs need a named item class.

# ~~~ FILE CONTENT ~~~
"""
Generated from symbols.json for ::java::assets::block_state_definition::ModelVariant
Local link to file: generated_symbols/assets/block_state_definition/ModelVariant.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Annotated

from generated_symbols.assets.block_state_definition.ModelVariantBase import ModelVariantBase


@dataclass(kw_only=True)
class ModelVariantStruct(ModelVariantBase):
    weight: Annotated[int, 'Range | `1` and above | inclusive'] | None = None


type ModelVariant = ModelVariantBase | list[ModelVariantStruct]
