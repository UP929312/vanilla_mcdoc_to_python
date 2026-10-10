"""
Generated from symbols.json for ::java::data::worldgen::feature::EndGatewayConfig
Local link to file: vanilla_mcdoc/data/worldgen/feature/EndGatewayConfig.py
"""
# ~~~ CODE ~~~
from typing import ClassVar

from vanilla_mcdoc.base import GeneratedModel


class EndGatewayConfig(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

    exact: bool
    exit: tuple[int, int, int] | None = None
