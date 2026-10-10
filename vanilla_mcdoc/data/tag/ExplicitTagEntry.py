"""
Generated from symbols.json for ::java::data::tag::ExplicitTagEntry
Local link to file: vanilla_mcdoc/data/tag/ExplicitTagEntry.py
"""
# ~~~ CODE ~~~
from typing import Generic, TypeVar

from vanilla_mcdoc.base import GeneratedModel


E = TypeVar('E')


class ExplicitTagEntry(GeneratedModel, Generic[E]):
    id: E
    required: bool | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::tag::ExplicitTagEntry": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "id",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::tag::E"
                }
            },
            {
                "kind": "pair",
                "key": "required",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ],
        "attributes": [
            {
                "name": "since",
                "value": {
                    "kind": "literal",
                    "value": {
                        "kind": "string",
                        "value": "1.16.2"
                    }
                }
            }
        ]
    }
}
