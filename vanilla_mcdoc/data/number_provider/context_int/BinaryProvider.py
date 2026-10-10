"""
Generated from symbols.json for ::java::data::number_provider::context_int::BinaryProvider
Local link to file: vanilla_mcdoc/data/number_provider/context_int/BinaryProvider.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.number_provider.context_int.IntRef import IntRef


class BinaryProvider(GeneratedModel):
    left: IntRef
    right: IntRef
