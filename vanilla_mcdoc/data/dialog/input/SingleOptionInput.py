"""
Generated from symbols.json for ::java::data::dialog::input::SingleOptionInput
Local link to file: vanilla_mcdoc/data/dialog/input/SingleOptionInput.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.dialog.input.Option import Option
    from vanilla_mcdoc.util.text.Text import Text


class SingleOptionInput(GeneratedModel):
    width: Annotated[int, Field(ge=1, le=1024)] | None = None  # Defaults to 200.
    label: Text  # Label displayed on the button.
    label_visible: bool | None = None  # Defaults to `true`.
    options: Annotated[list[Option | str], Field(min_length=1)]
