# Generated from symbols.json for ::java::assets::credits::CreditsJobTitle
from dataclasses import dataclass


@dataclass(kw_only=True)
class CreditsJobTitle:
    title: str
    names: list[str]  # Employees with the title.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::credits::CreditsJobTitle": {
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

