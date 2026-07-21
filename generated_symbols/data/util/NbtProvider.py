# Generated from symbols.json for ::java::data::util::NbtProvider
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.util.NbtContextTarget import NbtContextTarget


@dataclass(kw_only=True)
class NbtProviderStruct1:
    type: str

type NbtProvider = NbtContextTarget | NbtProviderStruct1


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

