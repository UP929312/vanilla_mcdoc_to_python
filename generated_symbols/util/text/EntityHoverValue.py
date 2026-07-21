# Generated from symbols.json for ::java::util::text::EntityHoverValue
from dataclasses import dataclass


@dataclass(kw_only=True)
class EntityHoverValue:
    name: str | None = None
    type: str | None = None
    id: str | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::text::EntityHoverValue": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "name",
                "type": {
                    "kind": "string"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "type",
                "type": {
                    "kind": "string"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "id",
                "type": {
                    "kind": "string"
                },
                "optional": True
            }
        ]
    }
}

