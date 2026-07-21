# Generated from symbols.json for ::java::assets::block_state_definition::MultiPartAlternatives
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.assets.block_state_definition.MultiPartCondition import MultiPartCondition


@dataclass(kw_only=True)
class MultiPartAlternatives:
    OR: list[MultiPartCondition]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::block_state_definition::MultiPartAlternatives": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "OR",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::assets::block_state_definition::MultiPartCondition"
                    }
                }
            }
        ]
    }
}

