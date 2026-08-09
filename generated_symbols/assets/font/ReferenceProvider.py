# Generated from symbols.json for ::java::assets::font::ReferenceProvider
from dataclasses import dataclass
from typing import Annotated

from runtime_metadata import IdSpec


@dataclass(kw_only=True)
class ReferenceProvider:
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

