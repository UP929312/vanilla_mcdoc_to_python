"""
Generated from symbols.json for ::java::data::dialog::input::TextInput
Local link to file: vanilla_mcdoc/data/dialog/input/TextInput.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.util.text.Text import Text


class MultilineStruct(GeneratedModel):
    max_lines: Annotated[int, Field(ge=1)] | None = None
    height: Annotated[int, Field(ge=1, le=512)] | None = None  # Height of the input. If this field is not present: - If `max_lines` is present, the height will be chosen to fit the maximum number of lines. The chosen height is capped at 512. - If `max_lines` is also not present, the height will be chosen to fit 4 lines.


class TextInput(GeneratedModel):
    width: Annotated[int, Field(ge=1, le=1024)] | None = None  # Defaults to 200.
    label: Text  # Label displayed to the left of control.
    label_visible: bool | None = None  # Defaults to `true`.
    initial: str | None = None  # Initial contents of the text input. Defaults to `""` (empty string).
    max_length: Annotated[int, Field(ge=1)] | None = None  # Maximum length of input Defaults to 32.
    multiline: MultilineStruct | None = None  # If present, allows users to input multiple lines.
