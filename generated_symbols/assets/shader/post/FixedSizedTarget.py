"""
Generated from symbols.json for ::java::assets::shader::post::FixedSizedTarget
Local link to file: generated_symbols/assets/shader/post/FixedSizedTarget.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass


@dataclass(kw_only=True)
class FixedSizedTarget:
    width: int
    height: int


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::shader::post::FixedSizedTarget": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "width",
                "type": {
                    "kind": "int"
                }
            },
            {
                "kind": "pair",
                "key": "height",
                "type": {
                    "kind": "int"
                }
            }
        ]
    }
}

