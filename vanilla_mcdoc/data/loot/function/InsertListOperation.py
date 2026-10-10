"""
Generated from symbols.json for ::java::data::loot::function::InsertListOperation
Local link to file: vanilla_mcdoc/data/loot/function/InsertListOperation.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel


class InsertListOperation(GeneratedModel):
    offset: Annotated[int, Field(ge=0)] | None = None  # The offset in the list to insert into. Defaults to 0.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::function::InsertListOperation": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "The offset in the list to insert into. Defaults to 0.",
                "key": "offset",
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
