"""
Generated from symbols.json for ::java::data::util::NbtProvider
Local link to file: generated_symbols/data/util/NbtProvider.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from generated_symbols.data.util.ContextNbtProvider import ContextNbtProvider
from generated_symbols.data.util.StorageNbtProvider import StorageNbtProvider

if TYPE_CHECKING:
    from generated_symbols.data.util.NbtContextTarget import NbtContextTarget


@dataclass(kw_only=True)
class NbtProviderStructContext(ContextNbtProvider):
    type: Literal['minecraft:context'] = 'minecraft:context'


@dataclass(kw_only=True)
class NbtProviderStructStorage(StorageNbtProvider):
    type: Literal['minecraft:storage'] = 'minecraft:storage'


type NbtProviderStruct = NbtProviderStructContext | NbtProviderStructStorage

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

