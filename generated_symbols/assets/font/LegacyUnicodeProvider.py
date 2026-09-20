"""
Generated from symbols.json for ::java::assets::font::LegacyUnicodeProvider
Local link to file: generated_symbols/assets/font/LegacyUnicodeProvider.py
"""
# ~~~ CODE ~~~
from generated_symbols.base import GeneratedModel


class LegacyUnicodeProvider(GeneratedModel):
    sizes: str
    template: str


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::font::LegacyUnicodeProvider": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "sizes",
                "type": {
                    "kind": "string"
                }
            },
            {
                "kind": "pair",
                "key": "template",
                "type": {
                    "kind": "string"
                }
            }
        ]
    }
}

