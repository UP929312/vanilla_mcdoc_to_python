# Generated from symbols.json for ::java::data::tag::TagEntry
from dataclasses import dataclass
from typing import Generic, TypeVar


E = TypeVar('E')

@dataclass(kw_only=True)
class TagEntry(Generic[E]):
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

