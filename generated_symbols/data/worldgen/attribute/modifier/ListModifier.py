# Generated from symbols.json for ::java::data::worldgen::attribute::modifier::ListModifier
from dataclasses import dataclass
from typing import TYPE_CHECKING, Generic, TypeVar

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.attribute.modifier.ListModifierType import ListModifierType


E = TypeVar('E')

@dataclass(kw_only=True)
class ListModifier(Generic[E]):
    modifier: ListModifierType
    argument: list[E]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::attribute::modifier::ListModifier": {
        "kind": "template",
        "child": {
            "kind": "struct",
            "fields": [
                {
                    "kind": "pair",
                    "key": "modifier",
                    "type": {
                        "kind": "reference",
                        "path": "::java::data::worldgen::attribute::modifier::ListModifierType"
                    }
                },
                {
                    "kind": "pair",
                    "key": "argument",
                    "type": {
                        "kind": "list",
                        "item": {
                            "kind": "reference",
                            "path": "::java::data::worldgen::attribute::modifier::E"
                        }
                    }
                }
            ]
        },
        "typeParams": [
            {
                "path": "::java::data::worldgen::attribute::modifier::E"
            }
        ]
    }
}

