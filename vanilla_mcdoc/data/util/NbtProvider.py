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


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::util::NbtProvider": {
        "kind": "union",
        "members": [
            {
                "kind": "reference",
                "path": "::java::data::util::NbtContextTarget"
            },
            {
                "kind": "struct",
                "fields": [
                    {
                        "kind": "pair",
                        "key": "type",
                        "type": {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "loot_nbt_provider_type"
                                        }
                                    }
                                }
                            ]
                        }
                    },
                    {
                        "kind": "spread",
                        "type": {
                            "kind": "dispatcher",
                            "parallelIndices": [
                                {
                                    "kind": "dynamic",
                                    "accessor": [
                                        "type"
                                    ]
                                }
                            ],
                            "registry": "minecraft:nbt_provider"
                        }
                    }
                ]
            }
        ]
    }
}
