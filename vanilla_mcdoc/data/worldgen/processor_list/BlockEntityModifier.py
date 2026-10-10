"""
Generated from symbols.json for ::java::data::worldgen::processor_list::BlockEntityModifier
Local link to file: vanilla_mcdoc/data/worldgen/processor_list/BlockEntityModifier.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.data.worldgen.processor_list.AppendLoot import AppendLoot
from vanilla_mcdoc.data.worldgen.processor_list.AppendStatic import AppendStatic


class BlockEntityModifierAppendLoot(AppendLoot):
    type: Literal['minecraft:append_loot', 'append_loot'] = 'minecraft:append_loot'


class BlockEntityModifierAppendStatic(AppendStatic):
    type: Literal['minecraft:append_static', 'append_static'] = 'minecraft:append_static'


class BlockEntityModifierClear(GeneratedModel):
    type: Literal['minecraft:clear', 'clear'] = 'minecraft:clear'


class BlockEntityModifierPassthrough(GeneratedModel):
    type: Literal['minecraft:passthrough', 'passthrough'] = 'minecraft:passthrough'


type BlockEntityModifier = Annotated[
    BlockEntityModifierAppendLoot | BlockEntityModifierAppendStatic | BlockEntityModifierClear | BlockEntityModifierPassthrough,
    Field(discriminator='type'),
]


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
