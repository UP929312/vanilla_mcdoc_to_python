"""
Generated from symbols.json for ::java::assets::credits::CreditsJobTitle
Local link to file: generated_symbols/assets/credits/CreditsJobTitle.py
"""
# ~~~ CODE ~~~
from generated_symbols.base import GeneratedModel


class CreditsJobTitle(GeneratedModel):
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

