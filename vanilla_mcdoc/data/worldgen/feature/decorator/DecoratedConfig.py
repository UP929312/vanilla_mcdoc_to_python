"""
Generated from symbols.json for ::java::data::worldgen::feature::decorator::DecoratedConfig
Local link to file: vanilla_mcdoc/data/worldgen/feature/decorator/DecoratedConfig.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.feature.decorator.ConfiguredDecorator import ConfiguredDecorator


class DecoratedConfig(GeneratedModel):
    outer: ConfiguredDecorator
    inner: ConfiguredDecorator
