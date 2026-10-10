"""
Generated from symbols.json for ::java::assets::font::TtfProvider
Local link to file: vanilla_mcdoc/assets/font/TtfProvider.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel


class TtfProvider(GeneratedModel):
    file: str
    size: float | None = None
    oversample: float | None = None
    shift: tuple[float, float] | None = None
    skip: str | list[str] | None = None
