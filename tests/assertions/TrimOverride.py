# ~~~ WHAT ARE WE TESTING ~~~

# Lowercase pair keys are converted to PascalCase when naming nested structs.
# This avoids weird `whenStruct`

# ~~~ FILE CONTENT ~~~
"""
Generated from symbols.json for ::java::assets::equipment::TrimOverride
Local link to file: generated_symbols/assets/equipment/TrimOverride.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

from runtime_metadata import IdSpec

if TYPE_CHECKING:
    from generated_symbols.assets.atlas.PaletteRef import PaletteRef


@dataclass(kw_only=True)
class WhenStruct:
    pattern: Annotated[str, IdSpec(registry='trim_pattern')] | None = None
    material: Annotated[str, IdSpec(registry='trim_material')] | None = None


@dataclass(kw_only=True)
class TrimOverride:
    when: WhenStruct
    texture: Annotated[str, IdSpec()] | None = None  # When present, overrides the base texture provided by trim pattern.  The texture is located under `trims/entity/<layer>/`.
    palette: PaletteRef | None = None  # When present, overrides the palette texture provided by trim material.
