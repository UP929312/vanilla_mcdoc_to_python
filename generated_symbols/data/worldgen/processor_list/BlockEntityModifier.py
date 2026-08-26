"""
Generated from symbols.json for ::java::data::worldgen::processor_list::BlockEntityModifier
Local link to file: generated_symbols/data/worldgen/processor_list/BlockEntityModifier.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Literal

from generated_symbols.data.worldgen.processor_list.AppendLoot import AppendLoot
from generated_symbols.data.worldgen.processor_list.AppendStatic import AppendStatic


@dataclass(kw_only=True)
class BlockEntityModifierAppendLoot(AppendLoot):
    type: Literal['minecraft:append_loot']


@dataclass(kw_only=True)
class BlockEntityModifierAppendStatic(AppendStatic):
    type: Literal['minecraft:append_static']


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

