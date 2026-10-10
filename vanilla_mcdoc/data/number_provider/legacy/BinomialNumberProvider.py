"""
Generated from symbols.json for ::java::data::number_provider::legacy::BinomialNumberProvider
Local link to file: vanilla_mcdoc/data/number_provider/legacy/BinomialNumberProvider.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.number_provider.legacy.LegacyNumberProvider import LegacyNumberProvider


class BinomialNumberProvider(GeneratedModel):
    n: LegacyNumberProvider
    p: LegacyNumberProvider
