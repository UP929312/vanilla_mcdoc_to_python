"""
Generated from symbols.json for ::java::assets::credits::Credits
Local link to file: generated_symbols/assets/credits/Credits.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Annotated, Literal


@dataclass(kw_only=True)
class TitlesStruct:
    title: str
    names: list[str]  # Employees with the title.


@dataclass(kw_only=True)
class DisciplinesStruct:
    discipline: Annotated[str, 'Length = 1 (inclusive) and above'] | Literal[""]
    titles: list[TitlesStruct]


@dataclass(kw_only=True)
class CreditsStruct:
    section: str  # Company segment.
    disciplines: list[DisciplinesStruct]


type Credits = list[CreditsStruct]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::credits::Credits": {
        "kind": "list",
        "item": {
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
}

