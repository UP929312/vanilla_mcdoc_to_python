"""
Generated from symbols.json for ::java::assets::credits::CreditsCompanySegment
Local link to file: vanilla_mcdoc/assets/credits/CreditsCompanySegment.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel


class TitlesStruct(GeneratedModel):
    title: str
    names: list[str]  # Employees with the title.


class DisciplinesStruct(GeneratedModel):
    discipline: Annotated[str, Field(min_length=1)] | Literal[""]
    titles: list[TitlesStruct]


class CreditsCompanySegment(GeneratedModel):
    section: str  # Company segment.
    disciplines: list[DisciplinesStruct]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::credits::CreditsCompanySegment": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Company segment.",
                "key": "section",
                "type": {
                    "kind": "string"
                }
            },
            {
                "kind": "pair",
                "key": "disciplines",
                "type": {
                    "kind": "list",
                    "item": {
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
            }
        ]
    }
}
