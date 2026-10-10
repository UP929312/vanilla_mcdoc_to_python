"""
Generated from symbols.json for ::java::assets::item_definition::CustomModelDataFloats
Local link to file: generated_symbols/assets/item_definition/CustomModelDataFloats.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from generated_symbols.base import GeneratedModel


class CustomModelDataFloats(GeneratedModel):
    index: Annotated[int, Field(ge=0)] | None = None  # The index of the `floats` list in the `custom_model_data` component. Defaults to 0.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::item_definition::CustomModelDataFloats": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "The index of the `floats` list in the `custom_model_data` component. Defaults to 0.",
                "key": "index",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0
                    }
                },
                "optional": True
            }
        ]
    }
}
