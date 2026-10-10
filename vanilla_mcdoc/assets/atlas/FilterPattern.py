"""
Generated from symbols.json for ::java::assets::atlas::FilterPattern
Local link to file: vanilla_mcdoc/assets/atlas/FilterPattern.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel


class FilterPattern(GeneratedModel):
    namespace: str | None = None
    path: str | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::atlas::FilterPattern": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "namespace",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "regex_pattern"
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "path",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "regex_pattern"
                        }
                    ]
                },
                "optional": True
            }
        ]
    }
}
