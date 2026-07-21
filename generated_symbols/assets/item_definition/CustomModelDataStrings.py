# Generated from symbols.json for ::java::assets::item_definition::CustomModelDataStrings
from dataclasses import dataclass
from typing import Annotated
from generated_symbols.assets.item_definition.SelectCases import SelectCases


@dataclass(kw_only=True)
class CustomModelDataStrings(SelectCases[str]):
    index: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # The index of the `strings` list in the `custom_model_data` component. Defaults to 0.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::item_definition::CustomModelDataStrings": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "The index of the `strings` list in the `custom_model_data` component. Defaults to 0.",
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
                "kind": "spread",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::assets::item_definition::SelectCases"
                    },
                    "typeArgs": [
                        {
                            "kind": "string"
                        }
                    ]
                }
            }
        ]
    }
}

