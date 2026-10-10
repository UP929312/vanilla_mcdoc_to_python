"""
Generated from symbols.json for ::java::assets::item_definition::Time
Local link to file: vanilla_mcdoc/assets/item_definition/Time.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.assets.item_definition.TimeSource import TimeSource


class Time(GeneratedModel):
    source: TimeSource
    wobble: bool | None = None  # Whether to oscillate for some time around target before settling. Defaults to true.
