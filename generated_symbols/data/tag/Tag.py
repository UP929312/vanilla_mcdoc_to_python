"""
Generated from symbols.json for ::java::data::tag::Tag
Local link to file: generated_symbols/data/tag/Tag.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Generic, TypeVar

if TYPE_CHECKING:
    from generated_symbols.data.tag.TagEntry import TagEntry


E = TypeVar('E')

@dataclass(kw_only=True)
class Tag(Generic[E]):
    replace: bool | None = None
    values: list[TagEntry[E]]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::tag::Tag": {
        "kind": "template",
        "child": {
            "kind": "struct",
            "fields": [
                {
                    "kind": "pair",
                    "key": "replace",
                    "type": {
                        "kind": "boolean"
                    },
                    "optional": True
                },
                {
                    "kind": "pair",
                    "key": "values",
                    "type": {
                        "kind": "list",
                        "item": {
                            "kind": "concrete",
                            "child": {
                                "kind": "reference",
                                "path": "::java::data::tag::TagEntry"
                            },
                            "typeArgs": [
                                {
                                    "kind": "reference",
                                    "path": "::java::data::tag::E"
                                }
                            ]
                        }
                    }
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

