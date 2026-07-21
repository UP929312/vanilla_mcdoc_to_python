# Generated from symbols.json for ::java::assets::item_definition::KeybindDown
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.util.text.Keybind import Keybind


@dataclass(kw_only=True)
class KeybindDown:
    keybind: Keybind  # The keybind ID to check for.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::item_definition::KeybindDown": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "The keybind ID to check for.",
                "key": "keybind",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::text::Keybind"
                }
            }
        ]
    }
}

