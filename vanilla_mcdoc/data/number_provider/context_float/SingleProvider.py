"""
Generated from symbols.json for ::java::data::number_provider::context_float::SingleProvider
Local link to file: vanilla_mcdoc/data/number_provider/context_float/SingleProvider.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.number_provider.context_float.FloatRef import FloatRef


class SingleProvider(GeneratedModel):
    input: FloatRef
