# Generated from symbols.json for ::java::util::text::CopyToClipboard
from dataclasses import dataclass


@dataclass(kw_only=True)
class CopyToClipboard:
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

