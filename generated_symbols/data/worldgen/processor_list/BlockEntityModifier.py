# Generated from symbols.json for ::java::data::worldgen::processor_list::BlockEntityModifier
from dataclasses import dataclass
from typing import Annotated, Any, Literal

from runtime_metadata import IdSpec


@dataclass(kw_only=True)
class DataStruct:
    pass


@dataclass(kw_only=True)
class BlockEntityModifierAppendLoot:
    type: Literal['minecraft:append_loot']
    loot_table: Annotated[str, IdSpec(registry='loot_table')]


@dataclass(kw_only=True)
class BlockEntityModifierAppendStatic:
    type: Literal['minecraft:append_static']
    data: DataStruct


@dataclass(kw_only=True)
class BlockEntityModifierClear:
    type: Literal['minecraft:clear']


@dataclass(kw_only=True)
class BlockEntityModifierPassthrough:
    type: Literal['minecraft:passthrough']


type BlockEntityModifier = BlockEntityModifierAppendLoot | BlockEntityModifierAppendStatic | BlockEntityModifierClear | BlockEntityModifierPassthrough


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::processor_list::BlockEntityModifier": {
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
                                    "value": "rule_block_entity_modifier"
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
                    "registry": "minecraft:rule_block_entity_modifier"
                }
            }
        ]
    }
}

