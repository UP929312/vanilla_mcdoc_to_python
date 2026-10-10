"""
Generated from symbols.json for ::java::util::text::KeybindText
Local link to file: vanilla_mcdoc/util/text/KeybindText.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Literal

from vanilla_mcdoc.util.text.TextBase import TextBase

if TYPE_CHECKING:
    from vanilla_mcdoc.util.text.Keybind import Keybind


class KeybindText(TextBase):
    keybind: Keybind
    type: Literal['keybind'] | None = 'keybind'
