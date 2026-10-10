"""
Generated from symbols.json for ::java::data::number_provider::context_int::SingleProvider
Local link to file: vanilla_mcdoc/data/number_provider/context_int/SingleProvider.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.number_provider.context_int.IntRef import IntRef


class SingleProvider(GeneratedModel):
    input: IntRef
