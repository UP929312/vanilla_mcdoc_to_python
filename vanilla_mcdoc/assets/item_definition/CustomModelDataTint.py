"""
Generated from symbols.json for ::java::assets::item_definition::CustomModelDataTint
Local link to file: vanilla_mcdoc/assets/item_definition/CustomModelDataTint.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.util.color.RGB import RGB


class CustomModelDataTint(GeneratedModel):
    index: Annotated[int, Field(ge=0)] | None = None  # The index of the `colors` list in the `custom_model_data` component. Defaults to 0.
    default: RGB  # Tint to apply when the `custom_model_data` component is not present, or when it doesn't have a color in the specified index.
