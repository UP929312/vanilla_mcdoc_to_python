# Generated from symbols.json for ::java::data::recipe::ItemResult
from dataclasses import dataclass
from typing import Annotated

from runtime_metadata import IdSpec


@dataclass(kw_only=True)
class ItemResult:
    item: Annotated[str, IdSpec(registry='item')]
    count: int | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::recipe::ItemResult": {
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
            },
            {
                "kind": "pair",
                "key": "count",
                "type": {
                    "kind": "int"
                },
                "optional": True
            }
        ]
    }
}

