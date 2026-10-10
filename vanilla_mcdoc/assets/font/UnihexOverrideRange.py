"""
Generated from symbols.json for ::java::assets::font::UnihexOverrideRange
Local link to file: vanilla_mcdoc/assets/font/UnihexOverrideRange.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel


class UnihexOverrideRange(GeneratedModel):
    from_: str = Field(alias='from')  # Minimum in codepoint range (inclusive).
    to: str  # Maximum in codepoint range (inclusive).
    left: Annotated[int, Field(ge=0, le=255)]  # Position of left-most column of the glyph.
    right: Annotated[int, Field(ge=0, le=255)]  # Position of right-most column of the glyph.
