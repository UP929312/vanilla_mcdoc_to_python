"""
Generated from symbols.json for ::java::pack::PackFeatures
Local link to file: vanilla_mcdoc/pack/PackFeatures.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.pack.FeatureFlag import FeatureFlag


class PackFeatures(GeneratedModel):
    enabled: list[FeatureFlag]
