# Generated from symbols.json for ::java::data::recipe::IngredientTag
from dataclasses import dataclass
from typing import Annotated

from runtime_metadata import IdSpec


@dataclass(kw_only=True)
class IngredientTag:
    tag: Annotated[str, IdSpec(registry='item', tags='implicit')]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::recipe::IngredientTag": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "tag",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "tree",
                                "values": {
                                    "registry": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "item"
                                        }
                                    },
                                    "tags": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "implicit"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                }
            }
        ]
    }
}

