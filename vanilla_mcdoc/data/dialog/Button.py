"""
Generated from symbols.json for ::java::data::dialog::Button
Local link to file: vanilla_mcdoc/data/dialog/Button.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.dialog.action.ClickAction import ClickAction
    from vanilla_mcdoc.util.text.Text import Text


class Button(GeneratedModel):
    label: Text
    tooltip: Text | None = None
    width: Annotated[int, Field(ge=1, le=1024)] | None = None  # Width of the button. Defaults to 150.
    action: ClickAction | None = None  # If not present, clicking button will simply close dialog without any action.
