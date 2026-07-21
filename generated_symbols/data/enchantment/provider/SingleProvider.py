# Generated from symbols.json for ::java::data::enchantment::provider::SingleProvider
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.IntProvider import IntProvider


@dataclass(kw_only=True)
class SingleProvider:
    enchantment: str
    level: IntProvider[int] | int


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::provider::SingleProvider": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "enchantment",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "enchantment"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "level",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::data::worldgen::IntProvider"
                    },
                    "typeArgs": [
                        {
                            "kind": "int"
                        }
                    ]
                }
            }
        ]
    }
}

