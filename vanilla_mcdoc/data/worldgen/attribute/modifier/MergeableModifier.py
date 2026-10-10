"""
Generated from symbols.json for ::java::data::worldgen::attribute::modifier::MergeableModifier
Local link to file: generated_symbols/data/worldgen/attribute/modifier/MergeableModifier.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Generic, TypeVar

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.attribute.modifier.MergeableModifierType import MergeableModifierType


T = TypeVar('T')


class MergeableModifier(GeneratedModel, Generic[T]):
    modifier: MergeableModifierType
    argument: T


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::attribute::modifier::MergeableModifier": {
        "kind": "template",
        "child": {
            "kind": "struct",
            "fields": [
                {
                    "kind": "pair",
                    "key": "modifier",
                    "type": {
                        "kind": "reference",
                        "path": "::java::data::worldgen::attribute::modifier::MergeableModifierType"
                    }
                },
                {
                    "kind": "pair",
                    "key": "argument",
                    "type": {
                        "kind": "reference",
                        "path": "::java::data::worldgen::attribute::modifier::T"
                    }
                }
            ]
        },
        "typeParams": [
            {
                "path": "::java::data::worldgen::attribute::modifier::T"
            }
        ]
    }
}
