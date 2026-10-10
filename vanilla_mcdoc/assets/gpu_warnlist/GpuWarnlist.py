"""
Generated from symbols.json for ::java::assets::gpu_warnlist::GpuWarnlist
Local link to file: vanilla_mcdoc/assets/gpu_warnlist/GpuWarnlist.py
"""
# ~~~ CODE ~~~
from typing import ClassVar

from vanilla_mcdoc.base import GeneratedModel


class GpuWarnlist(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'gpu_warnlist'

    renderer: list[str] | None = None
    version: list[str] | None = None
    vendor: list[str] | None = None
