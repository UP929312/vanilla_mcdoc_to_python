# Generated from symbols.json for ::java::assets::credits::Credits
from typing import Any


type Credits = list[Any]


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

