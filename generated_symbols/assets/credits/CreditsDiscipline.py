"""
Generated from symbols.json for ::java::assets::credits::CreditsDiscipline
Local link to file: generated_symbols/assets/credits/CreditsDiscipline.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from pydantic import Field

from generated_symbols.base import GeneratedModel


class TitlesStruct(GeneratedModel):
    title: str
    names: list[str]  # Employees with the title.


class CreditsDiscipline(GeneratedModel):
    discipline: Annotated[str, Field(min_length=1)] | Literal[""]
    titles: list[TitlesStruct]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::credits::CreditsDiscipline": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "discipline",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "string",
                            "lengthRange": {
                                "kind": 0,
                                "min": 1
                            }
                        },
                        {
                            "kind": "string",
                            "lengthRange": {
                                "kind": 0,
                                "min": 0,
                                "max": 0
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "titles",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "struct",
                        "fields": [
                            {
                                "kind": "pair",
                                "key": "title",
                                "type": {
                                    "kind": "string"
                                }
                            },
                            {
                                "kind": "pair",
                                "desc": "Employees with the title.",
                                "key": "names",
                                "type": {
                                    "kind": "list",
                                    "item": {
                                        "kind": "string"
                                    }
                                }
                            }
                        ]
                    }
                }
            }
        ]
    }
}

