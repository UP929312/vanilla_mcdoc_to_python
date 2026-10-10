"""
Generated from symbols.json for ::java::data::number_provider::context_float::AggregateOperands
Local link to file: vanilla_mcdoc/data/number_provider/context_float/AggregateOperands.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.number_provider.context_float.ContextFloatProvider import ContextFloatProvider
    from vanilla_mcdoc.data.number_provider.context_float.FloatRef import FloatRef
    from vanilla_mcdoc.registry.KnownContextFloatProviderId import KnownContextFloatProviderId


type AggregateOperands = ContextFloatProvider | Annotated[str, IdSpec(registry='context_float_provider', tags='allowed')] | KnownContextFloatProviderId | Annotated[list[FloatRef], Field(min_length=1)]
