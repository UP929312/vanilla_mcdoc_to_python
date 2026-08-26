"""
Generated from symbols.json for ::java::assets::item_definition::CustomModelDataFloats
Local link to file: generated_symbols/assets/item_definition/CustomModelDataFloats.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Annotated


@dataclass(kw_only=True)
class CustomModelDataFloats:
    index: Annotated[int, 'Range | `0` and above | inclusive'] | None = None  # The index of the `floats` list in the `custom_model_data` component. Defaults to 0.


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

