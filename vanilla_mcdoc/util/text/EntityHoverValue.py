"""
Generated from symbols.json for ::java::util::text::EntityHoverValue
Local link to file: vanilla_mcdoc/util/text/EntityHoverValue.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel


class EntityHoverValue(GeneratedModel):
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
