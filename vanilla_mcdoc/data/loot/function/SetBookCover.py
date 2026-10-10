"""
Generated from symbols.json for ::java::data::loot::function::SetBookCover
Local link to file: vanilla_mcdoc/data/loot/function/SetBookCover.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.data.loot.function.Conditions import Conditions

if TYPE_CHECKING:
    from vanilla_mcdoc.util.Filterable import Filterable


class SetBookCover(Conditions):
    title: Filterable[Annotated[str, Field(min_length=0, max_length=32)]] | None = None  # If omitted, the original title is kept (or an empty string is used if there was no component)
    author: str | None = None  # If omitted, the original author is kept (or an empty string is used if there was no component)
    generation: Annotated[int, Field(ge=0, le=3)] | None = None  # If omitted, the original generation is kept (or 0 is used if there was no component)


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::function::SetBookCover": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "If omitted, the original title is kept (or an empty string is used if there was no component)",
                "key": "title",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::util::Filterable"
                    },
                    "typeArgs": [
                        {
                            "kind": "string",
                            "lengthRange": {
                                "kind": 0,
                                "min": 0,
                                "max": 32
                            }
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "If omitted, the original author is kept (or an empty string is used if there was no component)",
                "key": "author",
                "type": {
                    "kind": "string"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "If omitted, the original generation is kept (or 0 is used if there was no component)",
                "key": "generation",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 3
                    }
                },
                "optional": True
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::loot::function::Conditions"
                }
            }
        ]
    }
}
