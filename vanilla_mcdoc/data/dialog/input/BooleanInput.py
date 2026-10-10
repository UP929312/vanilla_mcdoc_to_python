"""
Generated from symbols.json for ::java::data::dialog::input::BooleanInput
Local link to file: vanilla_mcdoc/data/dialog/input/BooleanInput.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.util.text.Text import Text


class BooleanInput(GeneratedModel):
    label: Text  # Label displayed to the right of control.
    initial: bool | None = None  # Initial value of the control. Defaults to `false` (unchecked).
    on_true: str | None = None  # String to send when the control is checked. Defaults to `"true"`.
    on_false: str | None = None  # String to send when the control is unchecked. Defaults to `"false"`.
