"""
Generated from symbols.json for ::java::data::worldgen::TrapezoidHeightProvider
Local link to file: vanilla_mcdoc/data/worldgen/TrapezoidHeightProvider.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.data.worldgen.UniformHeightProvider import UniformHeightProvider


class TrapezoidHeightProvider(UniformHeightProvider):
    plateau: int | None = None
