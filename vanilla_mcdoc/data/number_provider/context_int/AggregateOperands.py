"""
Generated from symbols.json for ::java::data::number_provider::context_int::AggregateOperands
Local link to file: vanilla_mcdoc/data/number_provider/context_int/AggregateOperands.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.number_provider.context_int.ContextIntProvider import ContextIntProvider
    from vanilla_mcdoc.data.number_provider.context_int.IntRef import IntRef
    from vanilla_mcdoc.registry.KnownContextIntProviderId import KnownContextIntProviderId


type AggregateOperands = ContextIntProvider | Annotated[str, IdSpec(registry='context_int_provider', tags='allowed')] | KnownContextIntProviderId | Annotated[list[IntRef], Field(min_length=1)]
