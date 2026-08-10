"""
Generated from symbols.json for ::java::data::recipe::SmithingTransformResult
Local link to file: generated_symbols/data/recipe/SmithingTransformResult.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Annotated

from runtime_metadata import IdSpec


@dataclass(kw_only=True)
class SmithingTransformResult:
    item: Annotated[str, IdSpec(registry='item')]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::recipe::SmithingTransformResult": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "item",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "item"
                                }
                            }
                        }
                    ]
                }
            }
        ],
        "attributes": [
            {
                "name": "until",
                "value": {
                    "kind": "literal",
                    "value": {
                        "kind": "string",
                        "value": "1.20.5"
                    }
                }
            }
        ]
    }
}

