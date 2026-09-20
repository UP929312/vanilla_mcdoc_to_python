"""
Generated from symbols.json for ::java::util::text::CopyToClipboard
Local link to file: generated_symbols/util/text/CopyToClipboard.py
"""
# ~~~ CODE ~~~
from generated_symbols.base import GeneratedModel


class CopyToClipboard(GeneratedModel):
    value: str  # The text value to copy to the clipboard.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::text::CopyToClipboard": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "The text value to copy to the clipboard.",
                "key": "value",
                "type": {
                    "kind": "string"
                }
            }
        ]
    }
}

