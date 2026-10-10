"""
Generated from symbols.json for ::java::data::number_provider::legacy::EnvironmentAttributeNumberProvider
Local link to file: vanilla_mcdoc/data/number_provider/legacy/EnvironmentAttributeNumberProvider.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.attribute.NumericalEnvironmentAttribute import NumericalEnvironmentAttribute


class EnvironmentAttributeNumberProvider(GeneratedModel):
    attribute: NumericalEnvironmentAttribute
