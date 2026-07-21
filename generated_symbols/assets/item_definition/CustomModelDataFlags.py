# Generated from symbols.json for ::java::assets::item_definition::CustomModelDataFlags
from dataclasses import dataclass
from typing import Annotated


@dataclass(kw_only=True)
class CustomModelDataFlags:
    index: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # The index of the `flags` list in the `custom_model_data` component. Defaults to 0.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::item_definition::CustomModelDataFlags": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "The index of the `flags` list in the `custom_model_data` component. Defaults to 0.",
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

