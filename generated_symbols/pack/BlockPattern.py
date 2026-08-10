"""
Generated from symbols.json for ::java::pack::BlockPattern
Local link to file: generated_symbols/pack/BlockPattern.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass


@dataclass(kw_only=True)
class BlockPattern:
    namespace: str | None = None
    path: str | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::pack::BlockPattern": {
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

