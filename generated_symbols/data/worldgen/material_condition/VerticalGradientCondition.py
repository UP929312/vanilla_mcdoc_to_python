# Generated from symbols.json for ::java::data::worldgen::material_condition::VerticalGradientCondition
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.VerticalAnchor import VerticalAnchor


@dataclass(kw_only=True)
class VerticalGradientCondition:
    random_name: str
    true_at_and_below: VerticalAnchor
    false_at_and_above: VerticalAnchor


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::material_condition::VerticalGradientCondition": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "random_name",
                "type": {
                    "kind": "string"
                }
            },
            {
                "kind": "pair",
                "key": "True_at_and_below",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::VerticalAnchor"
                }
            },
            {
                "kind": "pair",
                "key": "False_at_and_above",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::VerticalAnchor"
                }
            }
        ]
    }
}

