"""
Generated from symbols.json for ::java::pack::Pack
Local link to file: vanilla_mcdoc/pack/Pack.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.pack.PackFeatures import PackFeatures
    from vanilla_mcdoc.pack.PackFilter import PackFilter
    from vanilla_mcdoc.pack.PackFormat import PackFormat
    from vanilla_mcdoc.pack.PackOverlays import PackOverlays
    from vanilla_mcdoc.util.InclusiveRange import InclusiveRange
    from vanilla_mcdoc.util.text.Text import Text


class PackStruct(GeneratedModel):
    description: Text
    pack_format: int | None = None  # Optional since 1.21.9. Define it if you want older versions to recognize your pack with a “made for a newer version” warning message.  Because of backwards compatibility, only the main pack format can be used here. Minor formats can only be specified in min and max format.
    supported_formats: InclusiveRange[int] | int | None = None  # Must not be specified in case min_format indicates a format version for 1.21.9 and later.
    min_format: PackFormat | None = None  # The minimun format that is supported. To specify a minor version, use a list of two integers.
    max_format: PackFormat | None = None  # The maximum format that is supported. To specify a minor version, use a list of two integers.


class Pack(GeneratedModel):
    pack: PackStruct
    filter: PackFilter | None = None
    features: PackFeatures | None = None
    overlays: PackOverlays | None = None
