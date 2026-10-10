"""
Generated from symbols.json for ::java::data::util::NbtProvider
Local link to file: vanilla_mcdoc/data/util/NbtProvider.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, Literal

from pydantic import Field

from vanilla_mcdoc.data.util.ContextNbtProvider import ContextNbtProvider
from vanilla_mcdoc.data.util.StorageNbtProvider import StorageNbtProvider

if TYPE_CHECKING:
    from vanilla_mcdoc.data.util.NbtContextTarget import NbtContextTarget


class NbtProviderStructContext(ContextNbtProvider):
    type: Literal['minecraft:context', 'context'] = 'minecraft:context'


class NbtProviderStructStorage(StorageNbtProvider):
    type: Literal['minecraft:storage', 'storage'] = 'minecraft:storage'


type NbtProviderStruct = Annotated[
    NbtProviderStructContext | NbtProviderStructStorage,
    Field(discriminator='type'),
]


type NbtProvider = NbtContextTarget | NbtProviderStruct
