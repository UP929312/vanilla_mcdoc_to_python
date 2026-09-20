"""
Generated from symbols.json for ::java::assets::font::ReferenceProvider
Local link to file: generated_symbols/assets/font/ReferenceProvider.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from generated_symbols.base import GeneratedModel
from minecraft_registry import IdSpec


class ReferenceProvider(GeneratedModel):
    id: Annotated[str, IdSpec(registry='font')]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::font::ReferenceProvider": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "id",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "font"
                                }
                            }
                        }
                    ]
                }
            }
        ]
    }
}

