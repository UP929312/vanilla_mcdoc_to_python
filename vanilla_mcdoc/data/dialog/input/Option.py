"""
Generated from symbols.json for ::java::data::dialog::input::Option
Local link to file: vanilla_mcdoc/data/dialog/input/Option.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.util.text.Text import Text


class Option(GeneratedModel):
    id: str  # String to send on submit.
    display: Text | None = None  # Label displayed on the button. When not present, `id` will be used instead.
    initial: bool | None = None  # Whether this option is the initial value. Only one option can have this field set to `true`.
