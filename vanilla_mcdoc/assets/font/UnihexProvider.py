"""
Generated from symbols.json for ::java::assets::font::UnihexProvider
Local link to file: vanilla_mcdoc/assets/font/UnihexProvider.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.assets.font.UnihexOverrideRange import UnihexOverrideRange


class UnihexProvider(GeneratedModel):
    hex_file: str  # ZIP archive containing one or more *.hex files (files in archive with different extensions are ignored).
    size_overrides: list[UnihexOverrideRange] | None = None  # List of ranges to override the size of.
