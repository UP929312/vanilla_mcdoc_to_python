# Generated from symbols.json for ::java::assets::credits::CreditsDiscipline
from dataclasses import dataclass
from typing import Annotated, Any, Literal


@dataclass(kw_only=True)
class CreditsDiscipline:
    discipline: Annotated[str, 'Length = 1 (inclusive) and above'] | Literal[""]
    titles: list[Any]


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

