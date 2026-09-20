"""
Generated from symbols.json for ::java::assets::item_definition::CustomModelDataTint
Local link to file: generated_symbols/assets/item_definition/CustomModelDataTint.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from generated_symbols.base import GeneratedModel
from pydantic import Field

if TYPE_CHECKING:
    from generated_symbols.util.color.RGB import RGB


class CustomModelDataTint(GeneratedModel):
    index: Annotated[int, Field(ge=0)] | None = None  # The index of the `colors` list in the `custom_model_data` component. Defaults to 0.
    default: RGB  # Tint to apply when the `custom_model_data` component is not present, or when it doesn't have a color in the specified index.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::item_definition::CustomModelDataTint": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "The index of the `colors` list in the `custom_model_data` component. Defaults to 0.",
                "key": "index",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Tint to apply when the `custom_model_data` component is not present, or when it doesn't have a color in the specified index.",
                "key": "default",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::color::RGB"
                }
            }
        ]
    }
}

