"""
Generated from symbols.json for ::java::data::dialog::body::PlainMessage
Local link to file: vanilla_mcdoc/data/dialog/body/PlainMessage.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.util.text.Text import Text


class PlainMessage(GeneratedModel):
    contents: Text  # A multiline label. Click events in the text trigger `after_action` like any other action.
    width: Annotated[int, Field(ge=1, le=1024)] | None = None  # Maximum width of message. Defaults to 200.
