# Generated from symbols.json for ::java::util::text::KeybindText
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.util.text.TextBase import TextBase

if TYPE_CHECKING:
    from generated_symbols.util.text.Keybind import Keybind


@dataclass(kw_only=True)
class KeybindText(TextBase):
    keybind: Keybind
    type: str | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::text::KeybindText": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "keybind",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::text::Keybind"
                }
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.20.3"
                            }
                        }
                    }
                ],
                "key": "type",
                "type": {
                    "kind": "literal",
                    "value": {
                        "kind": "string",
                        "value": "keybind"
                    }
                },
                "optional": True
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::text::TextBase"
                }
            }
        ]
    }
}

