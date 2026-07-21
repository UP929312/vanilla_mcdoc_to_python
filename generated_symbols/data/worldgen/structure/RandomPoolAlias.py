# Generated from symbols.json for ::java::data::worldgen::structure::RandomPoolAlias
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.util.NonEmptyWeightedList import NonEmptyWeightedList


@dataclass(kw_only=True)
class RandomPoolAlias:
    alias: str
    targets: NonEmptyWeightedList[str]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::structure::RandomPoolAlias": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "alias",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id"
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "targets",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::util::NonEmptyWeightedList"
                    },
                    "typeArgs": [
                        {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "worldgen/template_pool"
                                        }
                                    }
                                }
                            ]
                        }
                    ]
                }
            }
        ]
    }
}

