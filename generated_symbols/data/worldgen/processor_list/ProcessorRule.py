# Generated from symbols.json for ::java::data::worldgen::processor_list::ProcessorRule
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.processor_list.BlockEntityModifier import BlockEntityModifier
    from generated_symbols.data.worldgen.processor_list.PosRuleTest import PosRuleTest
    from generated_symbols.data.worldgen.processor_list.RuleTest import RuleTest
    from generated_symbols.util.block_state.BlockState import BlockState


@dataclass(kw_only=True)
class ProcessorRule:
    location_predicate: RuleTest
    input_predicate: RuleTest
    output_state: BlockState
    position_predicate: PosRuleTest | None = None
    block_entity_modifier: BlockEntityModifier | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::processor_list::ProcessorRule": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "position_predicate",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::processor_list::PosRuleTest"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "location_predicate",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::processor_list::RuleTest"
                }
            },
            {
                "kind": "pair",
                "key": "input_predicate",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::processor_list::RuleTest"
                }
            },
            {
                "kind": "pair",
                "key": "output_state",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::block_state::BlockState"
                }
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.20"
                            }
                        }
                    }
                ],
                "key": "output_nbt",
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "dynamic",
                            "accessor": [
                                "output_state",
                                "Name"
                            ]
                        }
                    ],
                    "registry": "minecraft:block"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.20"
                            }
                        }
                    }
                ],
                "key": "block_entity_modifier",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::processor_list::BlockEntityModifier"
                },
                "optional": True
            }
        ]
    }
}

