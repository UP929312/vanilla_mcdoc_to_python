"""
Generated from symbols.json for ::java::assets::item_definition::KeybindDown
Local link to file: vanilla_mcdoc/assets/item_definition/KeybindDown.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.util.text.Keybind import Keybind


class KeybindDown(GeneratedModel):
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
