# Generated from symbols.json for ::java::assets::block_state_definition::BlockStateDefinitionMultipartEntry
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.assets.block_state_definition.ModelVariant import ModelVariant
    from generated_symbols.assets.block_state_definition.MultiPartCondition import MultiPartCondition


@dataclass(kw_only=True)
class BlockStateDefinitionMultipartEntry:
    apply: ModelVariant
    when: MultiPartCondition | None = None  # One condition or an array where at least one condition must apply.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::block_state_definition::BlockStateDefinitionMultipartEntry": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "One condition or an array where at least one condition must apply.",
                "key": "when",
                "type": {
                    "kind": "reference",
                    "path": "::java::assets::block_state_definition::MultiPartCondition"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "apply",
                "type": {
                    "kind": "reference",
                    "path": "::java::assets::block_state_definition::ModelVariant"
                }
            }
        ]
    }
}

