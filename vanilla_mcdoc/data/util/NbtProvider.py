"""
Generated from symbols.json for ::java::data::util::NbtProvider
Local link to file: vanilla_mcdoc/data/util/NbtProvider.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, Literal

from pydantic import Discriminator, Tag

from vanilla_mcdoc.base import tag_of
from vanilla_mcdoc.data.util.ContextNbtProvider import ContextNbtProvider
from vanilla_mcdoc.data.util.StorageNbtProvider import StorageNbtProvider

if TYPE_CHECKING:
    from vanilla_mcdoc.data.util.NbtContextTarget import NbtContextTarget


class NbtProviderStructContext(ContextNbtProvider):
    type: Literal['minecraft:context', 'context'] = 'minecraft:context'


class NbtProviderStructStorage(StorageNbtProvider):
    type: Literal['minecraft:storage', 'storage'] = 'minecraft:storage'


type NbtProviderStruct = Annotated[
    Annotated[NbtProviderStructContext, Tag('minecraft:context')]
    | Annotated[NbtProviderStructStorage, Tag('minecraft:storage')],
    Discriminator(tag_of('type')),
]


type NbtProvider = NbtContextTarget | NbtProviderStruct
