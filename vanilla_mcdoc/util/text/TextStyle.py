"""
Generated from symbols.json for ::java::util::text::TextStyle
Local link to file: vanilla_mcdoc/util/text/TextStyle.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.util.color.RGBA import RGBA
    from vanilla_mcdoc.util.text.ClickEvent import ClickEvent
    from vanilla_mcdoc.util.text.HoverEvent import HoverEvent
    from vanilla_mcdoc.util.text.TextColor import TextColor


class TextStyle(GeneratedModel):
    color: Annotated[str, Field(pattern='^#')] | TextColor | None = None
    shadow_color: RGBA | None = None  # Overrides the shadow properties of the text. If specified as 0, the shadow will never be displayed.
    font: Annotated[str, IdSpec(registry='font')] | None = None
    bold: bool | None = None
    italic: bool | None = None
    underlined: bool | None = None
    strikethrough: bool | None = None
    obfuscated: bool | None = None
    insertion: str | None = None
    click_event: ClickEvent | None = None
    hover_event: HoverEvent | None = None
