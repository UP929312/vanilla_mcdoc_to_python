"""
Generated from symbols.json for ::java::assets::texture_meta::MipmapStrategy
Local link to file: vanilla_mcdoc/assets/texture_meta/MipmapStrategy.py
"""
# ~~~ CODE ~~~
from enum import StrEnum


class MipmapStrategy(StrEnum):
    AUTO = "auto"
    MEAN = "mean"
    CUTOUT = "cutout"
    STRICTCUTOUT = "strict_cutout"
    DARKCUTOUT = "dark_cutout"
