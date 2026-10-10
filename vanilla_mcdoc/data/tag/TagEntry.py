"""
Generated from symbols.json for ::java::data::tag::TagEntry
Local link to file: vanilla_mcdoc/data/tag/TagEntry.py
"""
# ~~~ CODE ~~~
from typing import Generic, TypeVar

from vanilla_mcdoc.base import GeneratedModel


E = TypeVar('E')


class TagEntry(GeneratedModel, Generic[E]):
    id: E
    required: bool | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::tag::TagEntry": {
        "kind": "template",
        "child": {
            "kind": "union",
            "members": [
                {
                    "kind": "reference",
                    "path": "::java::data::tag::E"
                },
                {
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
            ]
        },
        "typeParams": [
            {
                "path": "::java::data::tag::E"
            }
        ]
    }
}
