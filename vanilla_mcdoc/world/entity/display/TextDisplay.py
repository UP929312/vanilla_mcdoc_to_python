"""
Generated from symbols.json for ::java::world::entity::display::TextDisplay
Local link to file: vanilla_mcdoc/world/entity/display/TextDisplay.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.world.entity.display.DisplayBase import DisplayBase

if TYPE_CHECKING:
    from vanilla_mcdoc.util.text.Text import Text
    from vanilla_mcdoc.world.entity.display.TextAlignment import TextAlignment


class TextDisplay(DisplayBase):
    text: Text | None = None  # Text to display. Components are resolved with the executor set to the display entity and the position set to `0 0 0`.
    line_width: Annotated[int, Field(ge=0)] | None = None  # Line width in pixels used to split lines (note: new line can also be added with `\n` characters). Defaults to 200.
    text_opacity: Annotated[int, Field(ge=0, le=255)] | None = None  # Opacity (alpha component) of rendered text. Defaults to 255. Interpolated.
    background: int | None = None  # Color of background. Includes alpha channel. Defaults to 0x40000000. Interpolated.  Calculated as `ALPHA << 24 | RED << 16 | GREEN << 8 | BLUE`. Each of these fields must be between 0 and 255, inclusive.
    default_background: bool | None = None  # If true, overrides `background` & rendering uses default text background color (same as in chat). Defaults to false.
    shadow: bool | None = None  # Whether to display the text with shadows. Defaults to false.
    see_through: bool | None = None  # Whether the text should be visible through opaque blocks. Defaults to false.
    alignment: TextAlignment | None = None  # How text should be aligned. Defaults to `center`.
