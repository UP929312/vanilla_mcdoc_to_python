"""
Generated from symbols.json for ::java::data::loot::function::ReplaceSectionListOperation
Local link to file: vanilla_mcdoc/data/loot/function/ReplaceSectionListOperation.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel


class ReplaceSectionListOperation(GeneratedModel):
    offset: Annotated[int, Field(ge=0)] | None = None  # The offset of the section to replace. Defaults to 0.
    size: Annotated[int, Field(ge=0)] | None = None  # The size of the section to replace. Defaults to size of the new list.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::function::ReplaceSectionListOperation": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "The offset of the section to replace. Defaults to 0.",
                "key": "offset",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "The size of the section to replace. Defaults to size of the new list.",
                "key": "size",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0
                    }
                },
                "optional": True
            }
        ]
    }
}
